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
printf {i in 1..m, j in 1..n: x[i,j] == 1} "bus %i in slot %i\n", i, j;
printf "\n";

data;

param n := 4;
param m := 3;
param kd := 1;
param kp := 10;

param: d    p :=
  1   100   11
  2   0     4
  3   5     1;

end;
