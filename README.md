# 🔄 Perceptron

A simple implementation of the **Perceptron**, one of the earliest and most fundamental building blocks of neural networks.

The goal of this project is to make the basic idea behind a neural network easy to understand by building the mechanism from scratch.

## What is a Perceptron?

A perceptron is a simple computational model inspired by a biological neuron.

It takes several inputs, gives each input a **weight**, adds them together with a **bias**, and then applies an activation rule to produce an output.

In simplified form:

```
Inputs
  ↓
Weighted Sum + Bias
  ↓
Activation
  ↓
Output
```

For example:

```
x₁ ──w₁──┐
x₂ ──w₂──┤
x₃ ──w₃──┤──> Σ + bias ──> Activation ──> Output
          │
```

The important idea is that the weights can be **learned from data**.

## Why is it important?

The perceptron is not a modern neural network by itself, but it introduces several ideas that appear throughout neural networks:

* Inputs
* Weights
* Bias
* Activation functions
* Learning from examples
* Connecting multiple computational units

When many such units are connected together into layers, they form the basic structure of a **neural network**.

So you can think of the perceptron as a small starting point for understanding how larger neural networks work.

## What this project demonstrates

This implementation focuses on keeping the mechanism visible rather than hiding it behind a machine-learning framework.

You can experiment with:

* Different input values
* Different weights
* Bias
* Activation functions
* Training examples
* Decision boundaries

The intention is to let you **see what the model is actually doing**.

## From One Neuron to Neural Networks

A single perceptron can make a simple decision.

Connect multiple perceptrons together, and you can begin constructing a network:

```
        Perceptron
       ↙    ↓    ↘
Input ──>  Layer  ──> Output
```

This project is therefore the first step in a larger learning path:

```text
Perceptron
    ↓
Multiple Perceptrons
    ↓
Neural Network
    ↓
Backpropagation
    ↓
More complex AI models
```

## Why build it from scratch?

Modern frameworks make neural networks extremely convenient to use, but they can hide the underlying mechanics.

This project takes the opposite approach:

> **Build the small thing first. Understand the mechanism. Then scale up.**

No large model or specialized hardware is required.

Just a small piece of code that demonstrates one of the fundamental ideas behind neural networks.

---

### Part of a 10-Day AI Modeling Series

This project is part of my **10 Days of Modeling AI for Beginners** series, where I build different AI mechanisms from simple foundations and gradually move toward more complex ideas.

The goal is not to build state-of-the-art models.

The goal is to make AI **visible, understandable, and experimentable.**
