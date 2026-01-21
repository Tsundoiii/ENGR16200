% Homework #1 Problem #2
% Description: Plate deflection calculator
% File: HW1_Programming_Prob2_chen5708.m
% Date: 18 January 2026
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
% This program calculates the plate deflection of a surface
% given the dimensions of the surface, deflection constant,
% and maximum summation limits.

clc
clear

% ---------------------------------------------------
%   Inputs
% ---------------------------------------------------

a = input("Enter the length a [meters]: ");
b = input("Enter the length b [meters]: ");
K = input("Enter the parameter K [meters^3]: ");
M_max = input("Enter M_max: ");
N_max = input("Enter N_max: ");

if a <= 0
    error("Error: a must be strictly positive")
elseif b <= 0
    error("Error: b must be strictly positive")
elseif K <= 0
    error("Error: K must be strictly positive")
end

% ---------------------------------------------------
%   Computations
% ---------------------------------------------------

function displacement = d_max(a, b, K, M_max, N_max)
    k = 16 * K / pi ^ 6;

    sum = 0;
    
    for m = 1:M_max
        for n = 1:N_max
            sum = sum + HW2_modeMN_chen5708(a, b, m, n);
        end
    end

    displacement = k * sum;
end

% ---------------------------------------------------
%   Outputs
% ---------------------------------------------------

fprintf("The maximum deflection of the plate is %.4f meters", ...
    d_max(a, b, K, M_max, N_max));