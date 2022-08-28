# Mmq's Data Science Training
# Created at: 2022/6/27 23:46
import time
import sys

print('\t\t\t\t此程序可以查找一定范围内的水仙花数\t\t\t\t')
time.sleep(0.5)
lower=int(input('请输入查找下限：'))
upper=int(input('请输入查找上限：'))
if lower>=upper:
    print('输入错误')
    time.sleep(1)
    sys.exit(0)
else:
    answer=[]
    for num in range(lower,upper):
        lst=[]
        for i in str(num):
            lst.append(int(i))
        total_sum=0
        for k in lst:
            total_sum+=k**3
        if total_sum==num:
            answer.append(num)
        else:
            pass
    print(answer)
