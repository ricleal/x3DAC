x3DAC
=====

New Python version of the 3DAC the software to correct single crystal data for absorption correction based on a three-dimensional model reconstruction from visual images.

**This work is based on the original publication of the same author:**

R. M. F. Leal, S. C. M. Teixeira, V. Rey, V. T. Forsyth and E. P. Mitchell, *Absorption correction based on a three-dimensional model reconstruction from visual images*, J. Appl. Cryst. (2008). **41**, 729-737

**Abstract:**

The results are presented of a feasibility study for the application of absorption corrections to macromolecular crystallographic X-ray diffraction data using a three-dimensional crystal model generated photographically. The model allows path lengths through the crystal, the solvent and the crystal mount system to be determined. The approach has been tested on the macromolecular crystallography beamline ID23-1 at the ESRF in Grenoble using a model insulin system with the standard mini diffractometer facilities, which incorporate high-quality camera systems for sample alignment. Data from the insulin crystal at low incident beam energy (6.0 keV or 2.1 Å) were recorded and processed using this approach. The resulting data are compared against those treated using an empirical method and show significant improvement. The methods described here are of general interest, particularly for long-wavelength X-ray work, and may also be applied to account for absorption effects in neutron crystallography.


TODO:
=====

Modules:
- Camera calibration
- Image processing (edge detection, segmentation)
- 3D reconstruction from silhouettes
- Iluminated Volume calculation (need beamsize)
- Beam paths calculation (need beam distribution)
- Transmission calculation from beam paths, volume and crystal contents
 