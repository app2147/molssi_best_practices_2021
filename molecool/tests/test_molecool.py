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

