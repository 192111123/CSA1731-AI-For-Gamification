import numpy as np

class NeuralNetwork:
    def __init__(self, layers):
        self.layers = layers
        self.params = {}
        self.cache = {}
        self.grads = {}
        self.initialize_parameters()

    def initialize_parameters(self):
        np.random.seed(1)
        for l in range(1, len(self.layers)):
            self.params['W' + str(l)] = np.random.randn(self.layers[l], self.layers[l-1]) * 0.01
            self.params['b' + str(l)] = np.zeros((self.layers[l], 1))

    def relu(self, Z):
        return np.maximum(0, Z)

    def relu_derivative(self, dA, Z):
        dZ = np.array(dA, copy=True)
        dZ[Z <= 0] = 0
        return dZ

    def sigmoid(self, Z):
        return 1 / (1 + np.exp(-Z))

    def sigmoid_derivative(self, dA, Z):
        s = self.sigmoid(Z)
        return dA * s * (1 - s)

    def forward(self, X):
        self.cache['A0'] = X
        A = X
        for l in range(1, len(self.layers)):
            Z = np.dot(self.params['W' + str(l)], A) + self.params['b' + str(l)]
            self.cache['Z' + str(l)] = Z
            if l == len(self.layers) - 1:
                A = self.sigmoid(Z)
            else:
                A = self.relu(Z)
            self.cache['A' + str(l)] = A
        return A

    def compute_cost(self, A, Y):
        m = Y.shape[1]
        cost = -(1/m) * np.sum(Y * np.log(A) + (1 - Y) * np.log(1 - A))
        return np.squeeze(cost)

    def backward(self, Y):
        m = Y.shape[1]
        Y = Y.reshape(self.cache['A' + str(len(self.layers) - 1)].shape)
        
        dA = -(np.divide(Y, self.cache['A' + str(len(self.layers) - 1)]) - np.divide(1 - Y, 1 - self.cache['A' + str(len(self.layers) - 1)]))

        for l in reversed(range(1, len(self.layers))):
            dZ = self.sigmoid_derivative(dA, self.cache['Z' + str(l)]) if l == len(self.layers) - 1 else self.relu_derivative(dA, self.cache['Z' + str(l)])
            dW = (1/m) * np.dot(dZ, self.cache['A' + str(l - 1)].T)
            db = (1/m) * np.sum(dZ, axis=1, keepdims=True)
            dA = np.dot(self.params['W' + str(l)].T, dZ)
            
            self.grads['dW' + str(l)] = dW
            self.grads['db' + str(l)] = db

    def update_parameters(self, learning_rate):
        for l in range(1, len(self.layers)):
            self.params['W' + str(l)] -= learning_rate * self.grads['dW' + str(l)]
            self.params['b' + str(l)] -= learning_rate * self.grads['db' + str(l)]

    def fit(self, X, Y, epochs, learning_rate):
        for i in range(epochs):
            A = self.forward(X)
            cost = self.compute_cost(A, Y)
            self.backward(Y)
            self.update_parameters(learning_rate)

            if i % 100 == 0:
                print(f"Cost after iteration {i}: {cost}")

    def predict(self, X):
        A = self.forward(X)
        predictions = (A > 0.5)
        return predictions


    # Example usage:
if __name__ == "__main__":
    # Generate dummy data for XOR problem
    X = np.array([[0, 0, 1, 1],
                  [0, 1, 0, 1]])
    Y = np.array([[0, 1, 1, 0]])

    # Define the neural network with 2 input neurons, 4 neurons in the hidden layer, and 1 output neuron
    nn = NeuralNetwork(layers=[2, 4, 1])

    # Train the neural network
    nn.fit(X, Y, epochs=10000, learning_rate=0.1)

    # Make predictions
    predictions = nn.predict(X)
    print("Predictions:")
    print(predictions)
    print("Actual values:")
    print(Y)

