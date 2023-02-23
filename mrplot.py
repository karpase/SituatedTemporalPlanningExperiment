import pandas as pd
import seaborn as sns
import matplotlib

matplotlib.use("pgf")
matplotlib.rcParams.update({
    "pgf.texsystem": "pdflatex",
    'font.family': 'serif',
    'text.usetex': True,
    'pgf.rcfonts': False,
})


df = pd.read_csv("mrplot.txt", sep=" ")
plot=sns.violinplot(x=df.tu, y=df.mr, data=df, cut=0, scale="width")
plot.set(
    xlabel="$t_u$",
    ylabel="Fraction of Time Spent on Metareasoning")
plot.figure.savefig("mrplot.pgf")

