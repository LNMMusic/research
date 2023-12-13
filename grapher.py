import matplotlib.pyplot as plt
import numpy as np

# Create a range of epochs
epochs = np.arange(1, 51)

# Simulate a loss curve for the training set: decreasing over time
training_loss = 1 / (0.1 * epochs + 0.5)

# Simulate a loss curve for the validation set: decrease, then increase after a point (overfitting)
validation_loss = training_loss.copy()
validation_loss[15:] = np.linspace(validation_loss[15], validation_loss[15] + 0.3, len(validation_loss[15:]))

# Plotting the training and validation loss
plt.figure(figsize=(10, 5))
plt.plot(epochs, training_loss, label='Training Loss')
plt.plot(epochs, validation_loss, label='Validation Loss', linestyle='--')
plt.title('Example of Overfitting in Training')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig('overfitting.png')