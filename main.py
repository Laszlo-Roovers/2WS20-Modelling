# Local imports
from graphs import *

# These specific function calls were used to generate the figures that are used
# in the report.
graph_density_f(-0.5, 1.5, mode="save")
graph_distribution_f(-0.5, 1.5, mode="save")
graph_max_greater_b(0, 1, mode="save")
graph_second_highest_bid(3, -0.5, 1.5, mode="save")
graph_second_highest_bid(4, -0.5, 1.5, mode="save")
graph_second_highest_bid(7, 0, 1, mode="save", multiple=True)

# Note: Running this file in its current state will save all the graphs that
# are generated above within this project's folder on your computer. If you
# do not want this and want to just view the images instead, replace all
# "save" arguments with "view".
