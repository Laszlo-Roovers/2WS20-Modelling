import matplotlib.pyplot as plt
from helper_functions import setup, distribution_f, density_f, second_highest_bid


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


def graph_max_greater_b(min_b: float, max_b: float, step=0.001,
                        mode="view") -> None:
    # Initialization
    b, y = setup(min_b, max_b, step)

    # Function definition
    for index in range(len(b)):
        y[index] = 1 - pow(distribution_f(b[index]), 3)

    # Generate graph
    fig, ax = plt.subplots()
    ax.plot(b, y, label="P({max(B1, B2, B3) > b})")

    # Add details to graph
    plt.xlim(0, 1)
    plt.ylim(0, 1)
    ax.set(xlabel="b", ylabel="P({max(B1, B2, B3) > b})", title="Probability largest B greater than b")
    ax.grid()
    ax.legend()

    # Process request
    if mode == "view":
        plt.show()
    elif mode == "save":
        fig.savefig("probability_max.png")


def graph_second_highest_bid(players: int, min_b: float, max_b: float,
                             step=0.001, mode="view", multiple=False) -> None:
    assert players > 2, "number of players must be greater than 2!"

    # Initialization
    x, y = setup(min_b, max_b, step)

    # Function definition & Generate graph
    if not multiple:
        for index in range(len(x)):
            y[index] = second_highest_bid(players, x[index])
        fig, ax = plt.subplots()
        ax.plot(x, y, label="P(R2 < b < R1)")
    else:
        fig, ax = plt.subplots()
        for player in range(3, players+1):
            for index in range(len(x)):
                y[index] = second_highest_bid(player, x[index])
            ax.plot(x, y, label="P(R2 < b < R1) " + str(player) + " players")

    # Add details to graph
    plt.xlim(min_b, max_b)
    plt.ylim(0, 1)
    ax.set(xlabel="b", ylabel="P(R2 < b < R1)", title="Probability second "
                                                      "highest bid various "
                                                      "amount of players")
    ax.grid()
    ax.legend()

    # Process request
    if mode == "view":
        plt.show()
    elif mode == "save":
        fig.savefig("second_highest_" + str(players) + ".png")


graph_second_highest_bid(7, 0, 1, mode="save", multiple=True)
