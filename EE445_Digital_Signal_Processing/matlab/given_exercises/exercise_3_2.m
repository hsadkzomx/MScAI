%
% EXERCISE_3_2.M
%
% Frequency response of an IIR filter.
%

N = 1000;
% set up a frequency axis
delta_theta = 6*pi/(N-1);
theta = -3*pi:delta_theta:3*pi;

% specify the real and imaginary parts of the numerator
% and denominator of the FT
numr = 1 + 0.6.*cos(theta) - 0.1.*cos(2*theta);
numi = -0.6.*sin(theta) + 0.1.*sin(2*theta);

denr = 1 - 0.3.*cos(theta) + 0.3.*cos(2*theta);
deni = 0.3.*sin(theta) - 0.3.*sin(2*theta);

mag = sqrt(numr.^2 + numi.^2)./sqrt(denr.^2 + deni.^2);
phase = atan(numi./numr) - atan(deni./denr);

% plot
figure(1);
plot(theta, 20*log10(mag)); grid on;
figure(2);
plot(theta, phase); grid on;

fprintf('\n\n\nFinished ...\n');
