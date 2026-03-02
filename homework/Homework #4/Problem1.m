clc
clear

function y = f(x)
    y = -5000 * x + 96000;
end

x = [12 13.5 15.2 17.4 18.8];
y = [40000 25000 16000 8000 6000];

h(1) = scatter(x, y, "DisplayName", "Collected Data");
hold on
grid on
h(2) = fplot(@f, [12 19], "DisplayName", "Model Equation");

title("Representation of Problem #1")
legend(h)
xlabel("Age of Concrete Deck (years)")
ylabel("Load Capacity (lbs)")