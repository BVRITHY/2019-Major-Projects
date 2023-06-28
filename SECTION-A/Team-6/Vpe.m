function VpE = Vpe(c,U)

sum_fin = 0;
n = size(U,2);

for k=1:n,
    for i=1:c,
        sum_fin = sum_fin + U(i,k) * log(U(i,k));
    end
end

VpE = (-1/n) * sum_fin;