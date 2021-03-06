function [ ] = renderRadar( directories,camera )
%RENDERRADAR: Creates the radar Renders from Blender using the python
%Script 'simulate_radar.py' located in the folder 'Python_Scripts' The
%rendered data are saved to the folder 'Radar_Renders'
% - directories   := The defined paths for the scene and the output
% - camera        := The defined camera and scene settings



q=char(39); % Character '

% read the python script
contents  = fileread(directories.radarpythonfile);

%escape backslash
pythonFileSep = '/';
blendfilepath_escaped =  strrep(directories.blendfilepath, filesep(), pythonFileSep);
outputfile_radar_escaped = strrep(directories.outputfile_radar, filesep(), pythonFileSep);
filename_radar_escaped = strrep(directories.filename_radar, filesep(), pythonFileSep);


% change the parameters in the python script
newcontents = regexprep(contents, {'^blendfilepath\S* = \S*',...
    '^camerafocallen\S* = \S*\d+', '^camerawidth\S* = \S*\d+', ...
    '^radar_resolution_x\S* = \S*\d+', '^radar_resolution_y\S* = \S*\d+',...
    '^outputfile\S* = \S*','^filename\S* = \S*','^numofFrames\S* = \S*\d+',...
    '^fps\S* = \S*\d+'}, ...
    {sprintf('blendfilepath = %s', [q,blendfilepath_escaped,q]), ...
    sprintf('camerafocallen = %d', camera.focalLen),...
    sprintf('camerawidth = %d',camera.dimension_width),...
    sprintf('radar_resolution_x = %d', camera.radar_numPx_x),...
    sprintf('radar_resolution_y = %d', camera.radar_numPx_y),...
    sprintf('outputfile = %s', [q,outputfile_radar_escaped,q]), ...
    sprintf('filename = %s', [q,filename_radar_escaped,q]),...
    sprintf('numofFrames = %d',camera.numofFrames),...
    sprintf('fps = %d',camera.fps)},'lineanchors');
fid = fopen(directories.radarpythonfile,'w');
fwrite(fid, newcontents);
fclose(fid);
% Render the Radar Animation
Command = [directories.Blender_path,' ','--background',' ','--python',' ',directories.radarpythonfile];
system(Command);
disp('radar rendering finished')

end

