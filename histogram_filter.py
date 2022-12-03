import numpy as np


class HistogramFilter(object):
    """
    Class HistogramFilter implements the Bayes Filter on a discretized grid space.
    """

    def histogram_filter(self, cmap, belief, action, observation):
        '''
        Takes in a prior belief distribution, a colormap, action, and observation, and returns the posterior
        belief distribution according to the Bayes Filter.
        :param cmap: The binary NxM colormap known to the robot.
        :param belief: An NxM numpy ndarray representing the prior belief.
        :param action: The action as a numpy ndarray. [(1, 0), (-1, 0), (0, 1), (0, -1)]
        :param observation: The observation from the color sensor. [0 or 1].
        :return: The posterior distribution.
        '''

        ### Your Algorithm goes Below.
        cmap = np.rot90(cmap, -1)
        belief = np.rot90(belief, -1)
        N = cmap.shape[0]
        M = cmap.shape[1]
        out = np.zeros((N, M))

        for i in range(N):
            for j in range(M):
                # cases: not out of boundaries
                if i + action[0] >= 0 and i + action[0] < N and j + action[1] >= 0 and j + action[1] < M:  # good case
                    out[i + action[0]][j + action[1]] += belief[i][j] * 0.9
                    out[i][j] += belief[i][j] * 0.1
                else:
                    out[i][j] += belief[i][j] * 1  # states remain unchanged

        sum = 0
        for i in range(N):
            for j in range(M):
                if cmap[i][j] == observation:
                    out[i][j] = 0.9 * out[i][j]
                    sum += out[i][j]
                else:
                    out[i][j] = 0.1 * out[i][j]
                    sum += out[i][j]
        out /= sum
        temp = 0
        tup = np.unravel_index(out.argmax(), out.shape)
        state = np.asarray(tup)
        belief = np.rot90(out, k=1)
        return belief
