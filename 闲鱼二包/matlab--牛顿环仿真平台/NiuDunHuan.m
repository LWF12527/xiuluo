%ţ�ٻ��������
%����ʱ�䣺2020/9/21
%�����ˣ�����
%����������������������������������������������������
clear
rm = 2;                            %�����λ���߳���һ�루mm��
temp = linspace(-rm, rm, 5001);
[X, Y] = meshgrid(temp);           %�������ڻ��ƶ�άͼ��ľ���
R = 500;                           %ƽ͹͸���İ뾶��mm��
d = (X.^2 + Y.^2)./(2 * R);        %���������Ĥ���
Lambda = 700e-6;                   %����Ⲩ����mm��
Delte = 2*d/Lambda * 2*pi + pi;    %������λ��
I = 128*(cos(Delte/2)).^2;         %������Թ�ǿ
figure                             %��ͼ
image(I);
colormap gray
axis off
axis equal
title('ţ�ٻ�(Newton ring)','FontSize',12);