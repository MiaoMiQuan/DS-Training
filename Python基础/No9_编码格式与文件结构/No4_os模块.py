# Mmq's Data Science Training
# Created at: 2022/8/10 22:04
import  os
# os模块通常与操作系统有关，os、os.path通常对目录或文件进行操作

# 打开文件、模块
# os.system('notepad.exe')
# os.system('calc.exe')

# 调用可执行文件
# os.startfile('D:\\开黑啦\\KaiHeiLa\\KOOK.exe')

# os模块其他功能
# print(os.getcwd())  #给出当前目录
# print(os.listdir(os.getcwd()))  #输出地址内全部文件
# print(os.listdir('../'))   # /表示根目录    ./表示当前目录    ../表示上一层目录
# os.mkdir('make_dir_test') #创建目录
# os.makedirs('make_dir_test/sub_dir_lv1/sub_dir_lv2') #创建多级目录
# os.rmdir('make_dir_test/sub_dir_lv1/sub_dir_lv2') #删除目录
# os.removedirs('make_dir_test/sub_dir_lv1') #删除多级目录
# os.chdir('D:\\开黑啦\\KaiHeiLa')  #将该路径设为当前工作路径

# print(os.getcwd())

# os.path模块其他功能
print(os.path.abspath('No1_文件读写.py'))  #获取绝对路径
print(os.path.exists('No1_文件读写.py'),os.path.exists('No2_文件读写.py'))# 判断文件或目录是否存在
print(os.path.join(os.getcwd(),'No1_文件读写.py'))  # 用join拼接目录和文件名
print(os.path.split('D:\\DS Workout\\Python基础\\No9_编码格式与文件结构\\No1_文件读写.py'))# 分离目录和文件名
print(os.path.splitext('D:\\DS Workout\\Python基础\\No9_编码格式与文件结构\\No1_文件读写.py'))# 分离文件名和扩展名
print(os.path.basename('D:\\DS Workout\\Python基础\\No9_编码格式与文件结构\\No1_文件读写.py'))# 从路径中提取文件名
print(os.path.dirname('D:\\DS Workout\\Python基础\\No9_编码格式与文件结构\\No1_文件读写.py'))# 从路径中提取目录名
print(os.path.isdir('D:\\DS Workout\\Python基础\\No9_编码格式与文件结构'),os.path.isdir('D:\\DS Workout\\Python基础\\No9_编码格式与文件结构\\No1_文件读写.py'))# 判断是否为路径
