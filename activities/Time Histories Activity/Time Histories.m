data = importdata("TimeHistories.txt").data;

t = data(:,1);
x = data(:,2);
y = data(:,3);
z = data(:,4);

loglog(t, x)
semilogy(t, y)
loglog(t, z)