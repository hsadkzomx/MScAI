%
% EXERCISE_7_1.M
%
% FIR filter design - playing with delays.
%

% cutoff
thetac = pi/3;
alpha = 4;

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% USE IIR FILTER CENTRED AT n = 0
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% specify a time axis
nn1 = -4:4;
% calculate the coefficients (remember that these are symmetrically
% arranged about n = 0)
hn1 = (1/3).*sin(nn1.*thetac)./(nn1.*thetac);
% take n = 0 into account
hn1(5) = (1/3);

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% USE FIR FILTER CENTRED AT n = 4
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
nn2 = 0:8;
hn2 = (1/3).*sin((nn2-alpha).*thetac)./((nn2-alpha).*thetac);
% take (n-4) = 0 into account
hn2(5) = (1/3);

figure(1);
stem(nn1, hn1);

figure(2);
stem(nn2, hn2);

