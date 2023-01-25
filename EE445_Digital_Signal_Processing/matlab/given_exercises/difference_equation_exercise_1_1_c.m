%
% Section1, Exercise 1.1(c)
%
% Implementation of digital filter difference equation.
%

% number of samples
N = 200;

% define filter coefficients
b0 = 1;
b1 = 0.6;
b2 = -0.1;
a1 = 0.3;
a2 = -0.3;


% define the input
% unit step
% x = ones(N,1);

% unit impulse
x = zeros(N,1);
x(1) = 1;

% define a vector for the output
y = zeros(N,1);

% define "filter memory"
% assume filter is causal (i.e. zero initial conditions so set "filter 
% memory" = 0 at the start)
xnm1 = 0;
xnm2 = 0;
ynm1 = 0;
ynm2 = 0;

% calculate the output
for n = 1:N,
    
    y(n) = b0*x(n) + b1*xnm1 + b2*xnm2 + a1*ynm1 + a2*ynm2;
    
    % update filter memory
    % NB: COMMON MISTAKE IS TO FORGET THIS !!
    % NM: do these "oldest first"
    xnm2 = xnm1;
    xnm1 = x(n);
    ynm2 = ynm1;
    ynm1 = y(n);
    
end;

% plot
%stem(y); grid on;
plot(y); grid on;

