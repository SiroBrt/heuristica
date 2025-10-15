param n;              # number of slots
param m;              # number of buses
param u;              # number of workshops
param c{1..m,1..m};   # passengers in bus i and j
param o{1..n,1..u};   # slot i open in workshop j

var aux;              # not a real variable, only to adjust passengerslost

var x{1..m,1..u,1..n}, binary;  # bus i assigned to workshop j at time k
var f{1..m,1..m,1..n}, binary;  # bus p and q are both assigned to time k

minimize passengerslost:
  (sum{p in 1..m, q in 1..m, slot in 1..n} (c[p,q]*f[p,q,slot]) - aux)/2;
subject to busassigned{bus in 1..m}: sum{workshop in 1..u, slot in 1..n} x[bus,workshop,slot]=1; 
subject to closedslot{workshop in 1..u, slot in 1..n}: sum{bus in 1..m} x[bus,workshop,slot]<=o[slot,workshop]; 
subject to conflict1{p in 1..m, q in 1..m, slot in 1..n}: sum{workshop in 1..u} (x[p,workshop,slot]+x[q,workshop,slot])<=1+f[p,q,slot]; 
subject to conflict2{p in 1..m, q in 1..m, slot in 1..n}: sum{workshop in 1..u} (x[p,workshop,slot]+x[q,workshop,slot])>=2*f[p,q,slot]; 
subject to aux1: aux = sum{i in 1..m}(c[i,i]);



solve;

printf "\n\nSolution:\n";
printf {i in 1..m, j in 1..u, k in 1..n: x[i,j, k] == 1} "bus %i in workshop %i at time %i\n", i, j,k;
printf "passengers lost = %i\n\n", passengerslost;




data;

end;
