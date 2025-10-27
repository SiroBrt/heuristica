param n;        # number of slots
param m;        # number of buses
param kd;       # penalty per kilometer
param kp;       # penalty per passenger
param d{1..m};  # distances to workshop
param p{1..m};  # passengers per bus

var c;
var x{1..m,1..n}, binary;

minimize loss:
  sum{i in 1..m, j in 1..n} (kd*d[i]-kp*p[i])*x[i,j]+c;
subject to onebusperslot{j in 1..n}: sum{i in 1..m} x[i,j] <=1; 
subject to busin1slot{i in 1..m}: sum{j in 1..n} x[i,j] <=1;
subject to aux: sum{i in 1..m} kp*p[i] = c;

solve;

printf "\n\nSolution:\n";
printf "loss = %i, #variables = %i, #constraints = %i\n", loss, m*n, m+n+1;
printf {i in 1..m, j in 1..n: x[i,j] == 1} "bus %i in slot %i\n", i, j;
printf "all other buses are unassigned\n\n";

end;
