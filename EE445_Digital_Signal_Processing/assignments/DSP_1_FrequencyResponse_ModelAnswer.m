%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%
% DSP_1_FrequencyResponse_ModelAnswer.M
%
% Sample model answers for EE445 Laboratory Assignment No. 1.
%
% Frequency Response of Discrete Time Systems. 
%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
clear all
close all
clc
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% EXERCISE 1
%
% Frequency response of a digital filter.
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% set up numerator and denominator polynomials
num_poly = [1, 0.4];
den_poly = [1, -1.5*cos(pi/8), 0.96];

% define sampling frequency
fsamp = 12000;

% get the frequency response
N = 1024;

% calculate frequency response
[H, freq_axis] = freqz(num_poly, den_poly, N, fsamp);

% alternative method of defining frequency axis
%freq_axis = 0:(fsamp/2)/(N-1):fsamp/2;

% plot
figure(1);

Mag = abs(H);

plot(freq_axis/1e3, 20*log10(Mag));
grid on;
% plots should be properly annotated
xlabel('Frequency (kHz)');
ylabel('Magnitude Response (dB)');
title('Exercise 1 - Magnitude Response');

% calculate the pole locations - there are a couple of ways to do this, 
% here is one example

% use the zplane function to get the poles and zeros. 
figure(2);
[zeros, poles] = zplane(num_poly,den_poly);

% use the roots function to get the poles
poles = roots(den_poly);

% calculate the magnitude and phase of the poles
pole_mag = abs(poles);
pole_angle = angle(poles);

% calculate the centre frequency
f0_Hz = fsamp*pole_angle(1)/(2*pi);

% output results
fprintf("The locations of the poles in polar form:\n");
fprintf("Pole 1: magnitude = %f phase = %f\n",pole_mag(1),pole_angle(1));
fprintf("Pole 2: magnitude = %f phase = %f\n",pole_mag(2),pole_angle(2));
fprintf("Centre frequency: = %f\n",f0_Hz);


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% EXERCISE 2
%
% Second-order filter.
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% The first thing to note is that the transfer function of the 
% filter in question is of the following form:
%
% H(z) =      z^2
%        ----------------
%        z^2 + b1*z + b2
%
% Note the double zero at z = 0.
%
% Coefficient b1 = -2*r*cos(theta0), where
% theta0 is the pole frequency, and r is the pole radius.
% Coefficient b2 = r^2.

% some constants
fsamp = 16e3;
f0 = 3.4e3;
pole_rad = 0.96;

% calculate coefficients
theta0 = 2*pi*f0/fsamp;
b1 = -2*pole_rad*cos(theta0);
b2 = pole_rad^2;

% calculate frequency response
num_poly = 1;
den_poly = [1, b1, b2];
N = 2048;
H = freqz(num_poly, den_poly, N);
nsamp = 120;
hn = impz(num_poly, den_poly, nsamp);
% plot frequency response
figure(3);
freq_axis = 0:(fsamp/2)/(N-1):fsamp/2;
plot(freq_axis, 20*log10((abs(H))));
grid on;
% annotate ...
xlabel('Frequency (kHz)');
ylabel('Magnitude Response (dB)');
title('Exercise 2 - Magnitude Response');

% plot impulse response
figure(4);
time_axis = (0:nsamp-1)/fsamp;
plot(time_axis./1e-3, hn);
grid on;
% annotate ...
xlabel('Time (ms)');
ylabel('Impulse Response (arbitrary units)');
title('Exercise 2 - Impulse Response');

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% EXERCISE 3
%
% Different filter types.
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% For each of the difference equations, it will be necessary
% to determine the transfer function, and hence specify the 
% numerator and denominator polynomials (for use with "freqz"
% and "impz").

% (i) HIGH-PASS FILTER
num_poly = [0.16, -0.48, 0.48, -0.16];
den_poly = [1, 0.13, 0.52, 0.3];
H = freqz(num_poly, den_poly);
hn = impz(num_poly, den_poly);
figure(5);
subplot(2,1,1);
plot(20*log10(abs(H)));
grid on;
% annotate ...
title('Exercise 3(i) - Magnitude Response');
subplot(2,1,2);
plot(hn);
grid on;
% annotate ...
title('Impulse Response');

% (ii) BAND-PASS FILTER
% NB: Note the absence of an "x(n-1)" and a "y(n-1)" term!!
num_poly = [0.634, 0, -0.634];
den_poly = [1, 0, -0.268];
H = freqz(num_poly, den_poly);
hn = impz(num_poly, den_poly);
figure(6);
subplot(2,1,1);
plot(20*log10(abs(H)));
grid on;
% annotate ...
title('Exercise 3(ii) - Magnitude Response');
subplot(2,1,2);
plot(hn);
grid on;
% annotate ...
title('Impulse Response');

% (iii) NOTCH (or "BAND-STOP") FILTER
% NB: Note the absence of an "x(n-1)" and a "y(n-1)" term!!
num_poly = [0.634, 0, 0.634];
den_poly = [1, 0, 0.268];
H = freqz(num_poly, den_poly);
hn = impz(num_poly, den_poly);
figure(7);
subplot(2,1,1);
plot(20*log10(abs(H)));
grid on;
% annotate ...
title('Exercise 3(iii) - Magnitude Response');
subplot(2,1,2);
plot(hn);
grid on;
% annotate ...
title('Impulse Response');

% (iv) RESONATOR (or BAND-PASS) FILTER
num_poly = [0.634, -5, 10];
den_poly = [10, -5, 1];
H = freqz(num_poly, den_poly);
hn = impz(num_poly, den_poly);
figure(8);
subplot(2,1,1);
plot(20*log10(abs(H)));
grid on;
% annotate ...
title('Exercise 3(iv) - Magnitude Response');
subplot(2,1,2);
plot(hn);
grid on;
% annotate ...
title('Impulse Response');

