"""Util Functions for Communication."""

import numpy as np

BOX_LOW = 0.0
BOW_HIGH = 1.0


def round_array_to_int(array):
    new_array = np.rint(array)
    # assert np.amax(new_array) == 1.0
    # assert np.amin(new_array) == 0.0
    return new_array

def mute_communications(comm_array):
    if comm_array[0] < 0.01:
        return np.zeros(comm_array.shape)
    else:
        return comm_array


def calculate_l2_distance(agent_1_pos, agent_2_pos):
    dist = np.linalg.norm(agent_2_pos - agent_1_pos)
    return dist


def apply_noise(array, noise_rate, distance):
    noise = np.random.normal(0.0, noise_rate * distance, size=array.size)
    return np.add(array, noise)

