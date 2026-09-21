import numpy as np


class Perceptron:
    """
    A simple Perceptron implementation using NumPy.

    The Perceptron learns a binary classification rule by
    adjusting its weights and bias based on prediction errors.
    """

    def __init__(self, learning_rate=0.1, epochs=100):
        self.learning_rate = learning_rate
        self.epochs = epochs

        self.weights = None
        self.bias = 0.0

    def activation(self, value):
        """Step activation function."""
        return 1 if value >= 0 else 0

    def predict(self, inputs):
        """Predict the class for one or more input samples."""
        inputs = np.asarray(inputs)

        weighted_sum = np.dot(inputs, self.weights) + self.bias

        return np.where(weighted_sum >= 0, 1, 0)

    def fit(self, X, y):
        """Train the Perceptron on a dataset."""
        X = np.asarray(X)
        y = np.asarray(y)

        # Initialize weights according to the number of features.
        self.weights = np.zeros(X.shape[1])
        self.bias = 0.0

        for _ in range(self.epochs):
            errors = 0

            for inputs, target in zip(X, y):
                prediction = self.activation(
                    np.dot(inputs, self.weights) + self.bias
                )

                error = target - prediction

                # Perceptron learning rule
                self.weights += self.learning_rate * error * inputs
                self.bias += self.learning_rate * error

                if error != 0:
                    errors += 1

            # Stop early if every sample was classified correctly.
            if errors == 0:
                break

        return self
