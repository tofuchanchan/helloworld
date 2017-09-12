import re
#元字符：[]
#常用来指定一个字符集
#元字符在字符集中不起作用 [abc$^] ,$^被看做普通字符
#补集匹配不在区间范围内的字符 [^5],即表示匹配除了这个字符集以外。若想^代表一个普通字符，则不能写在元字符首位

"""
s1 = r'abc adc a^c'
res1 = r'a[bd^]c'

if re.findall(res1,s1):
    print(re.findall(res1,s1))
else:
    print(re.findall(res1,s1))


#元字符：^
#首字符匹配

s2 = r'a b c d e f'
res2 = r'^b'

if re.findall(res2,s2):
    print(re.findall(res2,s2))
else:
    print(re.findall(res2,s2))


#元字符：$
#末字符匹配
s3 = r'a b c d e f'
res3 = r'f$'

if re.findall(res3,s3):
    print(re.findall(res3,s3))
else:
    print(re.findall(res3,s3))

"""

#元字符：\
#1. 取消所有元字符。
#2. \后面接不同字符表达不同含义：
#\d [0-9]
#\D [^0-9]
#\s 匹配任何空白字符 [\t\n\r\f\v]
#\S 匹配任何非空白字符 [^\t\n\r\f\v]
#\w 字符数字下划线[a-zA-Z0-9_]
#\W 非字符数字下划线[^a-zA-Z0-9_]