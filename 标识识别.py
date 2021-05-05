#实际标识情况举例
shijibiaoshi = [['Blue', 'Round'], ['Blue', 'Square'], ['Red', 'Round'], ['Blue', 'Triangle'], ['Red', 'Square'], ['Red', 'Triangle']]
#shijibiaoshi = [['Blue', 'Round'], ['Red', 'Round'], ['Blue', 'Triangle'], ['Red', 'Triangle'], ['Red', 'Square'], ['Blue', 'Square']]
#shijibiaoshi = [['Blue', 'Square'], ['Red', 'Round'], ['Blue', 'Triangle'], ['Red', 'Triangle'], ['Red', 'Square'], ['Blue', 'Round']]

#定义标识信息
class biaoshi:
    def __init__(self, color_, shape_):
        self.color = color_
        self.shape = shape_

#定义寻找相同形状标识函数
def find(i, shape, color):
    for j in range(i):
        if temp[j] == 'Finish':
            continue
        if temp[j].shape == shape and temp[j].color == color:
            return j + 1
    return False

#变量初始化
temp = []
flag = False
cnt = 0

#第一次遍历识别
for i in range(6):
    color = shijibiaoshi[i][0]
    shape = shijibiaoshi[i][1]
    temp.append(biaoshi(color, shape))
    if not flag:
        if color == 'Blue': #优先识别蓝色
            print('取{:}位置物品'.format(chr(ord('A') + i)))
            flag = True
            shijibiaoshi[i] = 'Finish'
            target = temp[i].shape
            next_ = find(i, target, 'Red') #寻找相同形状红色
            if next_:
                print('取{:}位置物品'.format(chr(ord('A') + next_ - 1)))
                flag = False
                shijibiaoshi[next_ - 1] = 'Finish'
                cnt += 1
    else: #如未寻找到继续遍历识别
        if color == 'Red' and shape == target:
            print('取{:}位置物品'.format(chr(ord('A') + i)))
            flag = False
            shijibiaoshi[next_] = 'Finish'
            cnt += 1

#如未完成，继续进行遍历至完成
while cnt < 3:
    for i in range(6):
        color = shijibiaoshi[i][0]
        shape = shijibiaoshi[i][1]
        if color == 'Blue': #优先识别蓝色
            print('取{:}位置物品'.format(chr(ord('A') + i)))
            shijibiaoshi[i] = 'Finish'
            next_ = find(6, temp[i].shape, 'Red') #寻找相同形状红色
            print('取{:}位置物品'.format(chr(ord('A') + next_ - 1)))
            shijibiaoshi[next_ - 1] = 'Finish'
            cnt += 1