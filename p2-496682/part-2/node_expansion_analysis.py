import pandas as pd
import matplotlib.pyplot as plt

infile = "data/brute_FLA.csv"
df1 = pd.read_csv(infile)
infile = "data/brute_NY.csv"
df2 = pd.read_csv(infile)
df_brute = pd.concat([df1, df2])

infile = "data/heur_FLA.csv"
df1 = pd.read_csv(infile)
infile = "data/heur_NY.csv"
df2 = pd.read_csv(infile)
df_heur = pd.concat([df1, df2])

plt.scatter(x=df_brute['stepsToSolution'], y=(df_brute['nodesExpanded'] / df_brute['time']), label="brute")
plt.scatter(x=df_heur['stepsToSolution'], y=(df_heur['nodesExpanded'] / df_heur['time']), label="heur")
plt.xlabel('steps to solution')
plt.ylabel('nodes/sec')
plt.legend(loc='best')
plt.savefig("plot/plot_node_expansion.png")
