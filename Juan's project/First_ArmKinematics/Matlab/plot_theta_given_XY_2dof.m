syms L_1 L_2 theta_1 theta_2 XE YE;

L1=228;
L2=136.5;

XE_RHS = L_1*cos(theta_1) + L_2*cos(theta_1+theta_2);
YE_RHS = L_1*sin(theta_1) + L_2*sin(theta_1+theta_2);

XE_MLF = matlabFunction(XE_RHS,'Vars',[L_1 L_2 theta_1 theta_2]);
YE_MLF = matlabFunction(YE_RHS,'Vars',[L_1 L_2 theta_1 theta_2]);

t1_degs_row = linspace(0,90,100);
t2_degs_row = linspace(-180,180,100);
[tt1_degs,tt2_degs] = meshgrid(t1_degs_row,t2_degs_row);
tt1_rads = deg2rad(tt1_degs);
tt2_rads = deg2rad(tt2_degs);

X_mat = XE_MLF(L1,L2,tt1_rads,tt2_rads);
Y_mat = YE_MLF(L1,L2,tt1_rads,tt2_rads);

plot_XY_given_theta_2dof(tt1_degs,tt2_degs,X_mat,Y_mat,(L1+L2));