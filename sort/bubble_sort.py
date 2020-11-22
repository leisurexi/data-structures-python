# auther: leisurexi
# date: 2020-11-21 22:06
# 冒泡排序实现

def bubble_sort(array):
    for i in range(len(array) - 1):
        changed = False
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp
                changed = True
        # 本次循环没有找到需要交换位置的，代表后续已经不需要排序了
        if not changed:
            break


if __name__ == '__main__':
    array = [6, 5, 6, 3, 2, 1]
    bubble_sort(array)
    print(array)
