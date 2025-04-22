import numpy as np
from math import ceil
from sklearn.preprocessing import add_dummy_feature
import matplotlib.pyplot as plt


def MSE_gradient(X: np.ndarray, y: np.ndarray, Theta: np.ndarray) -> np.ndarray:
    """
    Calcula el gradiente del error cuadrático medio (MSE) respecto a los parámetros Theta. 
    Params:  
    """
    m = len(X)
    return 2 / m * X.T @ (X @ Theta - y) 

class GD: 
    """Clase base abstracta para algoritmos de gradient descent."""
    def __init__(self, 
                 X: np.ndarray, 
                 y: np.ndarray, 
                 learning_rate: float = 0.1, 
                 n_epoch: int = 1000):
        self.X = X
        self.y = y
        self.eta = learning_rate
        self.n_epoch = n_epoch

    def optimice(self, initial_weights: np.ndarray = None):
        raise NotImplementedError("This method must be implemented by a subclass.")
    

class BGD(GD): 
    """
    Batch Gradient Descent: Actualiza los parámertros usando TODOS los datos en cada iteración. 
    """
    def optimice(self, initial_weights = None):
        if initial_weights is None: 
            theta = np.random.rand(self.X.shape[1], 1)  # Randomly initialized model params (m x 1 vector)
        else:
            theta = initial_weights
        
        thetas = []
        error = []
        
        for epoch in range(self.n_epoch): 
            gradients = MSE_gradient(self.X, self.y, theta)
            theta = theta - self.eta * gradients
            thetas.append(theta.flatten())
            error.append(np.abs(self.X @ theta - self.y))
        return theta, thetas, error

class SGD(GD):
    """
    Stochastic Gradient Descent: Actualiza los parámetros usando una muestra aleatoria por cada iteración. 
    """

    def __init__(self, X, y, learning_rate = 0.1, n_epoch = 1000, seed: int = 42):
        super().__init__(X, y, learning_rate, n_epoch)
        self.rng = np.random.default_rng(seed)

    @staticmethod
    def learning_schedule(t: float) -> float:
        t0, t1 = 5, 50
        return t0 / (t + t1)
    
    def optimice(self, initial_weights = None):
        if initial_weights is None: 
            theta = np.random.rand(self.X.shape[1], 1)  # Randomly initialized model params
        else:
            theta = initial_weights

        m = len(self.X)
        thetas = []
        error = []

        for epoch in range(self.n_epoch):
            for i in range(m):
                rdm_index = self.rng.integers(m)
                xi = self.X[rdm_index:rdm_index + 1]
                yi = self.y[rdm_index: rdm_index + 1]
                gradients = 2 * xi.T @ (xi @ theta - yi)
                eta = self.learning_schedule(epoch * m + i)
                theta = theta - eta * gradients
                thetas.append(theta.flatten())
                error.append(np.abs(self.X @ theta - self.y))
        return theta, thetas, error

class MGD(GD):
    """
    Mini-batch Gradient Descent: Actualiza los parámetros usando pequeños subconjuntos de datos. 
    """
    def __init__(self, X, y, learning_rate = 0.1, n_epoch = 1000, minibatch_size: int = 20, seed = 42):
        super().__init__(X, y, learning_rate, n_epoch)
        self.bsize = minibatch_size
        self.rng = np.random.default_rng(seed)

    @staticmethod
    def learning_schedule(t: float) -> float:
        t0, t1 = 5, 50
        return t0 / (t + t1)
    
    def optimice(self, initial_weights = None):
        if initial_weights is None: 
            theta = np.random.rand(self.X.shape[1], 1)
        else:
            theta = initial_weights
        
        m = len(self.X)
        n_batches_per_epoch = ceil(m / self.bsize)
        thetas = []
        error = []

        for epoch in range(self.n_epoch): 
            shuffled_indices = self.rng.permutation(m)
            X_shuffled = self.X[shuffled_indices]
            y_shuffled = self.y[shuffled_indices]
            
            for iteration in range(0, n_batches_per_epoch):
                idx = iteration * self.bsize
                xi = X_shuffled[idx: idx + self.bsize]
                yi = y_shuffled[idx: idx + self.bsize]
                gradients = 2 / self.bsize * xi.T @ (xi @ theta - yi)
                eta = self.learning_schedule(iteration)
                theta = theta - eta * gradients
                thetas.append(theta.flatten())
                error.append(np.abs(self.X @ theta - self.y))
        return theta, thetas, error


def generate_random_linear_data(n_samples: int = 100, noise_std: float = 1.0, seed: int = 0):
    """
    Genera datos sintéticos para regresión lineal: y = theta_0 + theta_1 * x + ruido

    Retorna:
    - X_b: matriz de características con columna de bias incluida
    - y: vector objetivo
    - true_theta: vector con los parámetros reales [theta_0, theta_1]
    """
    rng = np.random.default_rng(seed)
    X = 2 * rng.random((n_samples, 1))  # valores de x entre 0 y 2
    true_theta = np.array([[4], [3]])  # intercepto = 4, pendiente = 3
    y = true_theta[0] + true_theta[1] * X + rng.normal(0, noise_std, size=(n_samples, 1))
    X_b = add_dummy_feature(X)  # añade columna de 1s (bias)
    return X_b, y, true_theta

def plot_theta_paths(paths, labels, true_theta):
    """
    Plotea las trayectorias de descenso de theta en el espacio (θ₀, θ₁).
    """
    plt.figure(figsize=(8, 6))
    for thetas, label in zip(paths, labels):
        thetas = np.array(thetas)
        plt.plot(thetas[:, 0], thetas[:, 1], label=label, marker='o', markersize=2, linewidth=1)
    plt.scatter(true_theta[0], true_theta[1], c='black', marker='x', s=100, label='True θ')
    plt.xlabel(r'$\theta_0$')
    plt.ylabel(r'$\theta_1$')
    plt.title("Trajectories of θ during optimization")
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == '__main__':
    # Generar datos sintéticos
    X, y, true_theta = generate_random_linear_data(n_samples=100, noise_std=1.0, seed=42)

    # Ejecutar los 3 algoritmos de descenso
    bgd = BGD(X, y, learning_rate=0.1, n_epoch=50)
    sgd = SGD(X, y, n_epoch=50)
    mgd = MGD(X, y, minibatch_size=10, n_epoch=50)

    _, bgd_path, _ = bgd.optimice()
    _, sgd_path, _ = sgd.optimice()
    _, mgd_path, _ = mgd.optimice()

    # Plotear trayectorias de optimización
    plot_theta_paths(
        [bgd_path, sgd_path, mgd_path],
        labels=["Batch GD", "Stochastic GD", "Mini-batch GD"],
        true_theta=true_theta.flatten()
    )