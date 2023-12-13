# Loss Functions and Optimization in Backpropagation

In the context of neural networks, backpropagation is the method used for learning by iteratively updating the weights. It consists of two main phases: the forward pass, where the predictions are made; and the backward pass, or backpropagation, where the weights are updated in response to the output errors. The loss function and optimization process play critical roles during backpropagation.

## Loss Function

The loss function, also known as cost or objective function, is a measure of how well the neural network performs. It quantifies the difference between the predicted outputs of the network and the actual target values. The goal of training a neural network is to minimize this loss function.

The loss function, also known as cost or objective function, is a measure of the neural network's performance. It quantifies the difference between the network's predicted outputs ($\hat{y}$) and the actual target values ($y$). The goal of training is to minimize this loss function.

### Common Loss Functions

- **Mean Squared Error (MSE)** for regression tasks:
$\text{MSE} = \frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2$
where $y_i$ is the true value and $\hat{y}_i$ is the predicted value from the network.

- **Cross-Entropy Loss** for classification tasks:
$\text{Cross-Entropy} = -\sum_{c=1}^{M} y_{o,c} \log(p_{o,c})$
where $M$ is the number of classes, $y$ is a binary indicator of whether class label $c$ is the correct classification for observation $o$, and $p$ is the predicted probability that observation $o$ is of class $c$.


### Landscape of Loss Functions

The loss function can be visualized as a landscape with multiple dimensions representing the model's parameters (weights and biases). Each point on this landscape corresponds to a specific loss value, calculated based on the model's predictions for a given set of parameters.

We feed the model with an input `x`, calculate the activations with parameters (weights `w` and biases `b`) that produce the output `y`.

We check the loss, `L` = `y` - `y_hat`

<!-- make a table with for different combinations of w and b to get z -->
For a given `x`...
Example Loss Landscape:
| Weights (w) | Biases (b) | Loss (L) |
|-------------|------------|----------|
| 1           | 1          | 3        |
| 2           | 1          | 4        |
| 1           | 2          | 4        |
| 2           | 2          | 5        |

The goal is to find the combination of weights `w` and biases `b` that gives us the lowest loss value `L`.

We can navigate this landscape by changing the weights and biases, but this would be a very slow process.

To navigate this landscape efficiently, we use gradient descent, which leverages the gradient of the loss function to update the weights and biases in the direction that reduces the loss.

Minima Types:
- **Local Minimum**: The lowest point within a specific region.
- **Global Minimum**: The lowest point across the entire landscape.

Achieving the global minimum is ideal but challenging due to the presence of multiple local minima. Advanced optimization techniques and proper hyperparameter tuning are crucial for successful training.

## Optimization During Backpropagation

Optimization refers to the process of adjusting the weights and biases of the network to minimize the loss function. This process involves calculating the gradient of the loss function with respect to the weights and then updating the weights in the opposite direction of the gradient.

### Gradient Descent

The most common optimization algorithm used in neural networks is gradient descent. The weights are updated as follows:

$W_{new} = W_{old} - \eta \cdot \nabla L(W_{old})$

where:
- $W_{new}$ and $W_{old}$ are the new and old values of the weights, respectively.
- $\eta$ is the learning rate, a hyperparameter that controls the step size during the learning process.
- $\nabla L(W_{old})$ is the gradient of the loss function with respect to the old weights.

The learning rate in neural network training indeed acts as a control on the magnitude of weight updates during backpropagation. However, its primary purpose is not to prevent overfitting or underfitting directly; rather, it is to ensure that the optimization process progresses in a stable and efficient manner towards the minimum of the loss function. Here's a breakdown of its role:

### Convergence and Stability
- **Too High Learning Rate:** If the learning rate is too high, the weight updates can be so large that they overshoot the minimum, causing the optimization to diverge or leading to unstable training where the loss does not decrease in a predictable manner.
- **Too Low Learning Rate:** Conversely, if the learning rate is too low, the training process can become very slow because the weights are updated only by a tiny amount at each iteration. This might also result in the optimization getting stuck in local minima rather than finding the global minimum.

---

### Backpropagation Algorithm

1. **Forward Pass:**
   - Compute the output of the network using the current weights.
   - Evaluate the loss function comparing the network's output to the true target values.

2. **Backward Pass:**
   - Calculate the gradient of the loss function with respect to each weight (partial derivatives).
   - Use chain rule to backpropagate the gradients through the layers.
   - Update the weights by taking a step proportional to the negative of the gradients.

### Stochastic Gradient Descent (SGD)

A variant of gradient descent is Stochastic Gradient Descent (SGD), where the weights are updated after computing the gradient on a small subset or batch of the data, rather than the entire dataset at once. This method is less computationally intensive and often leads to faster convergence.

### Advanced Optimizers

There are more sophisticated optimization algorithms that adjust the learning rate dynamically and can lead to better performance:

- **Momentum:** Adds a fraction of the previous weight update to the current one, which helps accelerate gradients vectors in the right directions.
- **Adagrad:** Adapts the learning rate to the parameters, performing smaller updates for frequently updated parameters and larger updates for infrequent ones.
- **RMSprop:** Modifies Adagrad by using a moving average of squared gradients to adjust the learning rate.
- **Adam (Adaptive Moment Estimation):** Combines the ideas of Momentum and RMSprop by using both first and second moments of the gradients.

## Numerical Example

Consider a simple neural network with a single neuron using mean squared error as the loss function. Suppose the neuron's current weight is $W = 2$, the true target value is $y = 3$, and the predicted value after the forward pass is $\hat{y} = 1.5$.

The loss function is:
$L = \frac{1}{2} (y - \hat{y})^2 = \frac{1}{2} (3 - 1.5)^2 = \frac{1}{2} \cdot 2.25 = 1.125$

The derivative of $L$ with respect to $W$ is:
$\frac{\partial L}{\partial W} = \frac{\partial L}{\partial \hat{y}} \cdot \frac{\partial \hat{y}}{\partial W}$
$\frac

{\partial L}{\partial W} = -(y - \hat{y}) \cdot x = -(3 - 1.5) \cdot 1 = -1.5$

If we choose a learning rate $\eta = 0.1$, the weight update would be:
$W_{new} = W_{old} - \eta \cdot \frac{\partial L}{\partial W} = 2 - 0.1 \cdot (-1.5) = 2 + 0.15 = 2.15$

By iterating this process over many epochs, the network will gradually minimize the loss function, improving its predictions.