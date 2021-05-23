function [  ] = hdrRenders2matlab( directories,camera )
%HDRRENDERS2MATLAB: Converts the Radar Images from .exr to .mat format 
% the .mat files contain the Depth Image (z-Image) and the Amlitude Image
% (radar-Image). The .mat files are saved int the folder 'Exr_to_mat_files'
% - directories   := The defined paths for the scene and the output
% - camera        := The defined camera and scene settings


%% Defs
%File Defs
fileName =directories.filename_radar ;    % the name of the radar renders files 
filepath = directories.outputfile_radar ; % the path of the radar renders 'Rander_Renders'
outputpath = directories.radarmatfiles;   % the path of the output .mat files 'Exr_to_mat_files'
scale =camera.scale;                                 % 1Belnder Unit = 1m
fps = camera.fps ;
%Plot Defs
doPlot=false;

% add exrread to path
addpath('openexr-matlab-master')

for i=1:camera.numofFrames
if i<10
    x='000';
elseif i>=10 & i<100
    x='00';
elseif  i>=100
    x='0';
end
outFileName=[filepath,fileName,'_out',x,num2str(i),'.exr'];
zFileName=[filepath,fileName,'_z',x,num2str(i),'.exr'];


%load radar- and z-image
radarImage_full=exrread(outFileName);
radarImage=radarImage_full(:,:,1);

zImage_full=exrread(zFileName);
zImage=1/scale*zImage_full(:,:,1);

if size(zImage)~=size(radarImage)
    error('size(zImage)~=size(radarImage)');
end

if doPlot
    figure(1)
    imshow(radarImage);%tonemap(radarImage_full))
    figure(2)
    imshow(1/maxRange*scale*zImage)
end

save([outputpath,fileName,num2str(i)],'radarImage','zImage') % save the .mat file to the Folder 'Exr_to_mat_files'
end

disp('Packing exr files finished')

end

