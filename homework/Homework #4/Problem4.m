clc
clear

x = [35 55 90 135 225];
y = [400 750 1270 2100 3330];

function y = f(x)
    y = 1.1429 * x + log(7.3798);
end

hold on
h(1) = scatter(log(x), log(y), "DisplayName", "Collected Data");
title("Representation of Problem #4")
xlabel("log Capacity (kg x 10^3)")
ylabel("log Cost (thousand USD)")
h(2) = fplot(@f, [3.5 6], "DisplayName", "Model Equation");
legend(h, "Location", "northwest")
grid on