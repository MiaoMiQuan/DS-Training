# Mmq's Data Science Training
# Created at: 2022/7/19 23:13

# 捕获的过程，先捕小错误，再捕大错误
try:  #可能出错的代码
    a=int(input('第一个整数'))
    b=int(input('第二个整数'))
    print(a/b)
except ZeroDivisionError:   #小错误放前面
    print('除数不能为0')
except ValueError:          #大错误放后面
    print('要输入数字')
except BaseException:       #其他所有错误都归在这里面
    print('其他错误')
else:                       #没错则跑这个
    print('没毛病')
finally:                    #无论有没有错都会跑这个
    print('结束了')