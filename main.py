from gates.and_gate import run_and_gate
from gates.or_gate import run_or_gate


def display_results(name, X, y, predictions, model):
    print(f"Perceptron - {name} Gate")
    print("=" * 30)

    for inputs, target, prediction in zip(X, y, predictions):
        print(
            f"{inputs} -> "
            f"target: {target}, "
            f"prediction: {prediction}"
        )

    print("\nWeights:", model.weights)
    print("Bias:", model.bias)
    print()


def main():
    # Run AND gate
    X, y, predictions, model = run_and_gate()
    display_results("AND", X, y, predictions, model)

    # Run OR gate
    X, y, predictions, model = run_or_gate()
    display_results("OR", X, y, predictions, model)


if __name__ == "__main__":
    main()
