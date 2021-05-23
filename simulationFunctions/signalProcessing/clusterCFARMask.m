function [ clusterPeaks ] = clusterCFARMask( spec, CFARmask )
%CLUSTERCFARMASK returns the peaks from the spectrum, which are in the
%CFAR-mask.
% - spec         := The range Spectrum after the FFT and sum over all Channels
% - CFARmask     := The binary output of the CFAR
% - clusterPeaks := The peaks bins representing the detected Targets

%calc
absSpec=abs(spec);
endInds=find([0,CFARmask]-[CFARmask,0]>0)-1;
startInds=find([CFARmask,0]-[0,CFARmask]>0);

clusterPeaks=zeros(1,numel(startInds));
numPeaks=0;
for actInd=1:numel(startInds)
    if startInds(actInd)==endInds(actInd)
        numPeaks=numPeaks+1;
        clusterPeaks(numPeaks)=(startInds(actInd));
    elseif startInds(actInd)+1==endInds(actInd)
        numPeaks=numPeaks+1;
        if absSpec(startInds(actInd))>absSpec(endInds(actInd))
            clusterPeaks(numPeaks)=(startInds(actInd));
        else
            clusterPeaks(numPeaks)=(endInds(actInd));
        end
    else
        actPeaks=peakseek(absSpec(startInds(actInd):endInds(actInd)));
%         [~,actPeaks]=findpeaks(absSpec(startInds(actInd):endInds(actInd)));
        actPeaks=actPeaks+startInds(actInd)-1;
        if absSpec(startInds(actInd))>absSpec(startInds(actInd)+1)
            actPeaks=[startInds(actInd) actPeaks];
        end
        if absSpec(endInds(actInd))>absSpec(endInds(actInd)-1)
            actPeaks=[actPeaks endInds(actInd)];
        end
        clusterPeaks(numPeaks+1:numPeaks+numel(actPeaks))=actPeaks(:);
        numPeaks=numPeaks+numel(actPeaks);
    end
end

end

function [locs, pks]=peakseek(x,minpeakdist,minpeakh)
% Alternative to the findpeaks function.  This thing runs much much faster.
% It really leaves findpeaks in the dust.  It also can handle ties between
% peaks.  Findpeaks just erases both in a tie.  Shame on findpeaks.
%
% x is a vector input (generally a timecourse)
% minpeakdist is the minimum desired distance between peaks (optional, defaults to 1)
% minpeakh is the minimum height of a peak (optional)
%
% (c) 2010
% Peter O'Connor
% peter<dot>ed<dot>oconnor .AT. gmail<dot>com

if size(x,2)==1, x=x'; end

% Find all maxima and ties
locs=find(x(2:end-1)>=x(1:end-2) & x(2:end-1)>=x(3:end))+1;

if nargin<2, minpeakdist=1; end % If no minpeakdist specified, default to 1.

if nargin>2 % If there's a minpeakheight
    locs(x(locs)<=minpeakh)=[];
end

if minpeakdist>1
    while 1

        del=diff(locs)<minpeakdist;

        if ~any(del), break; end

        pks=x(locs);

        [garb, mins]=min([pks(del) ; pks([false del])]); %#ok<ASGLU>

        deln=find(del);

        deln=[deln(mins==1) deln(mins==2)+1];

        locs(deln)=[];

    end
end

if nargout>1,
    pks=x(locs);
end


end