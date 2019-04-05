.. _release_notes:

Release Notes
*************

Development Branch
------------------
`Development Branch`_


Version 1.2.5
-------------
Mar. 21, 2019

- Renamed ``pMuTT.io_`` module to ``pMuTT.io``
- Renamed ``pMuTT.io_.jsonio`` module to ``pMuTT.io.json``
- Added preliminary IO support for MongoDB in module: ``pMuTT.io.db``
- Bug fixes for Chemkin IO behavior

Version 1.2.4
-------------
Mar. 11, 2019

- Hotfix to correct Chemkin IO behavior

Version 1.2.3
-------------
Feb. 25, 2019

- Added ``smiles`` attribute to :class:`~pMuTT.statmech.StatMech` and 
  :class:`~pMuTT.empirical.EmpiricalBase` classes
- Added functions to write Chemkin surf.inp, gas.inp, and EAs.inp files
- Added :class:`~pMuTT.mixture.cov.CovEffect` class to model coverage effects
  and integrated it with :class:`~pMuTT.statmech.StatMech` and 
  :class:`~pMuTT.empirical.EmpiricalBase` classes
- Added ``include_ZPE`` parameter to ``get_EoRT``, ``get_E``, ``get_delta_EoRT``
  and ``get_delta_E`` for the :class:`~pMuTT.statmech.StatMech` class and
  :class:`~pMuTT.reaction.Reaction` class to add zero-point energy in
  calculations
- Renamed private methods ``_get_delta_quantity`` and ``_get_state_quantity`` to
  public methods ``get_delta_quantity`` and ``get_state_quantity`` in
  :class:`~pMuTT.reaction.Reaction` class
- Added generic method ``get_quantity`` to :class:`~pMuTT.statmech.StatMech`
  class so any method can be evaluated. It takes the parameters ``raise_error``
  and ``raise_warning`` so the user has the ability to ignore modes if they do
  not have the desired properties
- Added ``plot_coordinate_diagram`` method to the 
  :class:`~pMuTT.reaction.Reactions` class to plot coordinate diagrams.
- Added ``get_EoRT`` and ``get_E`` methods to :class:`~pMuTT.statmech.StatMech`
  class to calculate electronic contribution to thermodynamic properties
- Added ``get_EoRT_state`` and ``get_delta_EoRT`` methods to 
  :class:`~pMuTT.reaction.Reaction` to calculate electronic contribution to
  reaction properties
- Added an optional parameter, ``activation``, to ``get_delta_X`` methods to 
  specify the difference between the reactants/products and the transition
  state. 
- Added ``pMuTT.constants.symmetry_dict`` to allow easy look up of common
  symmetry numbers
- Fixed bug where specie-specific arguments were not passed correctly for
  :class:`~pMuTT.reaction.Reaction` class

Version 1.2.2
-------------
Jan. 18, 2019

- Added option to extract imaginary frequencies from VASP's OUTCAR files
- Added support for imaginary frequencies for 
  :class:`~pMuTT.statmech.vib.HarmonicVib` and 
  :class:`~pMuTT.statmech.vib.QRRHOVib` classes
- Restructured :class:`~pMuTT.statmech.vib.HarmonicVib` and 
  :class:`~pMuTT.statmech.vib.QRRHOVib` classes to calculate vibrational 
  temperatures, scaled wavenumbers and scaled inertia when methods are called 
  (rather than at initialization) to prevent incorrect calculations due to 
  changes in the vibrational wavenumbers.
- Fixed unit test names
- Added ``get_species`` to :class:`~pMuTT.reaction.Reaction` and 
  :class:`~pMuTT.reaction.Reactions`
- Fixed bug related to :class:`~pMuTT.empirical.references.References` and 
  :class:`~pMuTT.empirical.references.Reference` objects not JSON-write 
  compatible.
- Fixed bug related to referencing in :class:`~pMuTT.empirical.shomate.Shomate`
  class

Version 1.2.1
-------------
Dec. 17, 2018

- Added ``vib_outcar`` special rule for :func:`~pMuTT.io.excel.read_excel` and
  :func:`~pMuTT.io.vasp.set_vib_wavenumbers_from_outcar` to get vibrational 
  frequencies directly from VASP's OUTCAR file.
- Added ``get_X`` methods to :class:`~pMuTT.empirical.nasa.Nasa`, 
  :class:`~pMuTT.empirical.shomate.Shomate`, :class:`~pMuTT.statmech.StatMech` 
  and :class:`~pMuTT.reaction.Reaction` to directly calculate thermodynamic 
  properties (such as H, S, F, G) with the appropriate units
- Changed symbol for Hemlholtz energy from A to F

Contributors
^^^^^^^^^^^^
- Himaghna Bhattacharjee (himaghna_)

Version 1.2.0
-------------
Dec. 12, 2018

- Restructured code to exclude ``model`` module

Version 1.1.3
-------------
Dec. 11, 2018

- Added :class:`~pMuTT.reaction.bep.BEP` class
- Restructured :class:`~pMuTT.reaction.Reaction` class so reaction states (i.e.
  reactants, products, transition states) can be calculated separately
- Updated :class:`~pMuTT.empirical.references.References` class to be able
  reference any attribute
- Added ``placeholder`` entry to :data:`~pMuTT.statmech.presets` dictionary to
  represent an empty species
- Added correction factor to calculate partition coefficient, q, in
  :class:`~pMuTT.statmech.elec.IdealElec` class

Version 1.1.2
-------------
Nov. 27, 2018

- Fixed bugs in :class:`~pMuTT.reaction.Reaction` class for calculating
  pre-exponential factors
- Added methods in :class:`~pMuTT.reaction.Reaction` class to calculate rate
  constants and activation energy (currently, this just calculates the 
  difference in enthalpy between the reactant/product and the transition state)
- Quality of life improvements such as allowing
  :class:`~pMuTT.reaction.Reaction` class inputs to be a single pMuTT object
  instead of expecting a list

Version 1.1.1
-------------
Nov. 7, 2018

- Fixed bugs in :class:`~pMuTT.empirical.shomate.Shomate` class for ``get_HoRT``
  and ``get_SoR`` where one temperature would return a 1x1 vector instead of a
  float
- Fixed bug in :class:`~pMuTT.empirical.zacros.Zacros` class where it expected
  vibrational energies instead of wavenumbers.

Version 1.1.0
-------------
Oct. 26, 2018

- Updated :class:`~pMuTT.reaction.Reaction` class to parse strings
- New :class:`~pMuTT.empirical.shomate.Shomate` class
- New equation of state classes: :class:`~pMuTT.eos.IdealGasEOS`,
  :class:`~pMuTT.eos.vanDerWaalsEOS`
- New :class:`~pMuTT.reaction.phasediagram.PhaseDiagram` class
- New :class:`~pMuTT.statmech.vib.EinsteinVib` class
- New :func:`~pMuTT.io.chemkin.read_reactions` function to read species and
  reactions from Chemkin surf.inp and gas.inp files

.. _`Development Branch`: https://github.com/VlachosGroup/pMuTT/commits/development
.. _himaghna: https://github.com/himaghna