from abc import abstractmethod

import numpy as np
from sklearn.base import is_classifier
from sklearn.naive_bayes import GaussianNB as SKGaussianNB
from sklearn.utils.validation import check_is_fitted

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
    Base class for Naive Bayes interpretable model.
    """

    available_explanations = ["local"]
    explainer_type = "model"

    def __init__(
            self, feature_names=None, feature_types=None, nb_class=SKGaussianNB, **kwargs
    ):
        """
        Initializes class.

        Args:
            feature_names: List of feature names.
            feature_types: List of feature types.
            nb_class: A scikit-learn Gaussian Naive Bayes class.
            **kwargs: Kwargs pass to linear class at initialization time.
        """
        self.feature_names = feature_names
        self.feature_types = feature_types
        self.nb_class = nb_class
        self.kwargs = kwargs

    @abstractmethod
    def _model(self):
        # This method should be overridden.
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
        self.global_selector_ = gen_global_selector(
            len(self.feature_names_in_),
            self.feature_names_in_,
            self.feature_types_in_,
            unique_val_counts,
            None,
        )
        self.bin_counts_, self.bin_edges_ = np.histogram(X, self.feature_names_in_)

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

        X, n_samples = preclean_X(X, self.feature_names_in_, self.feature_types_in_, 0)
        X, _, _ = unify_data(
            X, n_samples, self.feature_names_in_, self.feature_types_in_, False, 0
        )

        return self.model().predict(X)
    
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
        is_classification = is_classifier(self)

        # Here starts our modifications (for binary classification)
        class_0_prior = model.class_prior_[0]
        class_1_prior = model.class_prior_[1]
        predictions = self.predict_proba(X)
        intercept = np.log(class_0_prior / class_1_prior)

        # Create conditional probabilities function...


