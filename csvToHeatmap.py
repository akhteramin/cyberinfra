import textwrap

import pandas as pd
import matplotlib.pyplot as plt
#

#
# plt.imshow(df,cmap='hot',interpolation='nearest')
#
# plt.show()


import seaborn as sns
sns.set()
path_to_csv= "./Experiment_Genre_Wise_Chart.csv"
df= pd.read_csv(path_to_csv)
print(df.head(3))
df1 = df[['Content', 'Genre', 'Score']]
print(df1.head())
result = pd.pivot_table(df, values='Score',
                     index=['Content'],
                     columns='Genre')
yticks = result.index
# keptticks = yticks[::int(len(yticks)/10)]
yticks = [textwrap.fill(y, 20) for y in yticks]

xticks = result.columns
xticks = [textwrap.fill(x, 15) for x in xticks]



annot_kws={'fontsize':10,
           'fontstyle':'oblique',
           'color':"white",
           'alpha':0.6,
           'verticalalignment':'center'}
ax=sns.heatmap(result, annot=True, fmt="g", annot_kws=annot_kws,linewidths=2, linecolor="k",yticklabels=yticks,xticklabels=xticks)

plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
         rotation_mode="anchor")
# plt.savefig("test.png",bbox_inches='tight')
#
# plt.margins(0,0)
# plt.savefig("myfig.pdf")
plt.show() # ta-da!
