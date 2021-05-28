'''
Test for the measure module
'''

import molecool
import molecool.molecule
import numpy as np
import pytest
import sys

def test_calculate_distance():
    """Testing that calculate_distance calculates what we expect"""
    
    r1 = np.array([0,0,0])
    r2 = np.array([0,1,0])

    expected_distance = 1

    calculated_distance = molecool.calculate_distance(r1, r2)

    assert expected_distance == calculated_distance

def test_calculate_angle():
    r1 = np.array([0,0,-1])
    r2 = np.array([0,0,0])
    r3 = np.array([1,0,0])
    
    expected_value = 90

    calculated_value = molecool.calculate_angle(r1, r2, r3, degrees=True)

    assert expected_value == calculated_value

def test_calculate_angle_60():
    r1 = np.array([0,0,-1])
    r2 = np.array([0,1,0])
    r3 = np.array([1,0,0])
    
    expected_angle = 60

    calculated_angle = molecool.calculate_angle(r1, r2, r3, degrees=True)

    assert pytest.approx(expected_angle) == calculated_angle

def test_calculate_angle_many(r1, r2, r3, expected_angle):
    calculated_angle = molecool.calculate_angle(r1, r2, r3)
    assert pytest.approx(calculated_angle) == expected_angle