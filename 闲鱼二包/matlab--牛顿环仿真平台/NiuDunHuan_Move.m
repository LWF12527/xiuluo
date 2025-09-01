%牛顿环干涉动图仿真
%仿真时间：2020/9/21
%制作人：陈岩
%REDME!!!该仿真模拟了牛顿环实验中平凸透镜被缓慢抬起时干涉图像的变化，按空格键仿真停止
%——————————————————————————
clear
rm = 2;                                 %正方形画面边长的一半（mm）
temp = linspace(-rm, rm, 301);
[X, Y] = meshgrid(temp);                %创建用于绘制二维图像的矩阵
R = 800;                                %平凸透镜的半径（mm）
Lambda = 700e-6;                        %入射光波长（mm）
flag = 1;
t = 0;

while flag
    input = get(gcf, 'currentkey');
    if strcmp(input, 'space');
        clc;
        flag = 0;
    end
    d = (X.^2 + Y.^2)./(2 * R) + t;     %计算空气薄膜厚度
    Delte = d/Lambda * 2*pi + pi;
    I = 128*(cos(Delte/2)).^2;            %计算相对光强
    image(I);
    colormap gray
    axis off
    axis equal
    title('牛顿环(Newton ring)','FontSize',12);
    pause(0.2);
    t = t+0.00003;
end



