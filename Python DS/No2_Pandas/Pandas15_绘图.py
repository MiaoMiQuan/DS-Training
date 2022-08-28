# Mmq's Data Science Training
# Created at: 2022/8/28 16:19
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# data=pd.DataFrame(np.random.randn(20)*2,index=np.arange(20))
# data.plot()
# plt.show()

data=pd.DataFrame(np.random.randn(16).reshape(4,4),index=['day1','day2','day3','day4'],columns=['A','B','C','D'])
# fig,axes=plt.subplots(2,2)
# data.plot(ax=axes[0,0],kind='bar')
# data.plot(ax=axes[0,1])
# data.plot(ax=axes[1,0],kind='barh')
# data.plot(ax=axes[1,1],kind='bar')
# plt.show()
data.plot(kind='bar')
plt.show()
