%
% EXERCISE_2_5.M
%

N = 100;

% define filter
b0 = 1;
b1 = 0.5;
a1 = 1;
a2 = -0.9;

% define the input
x = zeros(N,1);
x(1) = 1;

% define "filter memory"
% assume filter is causal (i.e. memory = 0 at the start)
xnm1 = 0;
ynm1 = 0;
ynm2 = 0;

% calculate the output
for n = 1:N,
    
    y(n) = b0*x(n) + b1*xnm1 + a1*ynm1 + a2*ynm2;
    
    % update filter memory
    % NB: COMMON MISTAKE IS TO FORGET THIS !!
    xnm1 = x(n);
    ynm2 = ynm1;
    ynm1 = y(n);
    
end;

% plot
%stem(y); grid on;
plot(y); grid on;
