# Activation Functions in Neural Networks

Activation functions in neural networks are critical: they determine the output of a neural network model, introduce non-linearity into the network, and help the network learn complex patterns. Below, we explain three commonly used activation functions.

## Sigmoid Activation Function

The sigmoid function is a widely used activation function that produces an output in the range (0,1). It is defined as:

$\sigma(x) = \frac{1}{1 + e^{-x}}$

### Example:

For an input \( x = 1 \):

$\sigma(1) = \frac{1}{1 + e^{-1}} = \frac{1}{1 + \frac{1}{e}} \approx 0.731$

Thus, the output of the neuron with a sigmoid activation function for an input of 1 would be approximately 0.731.

## Tanh Activation Function

The hyperbolic tangent function, or tanh, is similar to the sigmoid but outputs values in the range (-1,1). It is defined as:

$\tanh(x) = \frac{e^x - e^{-x}}{e^x + e^{-x}}$

### Example:

For an input \( x = 1 \):

$\tanh(1) = \frac{e^1 - e^{-1}}{e^1 + e^{-1}} = \frac{e - \frac{1}{e}}{e + \frac{1}{e}} \approx 0.761$

Thus, the output of the neuron with a tanh activation function for an input of 1 would be approximately 0.761.

## ReLU Activation Function

The Rectified Linear Unit (ReLU) function is another popular activation function, especially in deep neural networks, because of its simplicity and efficiency. It is defined as:

$\text{ReLU}(x) = \max(0, x)$

### Example:

For an input \( x = 1 \):

$\text{ReLU}(1) = \max(0, 1) = 1$

And for an input \( x = -1 \):

$\text{ReLU}(-1) = \max(0, -1) = 0$

Therefore, the output of the neuron with a ReLU activation function for inputs of 1 and -1 would be 1 and 0, respectively.

Each of these functions has its advantages and drawbacks. The sigmoid and tanh functions can suffer from vanishing gradients, which can slow down learning and make them less suitable for deep networks. ReLU, on the other hand, does not activate all neurons at the same time, which means that neurons can be inactive and not respond for certain input patterns, leading to a sparsity that can be beneficial.

In practice, the choice of activation function depends on the specific application and the specific layer within the neural network. Advanced architectures may use a combination of different activation functions throughout the network.