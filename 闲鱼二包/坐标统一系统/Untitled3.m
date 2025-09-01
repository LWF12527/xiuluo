clc
clear
close all

load x.mat
load y.mat 

x=Rotor_Spd_rpm;
y=real(response_obj);
% figure
% for ii = 1:100
% plot(x(ii,:),y(ii,:),'-')
% hold on
% end

[m,n ]= size(x);
xx1=x(2);
for ii = 2:n
    if y(1,ii)>y(1,ii-1)&&y(1,ii)>y(1,ii+1)
        xx1=x(1,ii);
        ka1=ii;
        break
    end
end
xx2=x(end-1);
for ii = n-1:-1:1
    if y(1,ii)<y(1,ii-1)&&y(1,ii)<y(1,ii+1)
        xx2=x(1,ii);
        ka2=ii;
        break
    end
end

for jj = 2:1000
    xy1=x(jj,2);
    for ii = 2:n
        if y(jj,ii)>y(jj,ii-1)&&y(jj,ii)>y(jj,ii+1)
            xy1=x(jj,ii);
            id1=ii;
            break
            
        end
    end
    xy2=x(end-1);
    
    for ii = n-1:-1:1
        if y(jj,ii)<y(jj,ii-1)&&y(jj,ii)<y(jj,ii+1)
            xy2=x(jj,ii);
            id2 = ii;
            break
        end
    end
    xz = xy1:10:xy2;
    zz = xx1:10:xx2;
   [ xz1 ,ps]= mapminmax(xz,xx1,xx2);
   yz = interp1(xz1,y(jj,id1:id2),zz);
   ax = [-10000:10:0 10:10:xx1];
   ay = [y(jj,1)*ones(1,1001) y(jj,1:ka1)];
   ax1 = mapminmax('apply',ax,ps);
   ax2= 10:10:xx1;
   ay1 = interp1(ax1,ay,ax2);
   
   bx = [ xx2:10:50000];
   by = [y(jj,ka2:end) y(jj,end)*ones(1,1000) ];
  
   bx1 = mapminmax('apply',bx,ps);
   bx2 = xx2:10:40000;
   by1 = interp1(bx1,by,bx2);
   y(jj,:)=[ay1(1:end-1) yz by1(2:end)]; 
    
    
end
    

figure
for ii = 1:1000
plot(x(ii,:),y(ii,:),'-')
hold on
end










