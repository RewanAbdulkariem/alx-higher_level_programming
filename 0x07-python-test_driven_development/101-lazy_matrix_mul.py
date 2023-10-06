#!/usr/bin/python3
"""
Module to multiply 2 matrices by using the module NumPy
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies two matrices using NumPy.
    """

    result = np.dot(m_a, m_b)
    return result
