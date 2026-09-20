import numpy as np

from src.perceptron import Perceptron


def run_or_gate():
    # OR gate dataset
    X = np.array([
        [0, 0],
        [0, 1],
        [1, 0],
        [1, 1]
    ])

    y = np.array([0, 1, 1, 1])

    # Create and train the Perceptron
    model = Perceptron(
        learning_rate=0.1,
        epochs=100
    )

    model.fit(X, y)

    # Generate predictions
    predictions = model.predict(X)

    return X, y, predictions, model
