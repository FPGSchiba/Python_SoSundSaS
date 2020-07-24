# version: 1.0
# Author: Jann Erhardt

import copy
import pyvirtualdisplay
import imageio
import base64
import IPython

from acme import environment_loop
from acme.tf import networks
from acme.adders import reverb as adders
from acme.agents.tf import actors as actors
from acme.datasets import reverb as datasets
from acme.wrappers import gym_wrapper
from acme import specs
from acme import wrappers
from acme.agents.tf import d4pg
from acme.agents import agent
from acme.tf import utils as tf2_utils
from acme.utils import loggers

import gym
import dm_env
import matplotlib.pyplot as plt
import numpy as np
import reverb
import sonnet as snt
import tensorflow as tfs

try:
  from dm_control import suite
except (ModuleNotFoundError, OSError):
  pass