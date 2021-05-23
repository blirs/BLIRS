clear variables
clc

addpath(genpath('simulationFunctions'));

%% Definitions
% The Scene and output files directories
directories = defineDirectories(); 
% The Camera and Simulation Settings
camera = defineSimulationSettings();
% The Radar Modulation Parameters
radarParameters = defineRadar(camera);

%% Create Blender Renders
% Radar
renderRadar(directories,camera);
% Infrared
renderIR(directories,camera);

%% Load Blender Renders and convert to matlab format
% convert exr files of Blender to mat files
hdrRenders2matlab(directories,camera);
% load the camera path
camPos=loadCameraPath(directories,camera);


%% Create the simulation output
% Infrared:
createVideo(directories,camera);
% Radar:
for i=1:camera.numofFrames
    fileName=[directories.radarmatfiles,directories.filename_radar,num2str(i)];
    radarData=simulateRadar(camera,fileName,radarParameters,camPos,1,i);
    targetList = radarSignalProcessing(radarData,radarParameters);
    save([directories.results,directories.filename_radar,num2str(i),'_out'],'radarData','targetList');
end
disp('Radar Simulation Finished')


