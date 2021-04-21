%%Fuzzy logic

l1=10;
l2=7;

theta1 = 0:0.1:pi/2;
theta2 = 0:0.1:pi;

[THETA1,THETA2] = meshgrid(theta1,theta2);
X = l1 * cos(THETA1) + l2*cos(THETA1 + THETA2);
Y = l1 * sin(THETA1) + l2 * sin(THETA1 + THETA2);

data1 = [X(:) Y(:) THETA1(:)];
data2 = [X(:) Y(:) THETA2(:)];

plot(X(:),Y(:),'r.');
axis equal;
xlabel('X','fontsize',10);
ylabel('Y','fontsize',10);
