# Mmq's Data Science Training
# Created at: 2022/8/7 21:39

# 包是一个分层次的目录结构，把功能相近的模块放在一个包内
# 通常含有__init__.py文件的目录称为包，反之只称为一个目录
# 包的导入：import【包.模块】asXXX 或 from【包或模块】import【模块或变量】asXXX。
# 包的新建:python package

import mmq_package as mmq
import mmq_package.Module1 as m1
from mmq_package import Module2 as m2
print(m1.a,m2.b)
from mmq_package.Module2 import b
print(b)

# import mmq_