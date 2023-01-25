%
% EXERCISE_4_1.M
%
% Exercise 4.1 from the Notes.
%

% first, specify the zeros and poles
zroots = [1.2 + j*0.7, 1.2 - j*0.7];
proots = [0.7 + j*0.4, 0.7 - j*0.4];

% convert the roots to numerator and denominator polynomials using the Matlab "poly" function
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

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% NOW, REFLECT THE ZEROS IN THE UNIT CIRCLE
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% use the polar form to get the "reflected" zero
rz = abs(zroots(1));
thetaz = angle(zroots(1));

rz2 = 1/rz;
zroots2(1) = rz2*exp(j*thetaz);
zroots2(2) = rz2*exp(-j*thetaz);

num_poly2 = poly(zroots2);

% scale to get a DC gain of 1
gainDC = sum(num_poly2)/sum(den_poly);
scalefac = 1/gainDC;
num_poly2 = scalefac * num_poly2;


% now, what does it look like?
% get the pole-zero map and the frequency response
figure(4);
zplane(num_poly2, den_poly);
grid on;

figure(5);
freqz(num_poly2, den_poly);

figure(6);
grpdelay(num_poly2, den_poly);


fprintf('\n\nFinished ...\n');

