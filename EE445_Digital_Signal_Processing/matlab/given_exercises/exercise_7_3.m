%
% EXERCISE_7_3.M
%
% Effect of windows.
%

% first, design a high pass filter
N = 6;
b1 = fir1(N, 0.5, 'high');

% try a longer window
b2 = fir1(2*N, 0.5, 'high');

% try a rectangular window
b3 = fir1(N, 0.5, 'high', rectwin(N+1));

% calculate the frequency responses
H1 = freqz(b1);
H2 = freqz(b2);
H3 = freqz(b3);

% plot
figure(1);
plot(abs(H1));
hold on;
plot(abs(H2), 'r');
plot(abs(H3), 'k');
hold off; grid on;

