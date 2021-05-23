function [ cameraPosition ] = loadCameraPath( directories,camera )
% LOADCAMERAPATH: import the camera path from Blender to Matlab to
% calculate the velcoities for each frame
% - dirctories: The defined firectories for the scene and the output files
% - camera: The defined scene settings


%% Read the Camera posistion in each frame
camerapath = [directories.outputfile_radar,'Camerapath.py'];
fileID = fopen(camerapath);
path = textscan(fileID,'%s%s%s%s%s');
jj=1;
cameraPosition=zeros(camera.numofFrames,3);
for ii=1:length(path{1})
    
    if( strcmp((path{1}(ii)),'obj.location'))
       
       cameraPosition(jj,1)=str2double(path{3}(ii));
       cameraPosition(jj,2)=str2double(path{4}(ii));
       cameraPosition(jj,3)=str2double(path{5}(ii));
       jj=jj+1;
    end
end

if jj~=camera.numofFrames+1
    error('loadCameraPath: The number of frames in definition and Camerapath.py do not match')
end


end