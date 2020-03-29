"""
判断一组文件中图片的个数
Date: 2020.03.29

"""


def count_image(file_list):
    """
    判断一组文件中图片的个数
    :param file 图片文件数量
    
    :return: 图片文件数量
    """
    count = 0
    for file in file_list:
        if file.endswith('png') or file.endswith('.jpg') or \
           file.endswith('webp') or file.endswith('bmp'):
           count = count + 1
    return count


#调用函数
img_list = ['1.jpb', '2.png', '3.webp', '4.bmp', '5.mp3']
result = count_image(img_list)
print('一共有', result, '个图片文件')