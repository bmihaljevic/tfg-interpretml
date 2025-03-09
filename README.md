# Extending [InterpretML](https://github.com/interpretml/interpret)

As it Github page says:

"**InterpretML** is an open-source package that incorporates state-of-the-art machine learning **interpretability techniques** under one roof. With this package, you can train interpretable glassbox models and explain blackbox systems. InterpretML helps you understand your model's global behavior, or understand the reasons behind individual predictions."

---

### Objective of this Extension

Currently, InterpretML implements several interpretable models, such as Explainable Boosting Machines (EBMs), decision trees, and linear models, along with various explanation techniques for blackbox models.

This extension aims to expand InterpretML by integrating probabilistic models while leveraging the existing explanation mechanisms provided by the library. By doing so, we enable users to analyze uncertainty, quantify probabilistic predictions, and gain deeper insights into model behavior beyond point estimates.

---

### How InterpretML visualize glassbox models?

InterpretML uses two main ways to explain these type of models:

- **Global Explanations**: These explanations provide insights into how a model makes predictions across the **entire dataset**. Example: How the score 

<img width="700" align="center" alt="Image" src="https://github.com/user-attachments/assets/8891b574-9e1d-488c-afee-4caef393f98a" />

<br>

- **Local Explanations**: These explanations focus on **individual predictions**, showing why the model made a specific decision for a given instance.

<img width="700" align="center" alt="Image" src="https://github.com/user-attachments/assets/51e6264e-83a4-4690-8ebf-c687d2ede98a" />

<br>

The main goal will be to use both global and local visualizations for different models that InterpretML does not currently implement.

---

### Adding new models

The new models incorporated in this extension are:

- **Naive Bayes** (Gaussian and Categorical): A simple yet powerful probabilistic model based on Bayes' theorem. It assumes feature independence, making it highly efficient for classification tasks.

- **TAN** (Tree Augmented Naive Bayes): An extension of Naive Bayes that allows for dependencies between features using a tree structure, improving its expressiveness while maintaining efficiency.

- **Bayesian Network**: A probabilistic graphical model that represents variables and their conditional dependencies via a directed acyclic graph (DAG). It is useful for modeling complex probabilistic relationships.

- **NAM** (Neural Additive Model): A neural network-based approach that extends Generalized Additive Models (GAMs) by learning feature contributions in a flexible and interpretable manner.

These models will be integrated with InterpretML's existing explanation mechanisms, ensuring users can interpret their predictions using global and local explanations.

---

