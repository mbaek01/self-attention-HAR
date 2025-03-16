import numpy as np
import math
import random

def rotation_matrix(axis, rad):
    if axis == 'x':
        rot_mat = np.aray([
            [1, 0, 0],
            [0, np.cos(rad), -np.sin(rad)],
            [0, np.sin(rad), np.cos(rad)]
        ])
    
    elif axis == 'y':
        rot_mat = np.array([
            [np.cos(rad), 0, np.sin(rad)],
            [0, 1, 0],
            [-np.sin(rad), 0, np.cos(rad)]
        ])

    elif axis == 'z':
        rot_mat = np.array([
            [np.cos(rad), -np.sin(rad), 0],
            [np.sin(rad), np.cos(rad), 0],
            [0, 0, 1]
        ])
    
    else: 
        raise ValueError("Invalid value: axis should be either x, y, or z")

    return rot_mat

def rotate_matrix(m):
    # Reshape n x m to n x m/3 x 3
    num_rows = m.shape[0]
    reshaped = m.reshape(num_rows, -1, 3)

    # Random Rotation 
    axes = ['x', 'y', 'z']

    random_axis_idx = random.choice([0, 1, 2])
    random_rad = random.uniform(0, 2 * math.pi)

    rot_mat = rotation_matrix(axes[random_axis_idx], random_rad)
    rotated = reshaped @ rot_mat

    # Reshape back 
    rotated_reshaped = rotated.reshape(num_rows, -1) 

    return rotated_reshaped