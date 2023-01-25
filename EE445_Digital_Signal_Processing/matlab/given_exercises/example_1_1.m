%
% EXAMPLE_1_1.M
%
% Example 1.1 from the DSP notes.
%

% some constants
fs = 8000;
fa = 1000;
%fa = 1100;
N = 100;
A = 1;

% generate a sinewave using Matlab's "vector handling"
x = sin(2.*pi.*(fa./fs).*(0:N-1));

% do this the "C way"
% for n = 0:N-1,
%     
%     x2(n+1) = sin(2*pi*(fa/fs).*n);
%     
% end;


% figure(2);
% stem((0:N-1), x);
% xlabel('Sample Index');
% ylabel('Amplitude');
% grid on;