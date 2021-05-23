function [ camera ] = defineSimulationSettings(  )
%DEFINESIMULATIONSETTINGS: Define the follwing Camera and Scene Settings:
% - radar_numPx_x       := number of horizontal Pixels for the radar Image
% - radar_numPx_y       := number of vertical Pixels for the radar Image
% - ir_numPx_x          := number of horizontal Pixels for the infrared Image
% - ir_numPx_y          := number of vertical Pixels for the infrared Image
% - numofFrames         := The number of Frames to simulate 
% - fps                 := The frame Rate per Second
% - focalLen            := The Camera Focal Length in mm
% - dimension_width     := The width of the Camera
% - doSave              := Save the output file of the radar renderes in a .mat file


% Set the horizontal Number of Pixels for the radar Image
camera.radar_numPx_x = 1000;
% Set the vertical Number of Pixels for the radar Image
camera.radar_numPx_y = 1000;
% Set the horizontal Number of Pixels for the ir Image
camera.ir_numPx_x = 500;
% Set the vertical Number of Pixels for the ir Image
camera.ir_numPx_y = 500;
% Define the Number of Frames of the Simulation
camera.numofFrames = 2;
% Define the Frame Rate Per Second
camera.fps = 1;
%Define the scale from Blender units to meters
camera.scale = 10; % 10 BU (Blender Units) = 1 meters
% Define the focal length of the Camera
camera.focalLen = 16;    %mm
% Define the Width of the Camera
camera.dimension_width = 32;
% The output of the radar simulation is saved to a mat file with the
% name outputfile_radarx_out.mat x is the frame number
camera.doSave = true;
end

