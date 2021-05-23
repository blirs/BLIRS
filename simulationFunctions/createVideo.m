function [  ] = createVideo( directories,camera )
% CREATEVIDEO: create the infrared video from the rendered Images and
% consider the temperature range of the infrared Camera
% The infrared video is saved in the Folder 'SimulationResults'
% - maxbright       := The maximum brightness in the image of the object with the
% maximum Temperatur( here 30 deg)
% - minbright       := The minimum brightness in the image of the object with the
% minumum Temperature (here 10 deg)
% - directories     := The defined directories for the scene and the output files
% - camera          := The defined Scene Settings


%% Definitions
maxbright = 0.3;  %Maximum Intensity for 30 degreed
minbright = 0.19; %Mimimum Instensity for 10 degrees

% create the video the output is located in the current path
% Infrared Renders
filename = directories.filename_ir;   % The name of the infrared Renderes
filepath = directories.outputfile_ir; % The path of the output folder 'Infrared_Renders'
resultspath = directories.results;    % the path of the results folder 'SimulationResults'


%% create the video
vw = VideoWriter([resultspath filename,'.avi'],'Uncompressed AVI');

vw.FrameRate= camera.fps;

open(vw)
for i=1:camera.numofFrames
    if i<10
        x='000';
    elseif i>=10 && i<100
        x='00';
    elseif  i>=100
        x='0';
    end

    im= hdrread([filepath,filename,x,num2str(i),'.hdr']);
    im = im(:,:,1);

    bright = (im-minbright).*((1/(maxbright-minbright))*256);
    bright(bright<0)=0;      % set min brightness for Pixels with brightness lower than that of 10deg 
    bright(bright>256)=256;  % set max brightness forPixels with brightness higher than that of 30deg
    imagebright = round(bright);
    
    writeVideo(vw,(imagebright/256));
end
close(vw)


disp('Infrared Simulation finished')


end

