from abc import abstractmethod

import numpy as np
from sklearn.base import ClassifierMixin, is_classifier
from sklearn.naive_bayes import CategoricalNB as SKCategoricalNB
from sklearn.utils.validation import check_is_fitted

from ..api.base import ExplainerMixin
from ..api.templates import FeatureValueExplanation
from ..utils._clean_simple import clean_dimensions, typify_classification
from ..utils._clean_x import preclean_X
from ..utils._explanation import (
    gen_global_selector,
    gen_local_selector,
    gen_name_from_class,
    gen_perf_dicts,
)
from ..utils._unify_data import unify_data

class BaseNaiveBayes:
    """
    Base class for Categorical Naive Bayes interpretable model.
    """

    available_explanations = ["local"]
    explainer_type = "model"

    def __init__(
            self, feature_names=None, feature_types=None, nb_class=SKCategoricalNB, **kwargs
    ):
        """
        Initializes class.
        
        Args:
            feature_names: List of feature names.
            feature_types: List of feature types.
            nb_class: A scikit-learn Categorical Naive Bayes class.
            **kwargs: Kwargs pass to Naive Bayes class at initialization time.
        """
        self.feature_names = feature_names
        self.feature_types = feature_types
        self.nb_class = nb_class
        self.kwargs = kwargs

    @abstractmethod
    def _model(self):
        # This method should be overriden.
        return None
    
    def fit(self, X, y):
        """
        Fits the model.
        
        Args:
            X: Numpy array for training instances.
            y: Numpy array as training labels.
        """

        y = clean_dimensions(y, "y")
        if y.ndim != 1:
            msg = "y must be 1 dimensional"
            raise ValueError(msg)
        if len(y) == 0:
            msg = "y cannot have 0 samples"
            raise ValueError(msg)
        
        if is_classifier(self.nb_class):
            y = typify_classification(y)
        else:
            y = y.astype(np.float64, copy=False)

        X, n_samples = preclean_X(X, self.feature_names, self.feature_types, len(y))

        X, self.feature_names_in_, self.feature_types_in_ = unify_data(
            X, n_samples, self.feature_names, self.feature_types, False, 0
        )

        self.model = self._model()
        self.model.fit(X, y)

        self.n_features_in_ = len(self.feature_names_in_)
        if is_classifier(self.nb_class):
            self.classes_ = self.model.classes_

        self.X_mins_ = np.min(X, axis=0)
        self.X_maxs_ = np.max(X, axis=0)
        self.categorical_uniq_ = {}

        for i, feature_type in enumerate(self.feature_types_in_):
            if feature_type in ("nominal", "ordinal"):
                self.categorical_uniq_[i] = sorted(set(X[:, i]))

        unique_val_counts = np.zeros(len(self.feature_names_in_), dtype=np.int64)
        for col_idx in range(len(self.feature_names_in_)):
            X_col = X[:, col_idx]
            unique_val_counts[col_idx] = len(np.unique(X_col))

        # to use in the global explanation
        self.global_selector = gen_global_selector(
            len(self.feature_names_in_),
            self.feature_names_in_,
            self.feature_types_in_,
            unique_val_counts,
            None,
        )
        self.bin_counts_, self.bin_edges_ = _hist_per_column(X, self.feature_types_in_)

        self.has_fitted_ = True

        return self
    
    def predict(self, X):
        """Predicts on provided instances.
        
        Args:
            X: Numpy array for instances.
            
        Returns:
            Predicted class label per instance
        """

        check_is_fitted(self, "has_fitted_")

        X, n_samples = preclean_X(X, self.feature_names_in_, self.feature_types_in_)
        X, _, _ = unify_data(
            X, n_samples, self.feature_names_in_, self.feature_types_in_, False, 0
        )

        return self._model().predict(X)
    
    def explain_local(self, X, y=None, name=None):
        """Provides local explanations for provided instances.

        Args:
            X: Numpy array for X to explain.
            y: Numpy vector for y to explain.
            name: User-defined explanation name.

        Returns:
            An explanation object, visualizing feature-value pairs
            for each instance as horizontal bar charts.
        """

        check_is_fitted(self, "has_fitted_")

        if name is None:
            name = gen_name_from_class(self)

        n_samples = None
        if y is not None:
            y = clean_dimensions(y, "y")
            if y.ndim != 1:
                msg = "y must be 1 dimensional"
                raise ValueError(msg)
            n_samples = len(y)

            if is_classifier(self):
                y = typify_classification(y)
            else:
                y = y.astype(np.float64, copy=False)

        X, n_samples = preclean_X(
            X, self.feature_names_in_, self.feature_types_in_, n_samples
        )

        if n_samples == 0:
            msg = "X cannot have 0 samples"
            raise ValueError(msg)
        
        X, _, _ = unify_data(
            X, n_samples, self.feature_names_in_, self.feature_types_in_, False, 0
        )

        model = self._model()

        classes = None
        is_classification = is_classifier(model)

       # Here starts our modifications (for binary classification)
        def conditional_probabilities(model, X, alpha):
            cp_0 = np.zeros(X.shape[0])
            cp_1 = np.zeros(X.shape[0])
            for j in range(X.shape[0]):
                cp_0[j] = (model.category_count_[j][0][int(X[j])] + alpha) / (model.class_count_[0] + alpha * model.category_count_[j].shape[1])
                cp_1[j] = (model.category_count_[j][1][int(X[j])] + alpha) / (model.class_count_[1] + alpha * model.category_count_[j].shape[1])
            return cp_0, cp_1

        class_0_prior = model.class_count_[0] / model.class_count_.sum()
        class_1_prior = model.class_count_[1] / model.class_count_.sum()
        predictions = self.predict_proba(X)
        intercept = np.log(class_0_prior / class_1_prior)

        data_dicts = []
        scores_list = []
        perf_list = []
        perf_dicts = gen_perf_dicts(predictions, y, is_classification, classes)
        for i, instance in enumerate(X):
            c0_cp, c1_cp = conditional_probabilities(model, instance, 1)
            scores = np.log(c0_cp / c1_cp)
            print("Instance", i)
            print(intercept)
            print(c0_cp, c1_cp)
            print(scores)
            print()
            scores_list.append(scores)
            data_dict = {}
            data_dict["data_type"] = "univariate"

            # Performance related (conditional)
            perf_dict_obj = None if perf_dicts is None else perf_dicts[i]
            data_dict["perf"] = perf_dict_obj
            perf_list.append(perf_dict_obj)

            # Names/scores
            data_dict["names"] = self.feature_names_in_
            data_dict["scores"] = scores

            # Values
            data_dict["values"] = instance

            data_dict["extra"] = {
                "names": ["Intercept"],
                "scores": [intercept],
                "values": [1],
            }
            data_dicts.append(data_dict)

        internal_obj = {
            "overall": None,
            "specific": data_dicts,
            "mli": [
                {
                    "explanation_type": "local_feature_importance",
                    "value": {
                        "scores": scores_list,
                        "intercept": intercept,
                        "perf": perf_list,
                    },
                }
            ],
        }
        internal_obj["mli"].append(
            {
                "explanation_type": "evaluation_dataset",
                "value": {"dataset": X, "dataset_y": y},
            }
        )

        selector = gen_local_selector(data_dicts, is_classification=is_classification)

        return FeatureValueExplanation(
            "local",
            internal_obj,
            feature_names=self.feature_names_in_,
            feature_types=self.feature_types_in_,
            name=name,
            selector=selector,
        )

