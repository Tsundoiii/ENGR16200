% Homework #2 Problem #2
% Description: Error function plotter
% File: HW2_Prob2_chen5708.m
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
% This program plots the error function and the Padé
% approximation of the error function based on user input
% bounds and order of approximant to use.

clc
clear

% ---------------------------------------------------
%   Inputs
% ---------------------------------------------------

min = input("Enter the minimum value of x to be plotted: ");
max = input("Enter the maximum value of x to be plotted: ");
order = input("Enter the Pade' approximant order to use: ");

% ---------------------------------------------------
%   Computations
% ---------------------------------------------------

points = linspace(min, max, 20);

% ---------------------------------------------------
%   Outputs
% ---------------------------------------------------

plot(points, erf(points), "-ob")

hold on

plot(points, pade_chen5708(order, points), "-->r")
legend("erf(x)", "P[2, 2](x)", "Location", "northwest")

hold off

title("Comparison of f(x) = erf(x) and f(x) = P[k, k](x)")
xlabel("x")
ylabel("f(x)")