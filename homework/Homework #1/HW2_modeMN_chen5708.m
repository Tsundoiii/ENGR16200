% Homework #1 Problem #2
% Description: Plate deflection summand function
% File: HW2_modeMN_chen5708.m
% Date: 17 January 2026
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
% This function calculates the summand of the formula
% used to determine maximum plate deflection.

% ---------------------------------------------------
%   Inputs
% ---------------------------------------------------

% ---------------------------------------------------
%   Computations
% ---------------------------------------------------

function summand = HW2_modeMN_chen5708(a, b, m, n)
    summand = sin(m * pi / 2) * sin(n * pi / 2) / (m * n) ...
    * (m ^ 2 / a ^ 2 + n ^ 2 / b ^ 2) ^ -2;
end

% ---------------------------------------------------
%   Outputs
% ---------------------------------------------------