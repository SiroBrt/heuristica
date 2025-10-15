param n;              # number of slots
param m;              # number of buses
param u;              # number of workshops
param c{1..m,1..m};   # passengers in bus i and j
param o{1..n,1..u};   # slot i open in workshop j

var x{1..m,1..u,1..n}, binary;  # bus i assigned to workshop j at time k
var f{1..m,1..m,1..n}, binary;  # bus p and q are both assigned to time k

minimize passengerslost:
  sum{p in 1..m, q in 1..m, k in 1..n} (c[p,q]*f[p,q,k]/2);
subject to busassigned{i in 1..m}: sum{j in 1..u, k in 1..n} x[i,j,k]=1; 
subject to closedslot{j in 1..n, k in 1..u}: sum{i in 1..m} x[i,j,k]<=o[j,k]; 
subject to conflict1{p in 1..m, q in 1..m, k in 1..n}: sum{j in 1..u} (x[p,j,k]+x[q,j,k])<=1+f[p,q,k]; 
subject to conflict2{p in 1..m, q in 1..m, k in 1..n}: sum{j in 1..u} (x[p,j,k]+x[q,j,k])>=2*f[p,q,k]; 



solve;

printf "\n\nSolution:\n";
printf {i in 1..m, j in 1..u, k in 1..n: x[i,j, k] == 1} "bus %i in workshop %i at time %i\n", i, j,k;
printf "passengers lost = %i\n\n", passengerslost - sum{i in 1..m}(c[i,i]);




data;

end;
