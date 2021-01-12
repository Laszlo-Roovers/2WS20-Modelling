# Local imports
from graphs import *
import simulation
from helper_functions import reward_uniform, reward_kumaraswamy

# These specific function calls were used to generate the figures that are used
# in the report.

graph_density_f(-0.5, 1.5, mode="save")
graph_distribution_f(-0.5, 1.5, mode="save")
graph_max_greater_b(0, 1, mode="save")
graph_second_highest_bid(3, -0.5, 1.5, mode="save")
graph_second_highest_bid(4, -0.5, 1.5, mode="save")
graph_second_highest_bid(7, 0, 1, mode="save", multiple=True)
graph_density_kumaraswamy(0, 1, mode="save")

# Note: Running this file in its current state will save all the graphs that
# are generated above within this project's folder on your computer. If you
# do not want this and want to just view the images instead, replace all
# "save" arguments with "view".

# Simulation for 3 players, first model
simulation.Simulation(players=3, iterations=10000, mode="uniform",
                      mole=True).run()

# Simulation for actual WIDM-setting, with first model
simulation.Simulation(players=9, iterations=1000, mode="uniform",
                      mole=True).run()

# Simulation for 3 players, second model
simulation.Simulation(players=3, iterations=10000, mode="kumaraswamy",
                      mole=True).run()

# Simulation for actual WIDM-setting, with second model
simulation.Simulation(players=9, iterations=1000, mode="kumaraswamy",
                      mole=True).run()

# Reward calculations
# Does not work yet for uniform because values become negative!
# for entry in reward_uniform(players=9, value=0.5):
#     print(entry)

for entry in reward_kumaraswamy(players=9, value=0.5):
    print(entry)


