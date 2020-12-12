import matplotlib.pyplot as plt
from helper_functions import *


def graph_distribution_f(min_x: float, max_x: float, step=0.001,
                         mode="view") -> None:
    # Initialization
    x, y = setup(min_x, max_x, step)

    # Piecewise function definition
    for index in range(len(x)):
        y[index] = distribution_f(x[index])

    # Generate graph
    fig, ax = plt.subplots()
    ax.plot(x, y, label="F(x)")

    # Add details to graph
    plt.xlim(min_x, max_x)
    ax.set(xlabel="x", ylabel="F(x)", title="Distribution function F(x)")
    ax.grid()
    ax.legend()

    # Process request
    if mode == "view":
        plt.show()
    elif mode == "save":
        fig.savefig("distribution_F.png")


def graph_density_f(min_x: float, max_x: float, step=0.001,
                    mode="view") -> None:
    # Initialization
    x, y = setup(min_x, max_x, step)

    # Piecewise function definition
    for index in range(len(x)):
        y[index] = density_f(x[index])

    # Generate graph
    fig, ax = plt.subplots()
    ax.plot(x, y, label="f(x)")

    # Add details to graph
    plt.xlim(min_x, max_x)
    ax.set(xlabel="x", ylabel="f(x)", title="Density function f(x)")
    ax.grid()
    ax.legend()

    # Process request
    if mode == "view":
        plt.show()
    elif mode == "save":
        fig.savefig("density_f.png")


def graph_max_greater_b(b: float, min_x: float, max_x: float, step=0.001,
                        mode="view") -> None:
    # Initialization
    x, y = setup(min_x, max_x, step)

    # Function definition
    for index in range(len(x)):
        y[index] = 1 - distribution_f(b)

    # Generate graph
    fig, ax = plt.subplots()
    ax.plot(x, y, label="P({max(B1, B2, B3) > b})")

    # Add details to graph
    plt.xlim(min_x, max_x)
    plt.ylim(0, 1)
    ax.set(xlabel="x", ylabel="P({max(B1, B2, B3) > b})", title="Probability largest B greater than b")
    ax.grid()
    ax.legend()

    # Process request
    if mode == "view":
        plt.show()
    elif mode == "save":
        fig.savefig("probability_max.png")


graph_max_greater_b(0.7, -0.5, 1.5)
