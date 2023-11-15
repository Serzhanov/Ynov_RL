
import numpy as np

from RL_classes.Bandit import Bandit
from RL_classes.BetaAlgo import BernThompson
from RL_classes.EpsilonGreedy import EpsilonGreedy
from RL_classes.Ucb import UCB


def simulate(arm_count,true_labels,simulations, timesteps, Algorithm):
  
  """ Simulates the algorithm over 'simulations' epochs """
  sum_regrets = np.zeros(timesteps)
  for e in range(simulations):
    bandit = Bandit(arm_count,true_labels)
    algo = Algorithm(bandit)
    regrets = np.zeros(timesteps)
    for i in range(timesteps):
      action = algo.get_action()
      reward, regret = algo.get_reward_regret(action)
      regrets[i] = regret
    sum_regrets += regrets  
  mean_regrets = sum_regrets / simulations
  return mean_regrets

def experiment(arms,true_labels,timesteps=10, simulations=10):
  """
  Standard setup across all experiments
  Args:
    timesteps: (int) how many steps for the algo to learn the bandit
    simulations: (int) number of epochs
  """
  algos = [EpsilonGreedy, UCB, BernThompson]
  regrets = []
  names = []

  for algo in algos:
    regrets.append(simulate(arm_count=arms,true_labels=true_labels,simulations=simulations, timesteps=timesteps, Algorithm=algo))
    names.append(algo.name())

  return regrets,names