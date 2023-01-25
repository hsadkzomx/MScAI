%
% EXERCISE_4_8.M
%

% some constants
f0 = 100;
fsamp = 10000;
A = 1;
nsamp = 1000;

% calculate the digital frequency
theta0 = 2*pi*f0/fsamp;

% calculate the coefficients
b1 = -2*cos(theta0);
b2 = 1;

% calculate initial conditions
% set initial conditions to calculate first output samples at n = 25;
ynm1 = A*cos(24*theta0);
ynm2 = A*cos(23*theta0);

% time axis
time = (25:nsamp+24);
y = zeros(nsamp, 1);

% main loop
for n = 1:nsamp,
    
    y(n) = -b1*ynm1 - b2*ynm2;
    
    % update memory
    ynm2 = ynm1;
    ynm1 = y(n);
    
end;

plot(y); grid on;
