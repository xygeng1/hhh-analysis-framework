import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_excel('plot_yield.xlsx', index_col=0)

plt.figure(figsize=(10, 8))
sns.heatmap(data, annot=True, cmap="YlGnBu")
plt.savefig('yield_plot.png')
# plt.show()