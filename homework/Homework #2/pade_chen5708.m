% Homework #2 Problem #2
% Description: Error function Padé approximant
% File: HW2_Programming_Prob2_chen5708.m
% Date: 24 January 2026
% By: Aurora Chen
% chen5708
% Section: 2
% Team: 27
% 
% ELECTRONIC SIGNATURE
% Aurora Chen
% 
% The electronic signature above indicates that the program
% submitted for evaluation is my individual work. I have
% a general understanding of all aspects of its development
% and execution.
% 
% This function returns the value of the Padé approxmant
% of the error function for a given order and array of
% values.

% ---------------------------------------------------
%   Inputs
% ---------------------------------------------------


% ---------------------------------------------------
%   Computations
% ---------------------------------------------------

function values = pade_chen5708(order, x)
    switch order
        case 1
            values = arrayfun(@(x) (2 / sqrt(pi)) * x, x);
        case 2
            values = arrayfun(@(x) (2 / sqrt(pi)) * ...
                x / (1 + x ^ 2 / 3), x);
        case 3
            values = arrayfun(@(x) (2 / sqrt(pi)) * ...
                (x - x ^ 3 / 30) / (1 + 3 * x ^ 2 / 10), x);
    end
end

% ---------------------------------------------------
%   Outputs
% ---------------------------------------------------

