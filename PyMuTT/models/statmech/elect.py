# -*- coding: utf-8 -*-

import numpy as np
from PyMuTT import constants as c

class IdealElect:
    """Electronic modes using the ideal gas assumption.
    
    Attributes
    ----------
        potentialenergy : float, optional
            Potential energy in eV. Default is 0
        spin : float, optional
            Electron spin. Default is 0
    """

    def __init__(self, potentialenergy=0., spin=0.):
        self.potentialenergy = potentialenergy
        self.spin = spin
        self._degeneracy = 2. * self.spin + 1.

    def get_q(self, T):
        """Calculates the partition function

        Parameters
        ----------
            T : float
                Temperature in K
        Returns
        -------
            q_elect : float
                Electronic partition function
        """
        return self._degeneracy*np.exp(-self.get_UoRT(T=T))

    def get_CvoR(self):
        """Calculates the dimensionless heat capacity at constant volume

        Returns
        -------
            CvoR_elect : float
                Electronic dimensionless heat capacity at constant volume
        """
        return 0

    def get_CpoR(self):
        """Calculates the dimensionless heat capacity at constant pressure

        Returns
        -------
            CpoR_elect : float
                Electronic dimensionless heat capacity at constant pressure
        """
        return self.get_CvoR()
    
    def get_UoRT(self, T):
        """Calculates the imensionless internal energy

        Parameters
        ----------
            T : float
                Temperature in K

        Returns
        -------
            UoRT_elect : float
                Electronic dimensionless internal energy
        """
        return self.potentialenergy/c.kb('eV/K')/T

    def get_HoRT(self, T):
        """Calculates the dimensionless enthalpy

        Parameters
        ----------
            T : float
                Temperature in K

        Returns
        -------
            HoRT_elect : float
                Electronic dimensionless enthalpy
        """
        return self.get_UoRT(T=T)

    def get_SoR(self):
        """Calculates the dimensionless entropy

        Returns
        -------
            SoR_elect : float
                Electronic dimensionless entropy
        """
        return np.log(self._degeneracy)

    def get_AoRT(self, T):
        """Calculates the dimensionless Helmholtz energy

        Parameters
        ----------
            T : float
                Temperature in K

        Returns
        -------
            AoRT_elect : float
                Electronic dimensionless Helmholtz energy
        """
        return self.get_UoRT(T=T) - self.get_SoR()

    def get_GoRT(self, T):
        """Calculates the dimensionless Gibbs energy

        Parameters
        ----------
            T : float
                Temperature in K

        Returns
        -------
            GoRT_elect : float
                Electronic dimensionless Gibbs energy
        """
        return self.get_HoRT(T=T) - self.get_SoR()