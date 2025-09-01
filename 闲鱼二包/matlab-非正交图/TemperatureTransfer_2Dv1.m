% 设定参数
L = 1; % 区域边界
mu = 1; % 热扩散系数
N = 100; % 网格数
dx = 2*L/(N-1); % 网格步长
dy = dx;
x = linspace(-L,L,N); % 网格节点
y = linspace(-L,L,N);
dt = 0.01; % 时间步长
t = 0:dt:1; % 时间节点
T = zeros(N,N,length(t)); % 温度场

% 初始条件
A = 1;
a = 1;
for i = 1:N
    for j = 1:N
        T(i,j,1) = A*exp(-a*(x(i)^2+y(j)^2));
    end
end

% 边界条件
T(:,1,:) = 0;
T(:,end,:) = 0;
T(1,:,:) = 0;
T(end,:,:) = 0;

% 求解差分方程
for k = 2:length(t)
    for i = 2:N-1
        for j = 2:N-1
            T(i,j,k) = T(i,j,k-1) + mu*dt*( (T(i+1,j,k-1)-2*T(i,j,k-1)+T(i-1,j,k-1))/dx^2 + (T(i,j+1,k-1)-2*T(i,j,k-1)+T(i,j-1,k-1))/dy^2 );
        end
    end
end

% 绘制温度分布图像
[k1 k2 k3]=size(T);
[X,Y] = meshgrid(x,y);
% figure(1)
% surf(X,Y,T(:,:,10),'EdgeColor','none');
% xlabel('x');
% ylabel('y');
% zlabel('T(x,y)');
% title('Temperature Distribution');
for k=1:k3
figure(k);
%surf(X,Y,T(:,:,k),'EdgeColor','none');
gca=pcolor(X,Y,T(:,:,k));
colorbar;
axis tight;
set(gca, 'LineStyle','none');
xlabel('x');
ylabel('y');
zlabel('T(x,y)');
title(strcat(['Temperature Distribution with t=',num2str((k-1)*dt,'%.3f')]));
pause(15)
close(k)
end

% T_xy_t = squeeze(T(:,N/2,:));
% [X,Y] = meshgrid(x,y);
% surf(X,Y,T_xy_t,'EdgeColor','none');
% xlabel('x');
% ylabel('t');
% zlabel('T');
% title('Temperature Distribution');
