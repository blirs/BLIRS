function [ radarParameters ] = defineRadar( camera )
%DEFINERADAR: Define the following Parameres for the Radar:
% - antenna_gain            := Antenna Gain Amplitude in the center of Image
% - antenna_three_dB_x      := The antenna beam width in x-direction
% - antenna_three_dB_y      := The antenna beam width in y-direction
% - f_c                     := The center frequency of the radar
% - B                       := The Bandwidth
% - T                       := The chirp duration
% - f_s                     := The sampling frequency
% - Tp                      := The Pule Repition Interval
% - Np                      := The Pulse number
% - Ns                      := The number of Samples per pulse
% - P                       := The antenna postion matrix in terms of wavelength 
% - noiseAmplitude_dB       := The amplitude of the noise in dB
% - antennaCharMask         := Mask for Amplitude Image representing the antenna gain / characteristic
% Antenna 
radarParameters.antenna_gain = 10^(23/10);
radarParameters.antenna_three_dB_x=11/360*2*pi; % 11deg beam width
radarParameters.antenna_three_dB_y=11/360*2*pi; % 11 deg beam width

% Modulation
radarParameters.f_c=94e9;       % Center Frequency, Hz
radarParameters.B=3e9;          % Bandwidth, Hz
radarParameters.T=25e-6;        % Chirp Duration, s

radarParameters.f_s=10e6;       % Sampling Frequency, Hz
radarParameters.Tp=200e-6;      % Pulse Repetition Interval
radarParameters.Np=160;         % Pulse Number
radarParameters.Ns=250;         % Number of Samples

% Antenna Positions in wavelengths(in terms of lambda), each row represent the separation
% of one element to all other elements
radarParameters.P=[0 0 0 ; 1/2 0 0 ; 0 1/2 0 ; 1/2 1/2 0];
radarParameters.numofAntenna = length(radarParameters.P); % Number of Antennas
radarParameters.c=299792458;    % light speed, m/s
radarParameters.noiseAmplitude_dB = 100; % The amplitude of the noise in dB

% Create the Antenna Mask 
radarParameters.antennaCharMask=createRadarMask(camera.radar_numPx_x,...
    camera.radar_numPx_y,radarParameters.antenna_gain,radarParameters.antenna_three_dB_x,...
    radarParameters.antenna_three_dB_y,camera.focalLen,camera.dimension_width);


end



function [ radarAmpMask ] = createRadarMask( numPx_x, numPx_y, antennaGain, ...
    three_dB_angle_az, three_dB_angle_el, cam_focal_len,camera_dimension_width)
%CREATERADARMASK: create the Mask for Amplitude Image representing the antenna gain / characteristic
% - numPx_x                := number of Image Pixel Cols
% - numPx_y                := number of Image Pixel Rows
% - antennaGain            := Antenna Gain Amplitude in the center of Image
% - three_dB_angle_az      := azimuth angle of -3dB for antenna Gain power
% - three_dB_angle_el      := elevation angle of -3dB for antenna Gain power
% - cam_focal_len          := focal length of camera view, in mm
% - camera_dimension_width := The width of the Camera in mm
% - radarAmpMask           := The Radar Amplitude Mask 

%% Def
cam_dimension_width= camera_dimension_width;   %mm
si=@(x)sin(x)./x;
radarChar=@(x)(si(x).^2);
si_three_dB=1.3916;         % x value, where si(x)==1/sqrt(2)

%% Calc
angle_of_view_x=2*atan(cam_dimension_width/(2*cam_focal_len));
angle_of_view_y=angle_of_view_x*numPx_y/numPx_x;

% three_dB_Px_x=three_dB_angle_az*numPx_x/angle_of_view_x;
% three_dB_Px_y=three_dB_angle_el*numPx_y/angle_of_view_y;
angX=linspace(-angle_of_view_x/2,angle_of_view_x/2,numPx_x);
angY=(linspace(-angle_of_view_y/2,angle_of_view_y/2,numPx_y))';

phi=sqrt(repmat((si_three_dB/three_dB_angle_az*angX).^2,numPx_y,1)+repmat((si_three_dB/three_dB_angle_el*angY).^2,1,numPx_x));

radarAmpMask=sqrt(antennaGain)*radarChar(phi);


end