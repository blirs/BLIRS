function [ targetList ] = radarSignalProcessing( rawData,radarParameters )
%RADARSIGNALPROCESSING: Signal Processing of the Radar Signal to get the
%output as a dected target list with estimated range, velocity and DOA
% - radarData         := The radar simulated Signal
% - radarParameters   := The defined Radar Modulation Parameters 
% - targetList        := The detected Target List
%                        - col1: estimated range
%                        - col2: estimated velocity
%                        - col3: estimated azimuth
%                        - col4: estimated elevation
%% Defs
% CFAR Definition
numTrainingCells=10;
numGuardCells=2;
probabilityFalseAlarm=1e-5;


%% Window
windowData=repmat(blackmanharris(size(rawData,1)),1,...
    size(rawData,2),size(rawData,3));
radarData=rawData.*windowData;

%% 1D-fft range
% to detect targets in range direction

fft_range = sqrt(size(radarData,1))*fft(radarData,[],1);
rangeSpec = sum(abs(fft_range),2);

% sum of all range spectra of the antennas
rangeSpec_sum = sum(rangeSpec,3);

%% detect targets range
[ CFAR_binaryMask ] = OS_CFAR_range(rangeSpec_sum,numGuardCells,...
    numTrainingCells,probabilityFalseAlarm,radarParameters.Np);   % CFAR Mask to find bins with targets
[rangeSpecMaxPos]=clusterCFARMask(rangeSpec_sum,CFAR_binaryMask); % Clsutering the CFAR Mask 
[peakPos,~]=peakInterp(rangeSpecMaxPos,radarData,false);          % Interpolation to estimate the range
rangeDetections=(radarParameters.Ns-peakPos+1)*radarParameters.c/(2*radarParameters.B);  % convert to metric units
%% detect targets velocity
targetList=[];
for actRangeTarg=1:numel(rangeSpecMaxPos)
    actRangeBin=rangeSpecMaxPos(actRangeTarg);
    actVelSpec=(fftshift(fft(fft_range(actRangeBin,:,:),[],2)));
    actVelSpecSum=sum(abs(actVelSpec),3);                             
    CFAR_binaryMask=OS_CFAR_velocity(actVelSpecSum,numGuardCells,...
        numTrainingCells,probabilityFalseAlarm);                     % CFAR Mask to find bins with targets
    if any(CFAR_binaryMask)
        [velSpecMaxPos]=clusterCFARMask(actVelSpec,CFAR_binaryMask); % Clsutering the CFAR Mask 
        [peakPos,peakAmpl]=peakInterp(velSpecMaxPos,...              % Interpolation to estimate the velocity
            fft_range(actRangeBin,:,:),true);   
        velDetections=(radarParameters.Np/2-1-peakPos)*...
            radarParameters.c/(2*radarParameters.f_c*...
            radarParameters.Tp*radarParameters.Np);                   % convert to metric units
        %% angle estimation for each range-Doppler target
        angle=zeros(numel(peakPos),2);
        for actVelTarg=1:numel(velSpecMaxPos)
            actVelBin=velSpecMaxPos(actVelTarg);
            arrayResponse=squeeze(actVelSpec(1,actVelBin,:));
            
            angle(actVelTarg,:) = bartlett_angleEsti(arrayResponse,radarParameters);
        end
            
        
        actTargets=[repmat(rangeDetections(actRangeTarg),numel(velDetections),1),...
            velDetections,...
            peakAmpl,...
            angle];
    else
        actTargets=[];
    end
    targetList=[actTargets;targetList];
end

end

