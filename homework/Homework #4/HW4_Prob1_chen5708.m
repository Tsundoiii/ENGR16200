% Homework #4 Problem #1
% Description: Thermal image target isolator
% File: HW4_Prob1_chen5708.m
% Date: 7 February 2026
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
% This programs filters an input thermal image to only show
% the main target of the image.

clc
clear

% ---------------------------------------------------
%   Inputs
% ---------------------------------------------------

pic = imread(input("Please enter the file name for the image: ", "s"));

% ---------------------------------------------------
%   Computations
% ---------------------------------------------------

r = pic(:,:,1);
g = pic(:,:,2);
b = pic(:,:,3);

new_pic = rgb2gray(pic);

brightest = max(max(new_pic));
darkest = min(min(new_pic));

phi = zeros(size(new_pic));

% Threshold for keeping bright pixels
% 0.5 found to be good factor through empirical testing
mid =  0.5 * ((brightest - darkest) / 2 + darkest);

% Erode and dilate to only keep large regions
se = strel("disk", 5);
new_pic = imerode(new_pic, se);
new_pic = imdilate(new_pic, se);

phi(new_pic > mid) = 1;

% Change data type to make MATLAB happy
phi = cast(phi, "logical");

% Keep only the largest contiguous component to
% filter out random splotches
phi = bwareafilt(phi, 1);

r(phi == 0) = 0;
g(phi == 0) = 0;
b(phi == 0) = 0;

new_pic = cat(3, r, g, b);

% ---------------------------------------------------
%   Outputs
% ---------------------------------------------------

imshowpair(phi, new_pic, "montage")