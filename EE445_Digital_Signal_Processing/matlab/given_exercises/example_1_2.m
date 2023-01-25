%
% EXAMPLE_1_2.M
%
% Example 1.2 from the DSP notes - AM waveform.
%

% Some constants
fs = 10e3;
fc = 1000;
fm = 80;
m = 1.5;
A = 1;
nsamp = 500;

% Calculate the digital frequencies
theta_m = 2*pi*fm/fs;
theta_c = 2*pi*fc/fs;

% Generate the AM waveform (“efficiently”)
sample_index = 0:nsamp-1;
x = A.*(1+m.*cos(sample_index.*theta_m)).*cos(sample_index.*theta_c);

% plot
figure(1);
plot(x);
grid on;
