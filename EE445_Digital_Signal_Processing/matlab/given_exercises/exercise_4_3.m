%
% EXERCISE_4_3.M
%
% Exercise 4.3 from the Notes.
%

% first, specify the zeros
zroots = [1.2 + j*0.7, 1.2 - j*0.7];

% use the polar form to get the "reflected" zeros
rz = abs(zroots(1));
thetaz = angle(zroots(1));

rz2 = 1/rz;
zroots2(1) = rz2*exp(j*thetaz);
zroots2(2) = rz2*exp(-j*thetaz);

% combine the two pairs of zeros to get a single vector
zroots3 = [zroots, zroots2];

% convert the roots to a polynomial
num_poly = poly(zroots3);
den_poly = 1;

% scale to get a DC gain of 1
%gainDC = sum(num_poly)/sum(den_poly);
%scalefac = 1/gainDC;
%num_poly = scalefac * num_poly;

% get the pole-zero map and the frequency response
figure(1);
zplane(num_poly, den_poly);
grid on;

figure(2);
freqz(num_poly, den_poly);

figure(3);
grpdelay(num_poly, den_poly);

fprintf('\n\nFinished ...\n');

