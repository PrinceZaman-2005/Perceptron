from examples.and_gate import run_and_gate


def main():
    X, y, predictions, model = run_and_gate()

    print("Perceptron - AND Gate")
    print("=" * 30)

    for inputs, target, prediction in zip(X, y, predictions):
        print(
            f"{inputs} -> "
            f"target: {target}, "
            f"prediction: {prediction}"
        )

    print("\nWeights:", model.weights)
    print("Bias:", model.bias)


if __name__ == "__main__":
    main()
