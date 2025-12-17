import sys
import pandas as pd
import matplotlib.pyplot as plt

if len(sys.argv) < 4:
    print("not enough arguments\n")
    exit(-1)
infile1 = sys.argv[1]
infile2 = sys.argv[2]
outfile = sys.argv[3]


df1 = pd.read_csv(infile1)
df2 = pd.read_csv(infile2)

plt.scatter(x=df1['stepsToSolution'], y=df1['nodesExpanded'], label=infile1)
plt.scatter(x=df2['stepsToSolution'], y=df2['nodesExpanded'], label=infile2)
plt.xlabel('steps to solution')
plt.ylabel('nodes expanded')
plt.legend(loc='best')
plt.savefig(outfile + "_nodes.png")
plt.close()

plt.scatter(x=df1['stepsToSolution'], y=df1['time'], label=infile1)
plt.scatter(x=df2['stepsToSolution'], y=df2['time'], label=infile2)
plt.xlabel('steps to solution')
plt.ylabel('time')
plt.legend(loc='best')
plt.savefig(outfile + "_time.png")
