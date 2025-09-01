function sum=cal2(p0jk,p1jk,ph,pj,pk)
sum=0;

for j=1:2
    for k=1:2
        sum=sum+p0jk(j,k)*log2(p0jk(j,k)/(ph(1)*pj(j)*pk(k)));
    end
end
for j=1:2
    for k=1:2
        sum=sum+p1jk(j,k)*log2(p1jk(j,k)/(ph(2)*pj(j)*pk(k)));
    end
end
end