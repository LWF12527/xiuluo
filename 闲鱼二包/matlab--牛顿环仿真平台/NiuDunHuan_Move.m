%ţ�ٻ����涯ͼ����
%����ʱ�䣺2020/9/21
%�����ˣ�����
%REDME!!!�÷���ģ����ţ�ٻ�ʵ����ƽ͹͸��������̧��ʱ����ͼ��ı仯�����ո������ֹͣ
%����������������������������������������������������
clear
rm = 2;                                 %�����λ���߳���һ�루mm��
temp = linspace(-rm, rm, 301);
[X, Y] = meshgrid(temp);                %�������ڻ��ƶ�άͼ��ľ���
R = 800;                                %ƽ͹͸���İ뾶��mm��
Lambda = 700e-6;                        %����Ⲩ����mm��
flag = 1;
t = 0;

while flag
    input = get(gcf, 'currentkey');
    if strcmp(input, 'space');
        clc;
        flag = 0;
    end
    d = (X.^2 + Y.^2)./(2 * R) + t;     %���������Ĥ���
    Delte = d/Lambda * 2*pi + pi;
    I = 128*(cos(Delte/2)).^2;            %������Թ�ǿ
    image(I);
    colormap gray
    axis off
    axis equal
    title('ţ�ٻ�(Newton ring)','FontSize',12);
    pause(0.2);
    t = t+0.00003;
end



