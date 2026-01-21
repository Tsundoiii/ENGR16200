% Homework #1 Problem #1
% Description: Population calculator
% File: HW1_Programming_Prob1_chen5708.m
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
% This program calculates the current population given an
% initial population, growth rate, and time from a file.

clc
clear

% ---------------------------------------------------
%   Inputs
% ---------------------------------------------------

data = importdata("HW1_Prob1_Input.txt").data;

% ---------------------------------------------------
%   Computations
% ---------------------------------------------------

function population = P(p_0, r, t)
    population = round(p_0 * exp(r * t));
end

% ---------------------------------------------------
%   Outputs
% ---------------------------------------------------

fprintf("Case#\tCurrentPopulation\n")

% Loop through each row of data to calculate and display population
for row = 1:size(data, 1)
    caseNumber = data(row, 1);
    p_0 = data(row, 3);
    r = data(row, 2);
    t = data(row, 4);
    population = P(p_0, r, t);

    fprintf("%d\t%d\n", caseNumber, population)
end