%
% EXERCISE_4_4.M
%
% Using "roots" and "residuez" to do cascade and parallel implementaion of
% transfer functions.
%

% transfer function
b = [23 40 36 19];
a = [10 9 8 3];

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% CASCADE
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% get the roots of the numerator (zeros) and denominator (poles)
rnum = roots(b);
rden = roots(a);

% use the "poly" function to combine complex conjugate zeros and poles
% NB: watch which elements in "rnum" and "rden" are complex
num2 = poly(rnum(2:3));
den2 = poly(rden(1:2));

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% PARALLEL
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% use the "residuez" function here
[R,P,K] = residuez(b,a);

fprintf('\n\nFinished ..\n');
