# auther: leisurexi
# date: 2020-11-22 23:18
# 插入排序实现

# 1. 遍历总元素个数减1次，因为第一个元素默认是有序的
# 2. 倒序比较，先比较当前元素和它的前一个元素
# 3. 如果前一个元素比当前元素大，就往后挪一位，再往前比较
# 4. 比较到小于当前元素时或者比较完时，代表需要插入了
def insertion_sort(array):
    for i in range(1, len(array)):
        a = array[i]
        # 当前元素的前一个元素下标
        j = i - 1
        for j in range(j, -1, -1):
            if array[j] > a:
                array[j + 1] = array[j]
            else:
                break
        array[j] = a


if __name__ == '__main__':
    array = [6, 5, 6, 3, 2, 1]
    insertion_sort(array)
    print(array)
