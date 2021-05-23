function [ ind_hat,a_hat ] = peakInterp( maxInd,data,isVel )
%PEAKINTERP Peak interpolation:
% 1. Zero padding with a factor of sizeNeighEvalInterv
% 2. Parabola interpolation around the maximum
% - maxInd   := Index of the Maximum bin
% - data     := The radarSignal
% - ind_hat  := The interpolated index
% - a_hat    := The amplitude of the interpolated index

%def
sizeNeighEvalInterv=3;  %eval 4 points (>3), enough for parable fit (requires 3 points)
        
%init
ind_hat=zeros(numel(maxInd),1);
a_hat=zeros(numel(maxInd),1);
%calc
if isVel
    zerosAppendedData=[data,zeros(size(data,1),size(data,2)*(sizeNeighEvalInterv-1),size(data,3))];
    spec_zp=fftshift(sum(sum(abs(fft(conj(zerosAppendedData),[],2)),1),3));
else
    zerosAppendedData=[data;zeros(size(data,1)*(sizeNeighEvalInterv-1),size(data,2),size(data,3))];
    spec_zp=sum(sum(abs(fft(zerosAppendedData,[],1)),2),3).';
end
N_p=numel(data);


for i=1:numel(maxInd)
    if maxInd(i)==1
        ind_hat(i)=1;
        a_hat(i)=spec_zp(1);
    elseif maxInd(i)==numel(data)
        ind_hat(i)=numel(data);
        a_hat(i)=spec_zp(end);
    else

        %% DFT approx
        realMaxInd=maxInd(i);
        fineSpace=(realMaxInd-2)*sizeNeighEvalInterv+1:realMaxInd*sizeNeighEvalInterv+1;
        fineSpec=spec_zp(fineSpace);
        [max_Amp,fineMaxInd]=max(fineSpec);
        maxIndFine=fineSpace(fineMaxInd);

        if maxIndFine>1&&maxIndFine<N_p*sizeNeighEvalInterv-1&&fineMaxInd>1&&fineMaxInd<numel(fineSpace)-1
            %% Parab approx
            parabPar=[1 -1 1;1 0 0;1 1 1]\(spec_zp([maxIndFine-1,maxIndFine,maxIndFine+1])');
            deltaFinePos=-parabPar(2)/(2*parabPar(3));
            max_Amp=[1,deltaFinePos,deltaFinePos^2]*parabPar;
        else
            deltaFinePos=0;
        end

        realmaxpos=(maxIndFine-1+deltaFinePos)/(sizeNeighEvalInterv)+1;
        ind_hat(i)=realmaxpos;
        a_hat(i)=max_Amp;
    end
end

end