class NaiveBayesExplanation(FeatureValueExplanation):
    """Visualizes specifically for NB methods."""

    explanation_type = None

    def __init__(
        self, 
        explanation_type, 
        internal_obj, 
        feature_names=None, 
        feature_types=None, 
        name=None, 
        selector=None,
    ):
        """Initializes class.
        
        Args:
            explanation_type:  Type of explanation.
            internal_obj: A jsonable object that backs the explanation.
            feature_names: List of feature names.
            feature_types: List of feature types.
            name: User-defined name of explanation.
            selector: A dataframe whose indices correspond to explanation entries.
        """
        super().__init__(
            explanation_type, 
            internal_obj, 
            feature_names, 
            feature_types, 
            name, 
            selector,
        )

    def visualize(self, key=None):
        """Provides interactive visualizations.

        Args:
            key: Either a scalar or list
                that indexes the internal object for sub-plotting.
                If an overall visualization is requested, pass None.

        Returns:
            A Plotly figure.
        """
        from ..visual.plot import (
            get_explanation_index,
            get_sort_indexes,
            mli_plot_horizontal_bar,
            mli_sort_take,
            plot_horizontal_bar,
            sort_take,
        )

        if isinstance(key, tuple) and len(key) == 2:
            provider, key = key
            if (
                provider == "mli"
                and "mli" in self.data(-1)
                and self.explanation_type == "global"
            ):
                explanation_list = self.data(-1)["mli"]
                explanation_index = get_explanation_index(
                    explanation_list, "global_feature_importance"
                )
                scores = explanation_list[explanation_index]["value"]["scores"]
                sort_indexes = get_sort_indexes(
                    scores, sort_fn=lambda x: -abs(x), top_n=15
                )
                sorted_scores = mli_sort_take(
                    scores, sort_indexes, reverse_results=True
                )
                sorted_names = mli_sort_take(
                    self.feature_names, sort_indexes, reverse_results=True
                )
                return mli_plot_horizontal_bar(
                    sorted_scores,
                    sorted_names,
                    title="Overall Importance:<br>Coefficients",
                )
            # pragma: no cover
            msg = f"Visual provider {provider} not supported"
            raise RuntimeError(msg)
        data_dict = self.data(key)
        if data_dict is None:
            return None

        if self.explanation_type == "global" and key is None:
            data_dict = sort_take(
                data_dict, sort_fn=lambda x: -abs(x), top_n=15, reverse_results=True
            )
            return plot_horizontal_bar(
                data_dict, title="Overall Importance:<br>Coefficients"
            )

        return super().visualize(key)
    
