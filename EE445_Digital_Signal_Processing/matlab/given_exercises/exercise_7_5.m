%
% EXERCISE_7_5.M
%
% Window vs. Parks-McClellan.
%

N = 20;
Wn = 0.5;

% window method
b1 = fir1(N, Wn, rectwin(N+1));

% P-M
f = [0, 0.45, 0.55, 1];
a = [1, 1, 0, 0];
b2 = firpm(N, f, a);

% plot
figure(1);
freqz(b1);
figure(2);
freqz(b2);

