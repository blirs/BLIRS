function [ CFAR_binaryMask ] = OS_CFAR_range( incoherentRangeData,numberGuardCells,numberTrainingCells,P_fa,N_p )
%OS_CFAR_RANGE: for detecting radar targets after range fft and incoherent
%integration (Gaussian noise pdf)
% - incoherentRangeData     := The range Spectrum after the FFT and sum 
% over all Channels
% - numberGuardCells        := The number of Guard Cells
% - numTrainingCells        := The number of Training Cells
% - P_fa                    := The Probaility of False Alert
% - N_p                     := The number of Range Bins
% - CFAR_binaryMask         := The binary CFAR Mask with the range bins with
% targets above the threshold

safetyFactor=1;   % non-Gaussianity

if size(incoherentRangeData,1)~=1 && size(incoherentRangeData,2)~=1 %data is 2D
    error('OS_CFAR_range: Data must be 1D (incoherent sum)')
end
incoherentRangeData=reshape(incoherentRangeData,1,[]);  % ensure row vector

windowShifts=[(-(numberGuardCells+numberTrainingCells):-(numberGuardCells+1)) ,...
              ((numberGuardCells+1):(numberGuardCells+numberTrainingCells))];

for trainCellInd=numel(windowShifts):-1:1
    indMtx(trainCellInd,:)=circshift(1:numel(incoherentRangeData),windowShifts(trainCellInd),2);
end
trainingMtx=incoherentRangeData(indMtx);

% estimated noise variance
sigmaVec=median(trainingMtx,1)/sqrt(pi/2)/N_p;  
% calculated threshold for given false alarm probability
thresholdVec=sqrt((4-pi)*N_p)*(sqrt(N_p*pi/2/(4-pi))+erfcinv(2*P_fa))*sigmaVec*safetyFactor; 

CFAR_binaryMask=incoherentRangeData>thresholdVec;

end

