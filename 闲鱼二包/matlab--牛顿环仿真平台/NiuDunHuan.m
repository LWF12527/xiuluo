%牛顿环干涉仿真
%仿真时间：2020/9/21
%制作人：陈岩
%——————————————————————————
clear
rm = 2;                            %正方形画面边长的一半（mm）
temp = linspace(-rm, rm, 5001);
[X, Y] = meshgrid(temp);           %创建用于绘制二维图像的矩阵
R = 500;                           %平凸透镜的半径（mm）
d = (X.^2 + Y.^2)./(2 * R);        %计算空气薄膜厚度
Lambda = 700e-6;                   %入射光波长（mm）
Delte = 2*d/Lambda * 2*pi + pi;    %计算相位差
I = 128*(cos(Delte/2)).^2;         %计算相对光强
figure                             %绘图
image(I);
colormap gray
axis off
axis equal
title('牛顿环(Newton ring)','FontSize',12);