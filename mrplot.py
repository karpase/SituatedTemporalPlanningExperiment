import pandas as pd
import seaborn as sns
df = pd.read_csv("mrplot.txt", sep=" ")
plot=sns.violinplot(x="tu", y="mr", data=df,linewidth=3)
plot.figure.savefig("mrplot.png")
