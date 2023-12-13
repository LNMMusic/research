# Building the Model with Keras using Sequential
In this guide, we'll build a neural network using the Keras Sequential API. We start defining the layers of the model, including number of neurons, activation functions, and input and output shapes. This elements are more related to the forward propagation process.

## `Layers`
Layers are composed with the following components:
- `Units`: represent the number of neurons in the layer.
- `Activation Function`: determines the output of a node in a neural network.
- `Regularizer`: applies penalties on layer parameters or layer activity during optimization to prevent overfitting (backpropagation process).
- `Input Shape`: the shape of the input data.
- `Output Shape`: the shape of the output data.

### `Structure`
- Input Layer: the initial layer that receives input with a shape that matches the number of features in the dataset.
- Hidden Layers: layers between the input and output layers. Where the neural network begins to learn from the input data. Each layer can have its own number of neurons and activation function.
- Output Layer: produces the final output of the model. Its configuration depends on the type of problem (e.g., regression, binary classification, multi-class classification).

### `Types`
- `Dense`: The most common layer type. It connects every neuron in one layer to every neuron in another layer.
- `Convolutional`: Used for image processing, including image recognition, object detection, and image segmentation.
- `Pooling`: Used in conjunction with convolutional layers to downsample feature maps.
- `Recurrent`: Used for sequential data. It processes sequences of inputs by iterating through the sequence elements and maintaining a state containing information relative to what it has seen so far.
- `Dropout`: Used to prevent overfitting. It randomly drops some neurons during training to reduce interdependent learning amongst the neurons.
- `Flatten`: Used to flatten the input. It's typically used between convolutional and dense layers.


## `Activation Functions`
Activation functions determine the output of a node in a neural network. Here are some common activation functions:

- **ReLU (Rectified Linear Unit)**: Outputs the input if it is positive; otherwise, it outputs zero. It's the most commonly used activation function in neural networks due to its simplicity and efficiency.
- **Sigmoid**: Maps the input into a range between 0 and 1. It's often used for binary classification.
- **Softmax**: Used in multi-class classification problems. It converts the outputs for each class into probabilities.
- **Tanh (Hyperbolic Tangent)**: Similar to the sigmoid but maps the input to a range between -1 and 1.
- **Leaky ReLU**: A variation of ReLU that allows a small gradient when the unit is not active.

Here an example of a model with a ReLU activation function:
```python
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# Example: Building a model
model = Sequential([
    Dense(64, activation='relu', input_shape=(input_shape,)),  # Input layer
    Dense(64, activation='relu'),                              # Hidden layer
    Dense(num_classes, activation='softmax')                   # Output layer
])
```

<br>

---

<br>

# Compiling the Model
After defining the model architecture, we need to compile the model. Compiling the model takes three parameters: the optimizer, the loss function, and the metrics. This elements are more related to the backpropagation process.

## `Loss Function`

The loss function measures how well the model performs. It calculates the difference between the model's predictions and the actual data.

- **Mean Squared Error (MSE)**: Commonly used in regression tasks.
- **Cross-Entropy**: Used in classification tasks. Variants include binary cross-entropy for binary classification and categorical cross-entropy for multi-class classification.

## `Optimizer`

The optimizer is an algorithm that changes the attributes of the neural network, such as weights and learning rate, to reduce losses.

- **SGD (Stochastic Gradient Descent)**: Traditional, simple optimizer.
- **Adam**: Combines the best properties of the AdaGrad and RMSProp algorithms to provide an optimization algorithm that can handle sparse gradients on noisy problems.
- **RMSprop**: Works well in online and non-stationary settings.

## `Metrics`

Metrics are used to evaluate the performance of your model.

- **Accuracy**: Commonly used in classification tasks.
- **Precision, Recall, F1-Score**: Used in classification, especially with imbalanced datasets.

```python
# Example: Compiling the model
model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])
```

Later we are gonna see a more detailed documentation about the metrics, specially the recall and precision which are important during training analysis.

<br>

---

<br>

# Conclusion

Building a neural network in Keras involves defining the model architecture with input, hidden, and output layers, selecting activation functions, and compiling the model with a specific loss function, optimizer, and metrics. This guide provides a basic framework for constructing a standard neural network in Keras.