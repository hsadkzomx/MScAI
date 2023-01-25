%
% EXAMPLE_6_4.M
%
% Impulse Invariant Transformation.
%

% describe the analogue filter
nums = [0, 0, 2];
dens = [1, 4, 3];

% calculate highest pole frequency
fc = 2/(2*pi);

% scale factor for calculation of fs
scale_fac = 5;

fs = scale_fac * fc;

[numz, denz] = impinvar(nums, dens, fs);

% get the frequency response
% set up a frequency axis
N = 512;
df = (fs/2)/N;
freq = (0:N-1)*df;

omega = (2*pi)*freq;

Hs = freqs(nums, dens, omega);
Hz = freqz(numz, denz, N);

% plot
figure;
plot(freq, 20*log10(abs(Hs)));
hold on;
plot(freq, 20*log10(abs(Hz)), 'r');
grid on;
hold off;


fprintf('\n\nFinished ...\n');

