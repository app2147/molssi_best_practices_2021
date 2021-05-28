"""
Unit and regression test for the molecool package.
"""

# Import package, test suite, and other packages as needed
import molecool
import molecool.molecule
import numpy as np
import pytest
import sys

def test_molecool_imported():
    """Sample test, will always pass so long as import statement worked"""
    assert "molecool" in sys.modules

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

    calculated_value = molecool.calculate_angle(r1,r2,r3,degrees=True)

    assert expected_value == calculated_value

def test_build_bond_list():
    coordinates = np.array([
        [1,1,1],
        [2.4,1,1],
        [-0.4,1,1],
        [1,1,2.4],
        [1,1,-0.4]])
    
    bonds = molecool.build_bond_list(coordinates)
    
    assert len(bonds) == 4

    for bond_length in bonds.values():
        assert bond_length == 1.4

def test_molecular_mass():
    symbols = ['C', 'H', 'H', 'H', 'H']
    
    calculated_mass = molecool.molecule.calculate_molecular_mass(symbols)
    
    actual_mass = 16.04
    
    assert pytest.approx(actual_mass, abs=1e-2) == calculated_mass

def test_center_of_mass():
    symbols = np.array(['C', 'H', 'H', 'H', 'H'])
    coordinates = np.array([[1,1,1], [2.4,1,1], [-0.4, 1, 1], [1, 1, 2.4], [1, 1, -0.4]])

    center_of_mass = molecool.molecule.calculate_center_of_mass(symbols, coordinates)

    expected_center = np.array([1,1,1])

    assert np.array_equal(center_of_mass, expected_center)