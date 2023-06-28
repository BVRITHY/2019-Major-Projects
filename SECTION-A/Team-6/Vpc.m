function Vpc = Vpc(c,U)

sum_fin = 0;
n = size(U,2);
for k=1:n,
    for i=1:c,
        sum_fin = sum_fin + (U(i,k)^2);
    end
end

Vpc = (1/n) * sum_fin;