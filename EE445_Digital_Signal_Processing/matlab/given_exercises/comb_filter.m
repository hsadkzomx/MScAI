%
% COMB_FILTER.M
%
% Characteristics of comb filter.
%

N = 8;

% specify the coefficients
b = [1, zeros(1,N-1), -1];

% frequency response
H = freqz(b, 1, 1000, 'whole');

figure(1);
plot(abs(H)); grid on;

figure(2);
zplane(b,1);

figure(3);
impz(b,1);
