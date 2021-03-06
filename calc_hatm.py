import numpy as np
import constants
import pdb, sys, os

"""
Routine for calculating atmospheric scale height of a planet.
"""

MUJUP = 2.22e-3 # Jupiter atmosphere mean molecular weight in kg mole^-1

def calc_hatm( z, mu=MUJUP ):
    """
    Input z is a dictionary containing the following:
    'mp' planet mass in kg
    'rp' planet radius in m
    'rs' stellar radius in m
    'a' semimajor axis in m
    'tstar' stellar effective temperature in K
    Input mu is a float specifying mean molecular weight
    of the atmosphere; default is that of Jupiter.
    """
    tpeq = calc_tpeq( z )
    little_g = constants.G*z['mp']/( ( z['rp']**2. ) )
    h = constants.RGAS*tpeq/mu/little_g
    print 'Tpeq={0}K, h={1}km'.format( tpeq, h/1000. )
    return h 

def calc_tpeq( z ):
    tpeq = np.sqrt( z['rs']/2./z['a'] )*z['tstar']
    return tpeq
