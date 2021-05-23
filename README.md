Blender Infrared and Radar Simulator (BLIRS)
============================================

This is cloned from https://www.iss.uni-stuttgart.de/download/blender-radar/Simulation.zip and is based on the published work for this article:

Monika Ouza, Michael Ulrich and Bin Yang  
A Simple Radar Simulation Tool for 3D Objects based on Blender  
Proc. Intern. Radar Symposium (IRS), June 2017  
https://doi.org/10.23919/IRS.2017.8008254

Currently this works only with the outdated Blender version 2.77.

The aim of this repository is to port the code to current Blender versions.

Install instructions for Windows 10
===================================
- Download this repository as .zip file and extract it. Remember the folder you extracted it to. For example: Downloads\Blirs
- Download Blender 2.77 for Windows (64 bit) (blender-2.77-windows64.zip) from here:  
https://download.blender.org/release/Blender2.77/
- Extract blender into the \Blirs\ folder. Please take care not to double the directory names. The blender.exe should now be located : \Blirs\blender-2.77-windows64\
- Download the pre-compiled MEX files for Matlab from here:  https://github.com/edgarv/hdritools/releases/tag/0.5.0  
I used this file:  
HDRITools-0.5.0-20170712-win64-amd64.avx2-vc110
- Extract the HDRITools to \Blirs\
- Copy the folder Blirs\HDRITools-0.5.0-20170712-win64-amd64.avx2-vc110\matlab\ to \Blirs\ and then rename it to \Blirs\openexr-matlab-master
-  Start Blender 2.77 by launching \Blirs\blender-2.77-windows64\blender.exe
- In Blender go to File -> User Preferences...  
Go to the "Add-ons" tab and enable:  
Import-Export: Export Camera Animation  
by checking the checkbox on the left.
- In the same "Add-ons" tab click "Install from File...", then navigate to Blirs\Python_Scripts\  
and select "simulate_materials.py". Then click the "Install from File..." button.
- Make sure that the newly installed Add-on
  "Material: Materials Toolbox" is activated.
- Click "Save User Settings"
- Close the User Preferences dialog.
- Test if everything is wokring by pressing CTR+SHIFT+M.  
A new window "Material Toolbox" should pop-up that can be closed with ESC.
- Start Matlab and open Blirs\simulation_main.m
