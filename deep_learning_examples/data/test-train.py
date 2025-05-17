import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
from tensorflow.keras.optimizers import Adam

# Define model parameters
learning_rate = 0.001
output_dim = 256
output_activation = "softmax"
activation = "relu"
input_shape = (100, 10)  # Example input shape (timesteps, features)

# Create LSTM model
model = Sequential([
    LSTM(units=output_dim, activation=activation, input_shape=input_shape, return_sequences=False),
    Dense(output_dim, activation=output_activation)
])

# Compile the model
optimizer = Adam(learning_rate=learning_rate)
model.compile(optimizer=optimizer, loss="categorical_crossentropy", metrics=["accuracy"])

# Load dataset (ensure correct paths)
X_train = np.load("X_train.npy")
y_train = np.load("y_train.npy")

# Save the model properly
model.save("lstm_model.h5")

print("Model saved as 'lstm_model.h5'.")
