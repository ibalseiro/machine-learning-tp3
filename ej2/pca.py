import numpy as np

class PCA:
    def __init__(self, n_components: int):
        """
        Initialize PCA model.

        Args:
        - n_components (int): The number of principal components to retain.
        """
        pass

    def fit(self, X: np.ndarray) -> None:
        """
        Fit PCA model to the training data.

        Args:
        - X (np.ndarray): The training data, with shape (n_samples, n_features).
        """
        pass

    def transform(self, X: np.ndarray) -> np.ndarray:
        """
        Transform input data using the learned PCA model.

        Args:
        - X (np.ndarray): The input data, with shape (n_samples, n_features).

        Returns:
        - np.ndarray: The transformed data, with shape (n_samples, n_components).
        """
        pass

    def fit_transform(self, X: np.ndarray) -> np.ndarray:
        """
        Fit PCA model to the training data and transform the input data.

        Args:
        - X (np.ndarray): The input data, with shape (n_samples, n_features).

        Returns:
        - np.ndarray: The transformed data, with shape (n_samples, n_components).
        """
        pass
