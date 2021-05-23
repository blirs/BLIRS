function [ directories ] = defineDirectories(  )
% DEFINEDIRECTORIES: Define the paths for:
% - blendfilepath     := Blender File with the defined Scene
% - radarpythonfile   := Path for the python script 'simulate_radar.py'
% - outputfile_radar  := Path for the Folder 'Radar_Renders'
% - radarmatfiles     := Path for the Folder ' Exr_to_mat_files'
% - filename_radar    := name for the radar renders
% - Blender_path      := Path to open the Blender app from Terminal: for linux 'blender'
% - irpythonfile      := Path for the python script 'simulate_ir.py'
% - outputfile_ir     := Path for the Folder 'Infrared_Renders'
% - filename_ir       := name for the infrared renders
% - results           := Path for the Folder 'Simulation Results'


% Enter here the path for the blend File to Render
directories.blendfilepath = fullfile(pwd,'Blend_File', 'scene_ir.blend') ;

% Enter here the Path for the Python script simulate_radar.py to create the
% radar Renders
directories.radarpythonfile = fullfile(pwd, 'Python_Scripts','simulate_radar.py') ;

% Enter the Path for the python Script simulate_infrared.py to create the
% Infrared Renderes
directories.irpythonfile = fullfile(pwd, 'Python_Scripts','simulate_infrared.py') ;

% Enter here the output file Path to put the Radar Rendered:
% 'Radar_Renders'
directories.outputfile_radar = fullfile(pwd,'Radar_Renders',filesep) ;

% Enter here the output file Path to put the Infrared Renderes:
% 'Infrared_Renders'
directories.outputfile_ir = fullfile(pwd,'Infrared_Renders',filesep) ;

% Enter here the output file Path to put the Radar .mat
% Files: 'Exr_to_mat_files'
directories.radarmatfiles = fullfile(pwd,'Exr_to_mat_files') ;

% Define the Name for the Rendered outputs
directories.filename_radar = 'room_radar_test';

% Define the Name for the Rendered outputs
directories.filename_ir = 'room_ir_test';

%Path to open the Blender app from Terminal (for Linux 'blender' if blender
%is downloaded in the default path
directories.Blender_path = '.\blender-2.77-windows64\blender.exe';


% Enter the Path for the folder to save the Simulation results:
% 'simulationResuts'
directories.results = fullfile(pwd,'simulationResults');

end

