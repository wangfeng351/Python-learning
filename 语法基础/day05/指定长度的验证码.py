"""
设计一个函数产生指定长度的验证码，验证码由大小写字母数字构成
Date: 2020.03.29

"""

import random

def generate_code(code_len):
    """
    生成指定长度的验证码

    :param code_len: 验证码的长度（4个字符）

    :return: 由 大小写英文字母和数字构成的随机验证码
    """
    all_chars = '0121502054a0sfsdffffffffagaf'
    last_pos = len(all_chars) - 1
    code = ''
    for _ in range(code_len):
        index = random.randint(0, last_pos)
        code += all_chars[index]
    return code


# 调用函数
code = generate_code(6)
print(code)