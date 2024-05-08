import numpy as np

class KMeans:
    def __init__(self, k: int, seed: int):
        """
        Initialize KMeans clustering model.
        
        Args:
        - k (int): Number of clusters.
        - seed (int): Seed to randomly initialize the centroids.
        """
        pass
    
    def fit(self, X: np.ndarray, n_iter: int=100) -> np.ndarray:
        """
        Perform clustering on input data X into k clusters.

        Args:
        - X (np.ndarray): Input array containing data to cluster.
        - n_iter (int): Number of iterations for the KMeans algorithm.

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
