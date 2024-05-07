import numpy as np

class KMeans:
    def __init__(self):
        """
        Initialize KMeans clustering model.
        """
        pass
    
    def fit(self, X: np.ndarray, k: int) -> np.ndarray:
        """
        Perform clustering on input data X into k clusters.

        Args:
        - X (np.ndarray): Input array containing data to cluster.
        - k (int): Number of clusters.

        Returns:
        - np.ndarray: Array containing cluster labels assigned to each point.
        """
        pass
    
    def _update_centroids(self, X: np.ndarray, labels: np.ndarray) -> None:
        """
        Update centroids of clusters based on point labels.

        Args:
        - X (np.ndarray): Input array containing data.
        - labels (np.ndarray): Array containing cluster labels assigned to each point.
        """
        pass
    
    def _compute_inertia(self, X: np.ndarray, labels: np.ndarray) -> float:
        """
        Compute sum of squared distances of each point to the nearest centroid.

        Args:
        - X (np.ndarray): Input array containing data.
        - labels (np.ndarray): Array containing cluster labels assigned to each point.

        Returns:
        - float: Sum of squared distances of each point to the nearest centroid.
        """
        pass
