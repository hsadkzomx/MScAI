%
% EXERCISE_4_2.M
%
% Exercise 4.2 from the Notes.
%

% first, specify the poles
proots = [0.7 + j*0.4, 0.7 - j*0.4];

% use the polar form to get the "reflected" pole
rp = abs(proots(1));
thetap = angle(proots(1));

rz = 1/rp;
zroots(1) = rz*exp(j*thetap);
zroots(2) = rz*exp(-j*thetap);

% convert the roots to denominator polynomials using the Matlab "poly" function
num_poly = poly(zroots);
den_poly = poly(proots);

% scale to get a DC gain of 1
gainDC = sum(num_poly)/sum(den_poly);
scalefac = 1/gainDC;
num_poly = scalefac * num_poly;

% get the pole-zero map and the frequency response
figure(1);
zplane(num_poly, den_poly);
grid on;

figure(2);
freqz(num_poly, den_poly);

figure(3);
grpdelay(num_poly, den_poly);

fprintf('\n\nFinished ...\n');

