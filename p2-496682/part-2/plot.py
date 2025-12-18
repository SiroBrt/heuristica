import sys
import pandas as pd
import matplotlib.pyplot as plt

if len(sys.argv) < 3:
    print("not enough arguments\n")
    exit(-1)
infile = sys.argv[1]
outfile = sys.argv[2]


df = pd.read_csv(infile)

df.plot(kind='scatter', x='stepsToSolution', y='time', label=infile)
plt.legend(loc='best')
# plt.loglog()
plt.savefig(outfile + "_time.png")

df.plot(kind='scatter', x='stepsToSolution', y='nodesExpanded', label=infile)
plt.legend(loc='best')
# plt.loglog()
plt.savefig(outfile + "_nodes.png")
