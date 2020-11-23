# auther: leisurexi
# date: 2020-11-23 23:23

"""
选择排序
1.原地排序算法：不需要额外存储空间。
2.不稳定的排序算法：每次需要找出未排序中元素的最小值，并和前面的元素交换位置；
比如 5,8,5,2,9 这样一组数据，当第一次找到2位最小元素时，与第一个5交换位置，
那第一个5和中间位置的5位置就变了，所有不是稳定的排序算法。
"""


def selection_sort(array):
    sorted_index = 0
    for i in range(len(array) - 1):
        min_index = sorted_index

        for j in range(sorted_index + 1, len(array)):
            if array[min_index] > array[j]:
                min_index = j

        temp = array[i]
        array[i] = array[min_index]
        array[min_index] = temp
        sorted_index += 1


if __name__ == '__main__':
    array = [6, 5, 6, 3, 2, 1]
    selection_sort(array)
    print(array)
