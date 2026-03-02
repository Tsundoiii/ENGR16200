clc
clear

x = linspace(225, 50, 8);
y = [0.760 0.771 0.760 0.775 0.790 0.794 0.808 0.800];

function y = msp(x)
    m = (0.77 - 0.81) / (175 - 50);
    y = m * x + 0.826;
end

function y = mls(x)
    y = -0.000277 * x + 0.8204;
end

h(1) = scatter(x, y, "DisplayName", "Collected Data");
hold on
grid on
h(2) = fplot(@msp, [50 250], "DisplayName", "Selected Points Equation");
h(3) = fplot(@mls, [50 250], "DisplayName", "Least Squares Equation");

title("Representation of Problem #2")
legend(h)
xlabel("Initial Height (cm)")
ylabel("Coefficient of Restitution")

hold off