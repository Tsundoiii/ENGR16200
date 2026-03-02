
% File: IncubatorCLResponse.m
% Date: 24 February 2019
% By: TMW

% Script for the incubator problem from Team Exercise 8.1.2
% Required inputs are the magnitude of the applied temperature change,
% the proportional gain of the controller, and the integral gain of
% the controller.
% Output is a plot of the closed loop response of the system

%---------------------------------------------------
%  Inputs
%---------------------------------------------------

deltaTappl = input('Enter the applied temperature change: ');
propGain = input('Enter the proportional gain: ');
intGain = input('Enter the integral gain: ');

%---------------------------------------------------
%  Computations
%---------------------------------------------------

% Calculate supplemental parameters

a = (1+propGain)/2;
omega2 = intGain - a^2;

% Check suitability of inputs
propCheck = (propGain > 0);
intCheck = (omega2 > 0);

if (propCheck & intCheck)

    % Calculate closed loop response    
    w = sqrt(omega2);
    c = (1-a)/w;
    t = 0:.05:6;
    clResponse = deltaTappl*(1 - exp(-a*t).*cos(w*t) - c*exp(-a*t).*sin(w*t));

%---------------------------------------------------
%  Outputs
%---------------------------------------------------
    
% Plot closed loop response versus time
    figure(1);
    plot(t,clResponse)
    xlabel('time (minutes)');
    ylabel('temperature change (degrees C)');
    title('Incubator Closed Loop Response')
else
    disp('Incorrect inputs. Please run again.')
end
