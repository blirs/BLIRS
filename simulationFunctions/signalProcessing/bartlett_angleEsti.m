function [ angle ] = bartlett_angleEsti( arrayResponse,radarParameters )
%BARTLETT_ANGLEESTI: Calculate the Bartlett Spectrum as the Correlation of
%the phase shifted channels outputs and estimate the DOA by Maximizing the
%Bartlett Spectrum
% - arrayResponse   := 
% - radarParameters := The defines Radar Modulation Parameters
% - angle            := The estimated DOA
%      
%
%% angle estimation
az =0:(pi/100):(pi);
el =0:(pi/100):(pi);

for azcount =1:length(az)
  for elcount =1:length(el)
    % ideal angle vector
    u_ideal = [cos(az(azcount))*sin(el(elcount)) ;cos(el(elcount)); sin(el(elcount))*sin(az(azcount))];
    % ideal Signal
    X_ideal=exp(-1j*2*pi*radarParameters.P*u_ideal);
    % Bartlett Spectrum
    B(azcount,elcount)= ((abs(X_ideal'*arrayResponse)).^2);
  end
end
[~,maxInd]= max(abs(B(:)));
[az_ind,el_ind] = ind2sub(size(B),maxInd);

angle=[az(az_ind),el(el_ind)];

end

