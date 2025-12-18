import pandas as pd
import matplotlib.pyplot as plt

df_old = pd.read_csv("old.csv")
df_new = pd.read_csv("new.csv")

plt.scatter(x=df_new['size'], y=df_new['time'], label="constraint solver")
plt.legend(loc='best')
plt.semilogy()
plt.savefig("plot/new_all.png")
plt.close()

plt.scatter(x=df_old['size'], y=df_old['time'], label="old solver")
plt.legend(loc='best')
plt.semilogy()
plt.savefig("plot/old_all.png")
plt.close()

plt.scatter(x=df_old['size'] * df_old['solutionFound'], y=df_old['time'] * df_old['solutionFound'], label="old solver")
plt.legend(loc='best')
plt.semilogy()
plt.savefig("plot/old_filtered.png")
plt.close()

plt.scatter(x=df_new['size'] * df_new['solutionFound'], y=df_new['time'] * df_new['solutionFound'], label="constraint solver")
plt.legend(loc='best')
plt.semilogy()
plt.savefig("plot/new_filtered.png")
plt.close()

plt.scatter(x=df_new['size'], y=df_new['time'], label="constraint solver")
plt.scatter(x=df_old['size'], y=df_old['time'], label="old solver")
plt.legend(loc='best')
plt.semilogy()
plt.savefig("plot/all.png")
plt.close()

plt.scatter(x=df_new['size'] * df_new['solutionFound'], y=df_new['time'] * df_new['solutionFound'], label="constraint solver")
plt.scatter(x=df_old['size'] * df_old['solutionFound'], y=df_old['time'] * df_old['solutionFound'], label="old solver")
plt.legend(loc='best')
plt.semilogy()
plt.savefig("plot/all_filterd.png")
