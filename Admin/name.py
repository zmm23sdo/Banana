import random

def unicode():#第一种方法:Unicode码
    val = random.randint(0x4e00, 0x9fbf)
    return chr(val)