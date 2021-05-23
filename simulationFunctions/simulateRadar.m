function [ radarSignal ]= simulateRadar(camera,matFileName,radarParameters,camPos,doPlot,frameNum)
% SIMULATERADAR: create the radar signal from the rendered Images 
% - camera          := The defined Scene Settings
% - matFileName     := Name of the .mat File that contains zImage and radarImage
% - radarParamters  := The deined Radar Modulation Parameter
% - camPos          := The Camera Position in each frame
% - frameNum        := The number of the current Frame
% - radarSignal     := The simulated Radar Signal
%                      - dim1: fastTime
%                      - dim2: slowTime
%                      - dim3: channels

%% load radar- and z-image
load(matFileName);
if frameNum==1
    v_c=zeros(3,1);
else 
    v_c=(camPos(frameNum,:)-camPos((frameNum-1),:)).'/camera.scale* camera.fps;
end

%% check data consistency
if size(zImage)~=size(radarImage)
    error('size(zImage)~=size(radarImage)');
elseif size(radarImage)~=size(radarParameters.antennaCharMask);
    error('size(radarImage)~=size(antennaCharMask)');
end

%% create amplitude image
antennaGain_roundTrip=radarParameters.antennaCharMask.^2;
radarMaskImage=radarImage.*antennaGain_roundTrip;

%% Radar simualtion
% precomputations

numAntenna=size(radarParameters.P,1);
t_fast=(0:radarParameters.Ns-1) * 1/radarParameters.f_s;
t_slow=(0:radarParameters.Np-1) * radarParameters.Tp;

rangePhaseRelation=(-1j*2*pi*2/radarParameters.c)*radarParameters.B/radarParameters.T*t_fast.';
%rangePhaseRelation=repmat(rangePhaseRelation,1,radarParameters.Np);%,numAntenna);
dopplerPhaseRelation=((-1j*2*pi*2)/radarParameters.c)*radarParameters.f_c*t_slow;
%dopplerPhaseRelation=repmat(dopplerPhaseRelation,radarParameters.Ns,1);%,numAntenna);
doaPhaseRelation_x=-1j*2*pi*radarParameters.P(:,1);
%doaPhaseRelation_x=permute(-1j*2*pi*radarParameters.P(:,1),[3,2,1]);
%doaPhaseRelation_x=repmat(doaPhaseRelation_x,radarParameters.Ns,radarParameters.Np,1);
doaPhaseRelation_y=-1j*2*pi*radarParameters.P(:,2);
%doaPhaseRelation_y=permute(-1j*2*pi*radarParameters.P(:,2),[3,2,1]);
%doaPhaseRelation_y=repmat(doaPhaseRelation_y,radarParameters.Ns,radarParameters.Np,1);
doaPhaseRelation_z=-1j*2*pi*radarParameters.P(:,3);
%doaPhaseRelation_z=permute(-1j*2*pi*radarParameters.P(:,3),[3,2,1]);
%doaPhaseRelation_z=repmat(doaPhaseRelation_z,radarParameters.Ns,radarParameters.Np,1);

focalLengthInPixel = camera.focalLen / camera.dimension_width * size(zImage,2);

%simulation loop over all pixel
if doPlot
    h=waitbar(0,'Calculate Radar Simulation');
end
radarSignal=zeros(radarParameters.Ns,radarParameters.Np,numAntenna);
for imRow=1:size(zImage,1)
    for imCol=1:size(zImage,2)
        actZ=zImage(imRow,imCol);
        if actZ < 10000
            
            A=radarMaskImage(imRow,imCol) / 256; % The Amplitude value of each pixel


            u = [imCol-size(zImage,2)/2;...
                size(zImage,1)/2-imRow;...
                focalLengthInPixel];
            u = u/norm(u);                 % electrical angle
            
            r = actZ/u(3);                 % range
            
            v_r = v_c.' * u;               % radial velocity
            
            pixelRadarSignal = A * exp(rangePhaseRelation * r)...
                *exp(dopplerPhaseRelation * v_r);
%                 doaPhaseRelation_x * u(1) + ...
%                 doaPhaseRelation_y * u(2) + ...
%                 doaPhaseRelation_z * u(3));
            phaseShiftAntenna = doaPhaseRelation_x*u(1) + ...
                                doaPhaseRelation_y*u(2) + ...
                                doaPhaseRelation_z*u(3);
            for antenne= 1:numAntenna
                radarSignal(:,:,antenne) = radarSignal(:,:,antenne) + ...
                    exp(phaseShiftAntenna(antenne))*pixelRadarSignal;
            end
            
%             radarSignal=radarSignal + pixelRadarSignal; 
        end
    end
    if doPlot
        waitbar(imRow/size(zImage,1))
    end
end
if doPlot
    close(h)
end

%normalize to Image size
numberOfPixels=size(zImage,1)*size(zImage,2);
radarSignal=radarSignal/ numberOfPixels;

%Add noise
noiseAmplLin=20*log(radarParameters.noiseAmplitude_dB/10)/log(10) / numberOfPixels;
radarSignal=radarSignal + randn(size(radarSignal))*noiseAmplLin + 1j*randn(size(radarSignal))*noiseAmplLin;

end
