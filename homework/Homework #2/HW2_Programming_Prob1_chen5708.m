% Homework #2 Problem #1
% Description: Smog check program
% File: HW2_Programming_Prob1_chen5708.m
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
% This program determines the result of a smog check for
% various cars that have been tested based on emissions
% limits input by the user.

clc
clear

% ---------------------------------------------------
%   Inputs
% ---------------------------------------------------

% Import data as tabke
data = readtable(input("Please enter the file name for the " + ...
    "smog check data: ", "s"));

maxNOX = input("Please enter the maximum NOX value (in PPM): ");
maxCO = input("Please enter the maximum CO value (in PPM): ");
maxHC = input("Please enter the maximum HC value (in PPM): ");
resultsFile = input("Please enter the file name for the " + ...
    "smog check results: ", "s");

% ---------------------------------------------------
%   Computations
% ---------------------------------------------------

% Return either the string "PASS!" or the amount that
% the car has failed the test by
function output = checkValue(value, maximum)
    if value > maximum
        output = num2str(value - maximum, "%1.3f");
    else
        output = "PASS!";
    end
end

% Apply above function to each value, one column at a time

data.NOX = arrayfun(@checkValue, data.NOX, ...
    repelem(maxNOX, length(data.NOX)).', "UniformOutput", false);

data.CO = arrayfun(@checkValue, data.CO, ...
    repelem(maxCO, length(data.CO)).', "UniformOutput", false);

data.HC = arrayfun(@checkValue, data.HC, ...
    repelem(maxHC, length(data.HC)).', "UniformOutput", false);

% Create new table with counts of how many times "PASS!"
% appears in each row, then merge it with the existing table
data = [data rowfun(@(a, nox, co, hc) (string(nox) == "PASS!") + ...
    (string(co) == "PASS!") + (string(hc) == "PASS!"), data, ...
    "OutputVariableNames", "NUM_PASSES")];

% ---------------------------------------------------
%   Outputs
% ---------------------------------------------------

writetable(data, resultsFile, "Delimiter", "\t")