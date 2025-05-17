import numpy as np

# Define dataset parameters
num_samples = 5000  # Number of sequences
sequence_length = 100  # Timesteps per sample
feature_dim = 10  # Features per timestep
output_dim = 256  # Label categories

def generate_dataset(num_samples, sequence_length, feature_dim, output_dim):
    """Generates synthetic time-series data and labels"""
    X = np.random.rand(num_samples, sequence_length, feature_dim)  # Random sequences
    y = np.random.randint(0, output_dim, size=(num_samples,))  # Random categorical labels
    
    # Convert labels to one-hot encoding
    y_one_hot = np.zeros((num_samples, output_dim))
    y_one_hot[np.arange(num_samples), y] = 1
    
    return X, y_one_hot

# Generate dataset
X_train, y_train = generate_dataset(num_samples, sequence_length, feature_dim, output_dim)

# Save dataset
np.save("X_train.npy", X_train)
np.save("y_train.npy", y_train)

print("Dataset saved as 'X_train.npy' and 'y_train.npy'.")
