p00jk=[0.0,0.0588;0,0];
p01jk=[0.0588,0.0588;0.0588,0.1569];
p10jk=[0.0196,0.1569;0.0392,0.0392];
p11jk=[0.0196,0.0392;0.2353,0.0588];
ph=[0.3921,0.6079];
pi=[0.3137,0.6863];
pj=[0.4117,0.5883];
pk=[0.4313,0.5689];
sum=0;
for j=1:2
    for k=1:2
        sum=sum+p00jk(j,k)*log2(p00jk(j,k)/(ph(1)*pi(1)*pj(j)*pk(k)));
    end
end
for j=1:2
    for k=1:2
        sum=sum+p01jk(j,k)*log2(p01jk(j,k)/(ph(1)*pi(2)*pj(j)*pk(k)));
    end
end
for j=1:2
    for k=1:2
        sum=sum+p10jk(j,k)*log2(p10jk(j,k)/(ph(2)*pi(1)*pj(j)*pk(k)));
    end
end
for j=1:2
    for k=1:2
        sum=sum+p11jk(j,k)*log2(p11jk(j,k)/(ph(2)*pi(2)*pj(j)*pk(k)));
    end
end
fprintf("T4=%f\n",sum);