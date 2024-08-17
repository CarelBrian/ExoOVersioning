import matplotlib.pyplot as plt
import numpy as np

def plot_functions():
    x = np.linspace(-10, 10, 400)
    y1 = x ** 2
    y2 = x ** 3

    plt.figure(figsize=(10, 5))

    # Tracer y = x^2
    plt.subplot(1, 2, 1)
    plt.plot(x, y1, label="y = x^2", color='blue')
    plt.title("Graph of y = x^2")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True)
    plt.legend()

    # Tracer y = x^3
    plt.subplot(1, 2, 2)
    plt.plot(x, y2, label="y = x^3", color='green')
    plt.title("Graph of y = x^3")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True)
    plt.legend()

    plt.tight_layout()
    plt.savefig("plots.png")
    plt.show()

if __name__ == "__main__":
    plot_functions()
# Modified programme.py
