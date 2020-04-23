"""
冒泡排序
@Date 2020.04.23
"""

def bubble_sort(items, comp=lambda x, y: x > y):
    items = items[:]
    for i in range(len(items)):
        swapped = False
        for j in range(len(items) - 1 - i):
            if comp(items[j], items[j + 1]):
                items[j],items[j+1] = items[j+1],items[j]
                swapped = True
        if not swapped:
            break
    return items

if __name__ == '__main__':
    list = [58,28,18,8]
    print(bubble_sort(list))