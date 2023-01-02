## Track Robot position using Bayes Filter
### Overview
This project implements a Bayes filter to track the position of a robot operating in a 2D grid world. The robot is equipped with a noisy odometer and a noisy color sensor. The grid world consists of cells that are characterized by a color (0 or 1). The color sensor reads the color of the cell correctly with probability 0.9 and incorrectly with probability 0.1.

At each step, the robot can take an action to move in one of four directions (north, east, south, west). However, the execution of these actions is noisy, so after the robot performs an action, it actually makes the move with probability 0.9 and stays at the same spot without moving with probability 0.1. If the robot is at the edge of the grid world and is tasked with executing an action that would take it outside the boundaries of the grid world, the robot remains in the same state with probability 1.

The filter begins with a uniform prior on all states, meaning that the probability of the robot being in any particular cell is initially equal. For example, if the grid world consists of 4 cells (x1, x2, x3, x4), the initial probability for each cell is P(X0 = xi) = 0.25.

Given a stream of actions and corresponding observations, the Bayes filter uses probabilistic techniques to estimate the robot's current position.
### Run the code
Simply run the ``
