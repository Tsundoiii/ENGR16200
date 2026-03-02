clc
clear

data = importdata("data_team27_19h24m34s_conv.csv");

time = data(:, 1);
a_x = data(:, 2);
a_y = data(:, 3);
a_z = data(:, 4);
a = sqrt(a_x .^ 2 + a_y .^ 2 + a_z .^ 2) - 1;
max_a = max(a);
avg_a = mean(a(29:60) * 9.81 + 9.81);

function value = f(t)
    if t < 2
        value = exp(t);
    elseif t > 4
        value = exp((10 - t) / 3);
    else
        value = 10;
    end
end

function value = score(t, a, c)
    value = round((12 / (c + 0.001)) * (f(t) ^ ((40 - a) / 10)));
end

fprintf("Maximum acceleration (g): %f\n", max_a * 9.81)
fprintf("Average acceleration (m/s^2): %f\n", avg_a)
fprintf("Score: %i\n", score(3.86, max_a * 9.81, 0.16))
plot(time, a)

title("Acceleration vs. time of Egg Descent System")
xlabel("Time (s)")
ylabel("Acceleration (g)");