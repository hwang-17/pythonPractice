import numpy as np
import pandas as pd
from matplotlib import pyplot as plt


datas = pd.read_csv("Datas/LC.csv")
values = datas.loc[:,["年龄", "历史逾期还款期数"]]
group = values.groupby("年龄").mean()['历史逾期还款期数']
plt.plot(group.index, group.values)
plt.show()