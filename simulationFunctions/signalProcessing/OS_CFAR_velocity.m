function [ CFAR_binaryMask ] = OS_CFAR_velocity( velData,numberGuardCells,numberTrainingCells,P_fa )
%OS_CFAR_VELOCITY for detecting radar targets after vel fft for a single
%row of data matrix (Rayleigh noise pdf)
% - velData             := velocity Spectrum after the FFT and sum over all Channels
% - numberGuardCells    := number of Guard Cells
% - numberTrainingCells := number of Training Cells
% - P_fa                := Proability of False Alert Rate
% - CFAR_binaryMAsk     := he binary CFAR Mask with the velocity bins with
% targets above the threshold


safetyFactor=2;   % non-Gaussianity

if size(velData,1)~=1 && size(velData,2)~=1 %data is 2D
    error('OS_CFAR_velocity: Data must be 1D (incoherent sum)')
end
velData=reshape(velData,1,[]);  % ensure row vector

% halfWindowLen=numberGuardCells+numberTrainingCells;
windowShifts=[(-(numberGuardCells+numberTrainingCells):-(numberGuardCells+1)) ,...
              ((numberGuardCells+1):(numberGuardCells+numberTrainingCells))];
          
for trainCellInd=numel(windowShifts):-1:1
    indMtx(trainCellInd,:)=circshift(1:numel(velData),windowShifts(trainCellInd),2);
end
trainingMtx=velData(indMtx);
% trainingVec=[zeros(1,halfWindowLen),velData,zeros(1,halfWindowLen)];
% trainingMtx=trainingVec(ones(numel(windowShifts),1),...
%     ((halfWindowLen-windowShifts.'):(halfWindowLen-windowShifts.'+numel(velData))

sigmaVec=median(trainingMtx,1)/sqrt(2*log(2));
thresholdVec=sqrt(-2*log(P_fa))*sigmaVec*safetyFactor;

CFAR_binaryMask=velData>thresholdVec;

end

