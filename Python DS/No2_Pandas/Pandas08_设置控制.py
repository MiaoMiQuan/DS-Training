import pandas as pd

#设置控制
print(pd.get_option('display.max_rows'))
pd.set_option('display.max_rows',50)
print(pd.get_option('display.max_rows'))
print(pd.DataFrame([x for x in range(100)]))

print(pd.get_option('display.max_colwidth'))

print(pd.get_option('display.precision'))
pd.set_option('display.precision',2) #改小数位数
print(pd.DataFrame([1.11111111111]))
pd.set_option('display.precision',6)
print(pd.DataFrame([1.11111111111]))