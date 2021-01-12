import random
from kumaraswamy import kumaraswamy

class Simulation:
    def __init__(self, players, iterations, mode, mole):
        assert players >= 3, "At least 3 players needed."
        # This is the total amount n of opponents, of which n-2 play without
        # strategy, one is the mole, and the smart players.
        self.players = players
        self.iterations = iterations
        self.mode = mode
        self.mole = mole

    def get_specs(self):
        print("This simulation considers a setting with " + str(self.players) +
              " players and iterates a total of " + str(self.iterations) +
              " times.")

    def run(self):
        print("Starting simulation...")
        successes = 0
        failures = 0
        for _ in range(self.iterations):
            # Everybody except mole has no strategy now
            strategyless_opponents = 0
            if self.mole:
                bids = [1]
                strategyless_opponents = self.players - 2
            else:
                bids = []
                strategyless_opponents = self.players - 1

            # First model
            if self.mode == "uniform":
                for opponent in range(strategyless_opponents):
                    bids.append(random.uniform(0, 1))

            # Second model
            if self.mode == "kumaraswamy":
                dist = kumaraswamy(2, 5)
                sample = dist.rvs(strategyless_opponents)
                if self.players > 3:
                    for entry in sample:
                        bids.append(entry)
                elif self.players == 3:
                    bids.append(sample)

            # Choose optimal bid, according to formula in report
            bid = 0
            if self.mode == "uniform":
                bid = float((self.players - 1) / self.players)
                # bid = 4.0/9.0
            else:
                # Hard-coded for the case with 9 other players
                bid = 0.4528

            # Check if the bid is indeed the second highest
            bids.sort()
            if bids[-2] < bid < bids[-1]:
                successes += 1
            else:
                failures += 1

        print("Simulation finished")
        print("Results\n-----------------------------------------------------")
        print("Bid: " + str(bid))
        print("Successes: " + str(successes))
        print("Failures: " + str(failures))
        print("Total runs: " + str(self.iterations))
        print("Success Ratio: " + str(successes / self.iterations))