class NaiveBayesClassifier(BaseNaiveBayes, ClassifierMixin, ExplainerMixin):
    """Naive Bayes.
    
    Currently wrapper around Naive Bayes in scikit-learn: https://github.com/scikit-learn/scikit-learn
    """

    def __init__(
            self, feature_names=None, feature_types=None, nb_class=SKCategoricalNB, **kwargs
    ):
        """Initializes class.
        
        Args:
            feature_names: List of feature names.
            feature_types: List of feature types.
            nb_class: A scikit-learn Gaussian Naive Bayes class.
            **kwargs: Kwargs pass to Naive Bayes class at initialization time.
        """
        super().__init__(feature_names, feature_types, nb_class, **kwargs)

    def _model(self):
        return self.sk_model_
    
    def fit(self, X, y):
        """Fits model to provided instance.
        
        Args:
            X: Numpy array for training instances.
            y: Numpy array as training labels.
        """
        self.sk_model_ = self.nb_class(**self.kwargs)
        return super().fit(X, y)
    
    def predict_proba(self, X):
        """Probability estimates on provided instances.

        Args:
            X: Numpy array for instances.

        Returns:
            Probability estimate of instance for each class.
        """

        check_is_fitted(self, "has_fitted_")

        X, n_samples = preclean_X(X, self.feature_names_in_, self.feature_types_in_)
        X, _, _ = unify_data(
            X, n_samples, self.feature_names_in_, self.feature_types_in_, False, 0
        )

        return self.model.predict_proba(X)

def _hist_per_column(arr, feature_types=None):
    counts = []
    bin_edges = []

    if feature_types is not None:
        for i, feat_type in enumerate(feature_types):
            if feat_type == "continuous":
                count, bin_edge = np.histogram(arr[:, i], bins="doane")
                counts.append(count)
                bin_edges.append(bin_edge)
            elif feat_type in ("nominal", "ordinal"):
                # Todo: check if this call
                bin_edge, count = np.unique(arr[:, i], return_counts=True)
                counts.append(count)
                bin_edges.append(bin_edge)
    else:
        for i in range(arr.shape[1]):
            count, bin_edge = np.histogram(arr[:, i], bins="doane")
            counts.append(count)
            bin_edges.append(bin_edge)
    return counts, bin_edges