function sum=cal1(phk,ph,pk)
sum=0;
for h=1:2
    for k=1:2
        sum=sum+phk(h,k)*log2(phk(h,k)/(ph(h)*pk(k)));
    end
end
end