#coding: utf-8
import random
import hashlib

def get_inverse(value, p):
    for i in range(1, p):
        if (i * value) % p == 1:
            return i
    return -1


def get_gcd(x, y):
    if y == 0:
        return x
    else:
        return get_gcd(y, x % y)


def add(x1, y1, x2, y2, a, p):  # 计算P+Q=R
    flag = 1  # 符号(+/-)

    # 如果P=Q，斜率k=(3x^2+a)/2y mod p
    if x1 == x2 and y1 == y2:
        member = 3 * (x1 ** 2) + a  # 分子
        denominator = 2 * y1  # 分母

    # 如果P≠Q， 斜率k=(y2-y1)/(x2-x1) mod p
    else:
        member = y2 - y1
        denominator = x2 - x1

        if member * denominator < 0:
            flag = 0  # 表示负数
            member = abs(member)
            denominator = abs(denominator)

    # 将分子分母化为最简形式
    gcd = get_gcd(member, denominator)
    member = member // gcd  # // 表示整数除法，返回整数
    denominator = denominator // gcd

    # 求分母的逆元
    inverse_deno = get_inverse(denominator, p)
    # 求斜率
    k = (member * inverse_deno)
    if flag == 0:
        k = -k
    k = k % p

    # 计算P+Q=(xR,yR)
    xR = (k ** 2 - x1 - x2) % p
    yR = (k * (x1 - xR) - y1) % p

    return xR, yR

def rank(x0, y0, a, b, p): # 计算阶
    x1 = x0  # -P的横坐标
    y1 = (-1 * y0) % p  # -P的纵坐标
    temp_x = x0
    temp_y = y0
    n = 1
    while True:
        n += 1
        xp, yp = add(temp_x, temp_y, x0, y0, a, p)  # P做自加, 直到(xp,yp)==-P，即(xp,yp)+P=0∞，此时n+1为阶数
        if xp == x1 and yp == y1:
            return n + 1
        temp_x = xp
        temp_y = yp

"""
def get_dot(x0, a, b, p):
    y0 = -1
    for y in range(p):
        # 遍历寻找满足椭圆曲线方程的解, P
        if y ** 2 % p == (x0 ** 3 + a * x0 + b) % p:
            y0 = y
            break
    # 如果找不到合适的y0返回False
    if y0 == -1:
        return False
    x1 = x0
    y1 = (-1 * y0) % p   # 由P计算-P
    return x0, y0, x1, y1

"""

def get_publicKey(xG, yG, private_key, a, p):
    temp1 = 0
    temp2 = 0
    temp_x = xG
    temp_y = yG
    while private_key:
        if private_key & 1:
            temp1, temp2 = add(temp1, temp2, temp_x, temp_y, a, p)
        temp_x, temp_y = add(temp_x, temp_y, temp_x, temp_y, a, p)
        private_key >>= 1
    return temp1, temp2

"""
def input_():
    # 选择曲线方程
    while True:
        a = int(input('输入椭圆曲线参数a的值：'))
        b = int(input('输入椭圆曲线参数b的值：'))
        p = int(input('输入椭圆曲线素数p的值：'))

        # 判别式Δ≠0
        if (4 * (a ** 3) + 27 * (b ** 2)) % p == 0:
            print('输入的参数有误，请重新输入！\n')
        else:
            break

    # 选择基点G
    print('在上图坐标系中选择基点G的坐标')
    xG = int(input('横坐标：'))
    yG = int(input('纵坐标：'))

    # 获取曲线的阶
    n = get_rank(xG, yG, a, b, p)

    # 随机生成私钥key，且key<n
    # private_key = int(input('输入私钥key(<%d)：' % n))
    # 生成公钥KEY
    xK, yK = get_publicKey(xG, yG, private_key, a, p)
    return xK, yK, private_key, a, b, p, n, xG, yG
"""
"""
def encrypt(xG, yG, xK, yK, private_key, a, p, n):
    kGx, kGy = get_publicKey(xG, yG, private_key, a, p)  # kG
    kQx, kQy = get_publicKey(xK, yK, private_key, a, p)  # kQ
    plain = input('输入需要加密的字符串：')
    plain = plain.strip()
    c = []
    print('密文为：', end='')
    for char in plain:
        intchar = ord(char)   # 返回ASCII所对应的值, 事实上此处应当调用hashlib库，用哈希函数加密
        cipher = intchar * kQx
        c.append([kGx, kGy, cipher])
        print('(%d,%d),%d' % (kGx, kGy, cipher), end=' ')
    print()
    return c
"""

def decrypt(c, private_key, a, p):
    for charArr in c:
        kQx, kQy = get_publicKey(charArr[0], charArr[1], private_key, a, p)
        print(chr(charArr[2] // kQx), end='')
    print()


if __name__ == '__main__':

    # secp256k1标准下的参数
    p = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFC2F
    a = 0x0000000000000000000000000000000000000000000000000000000000000000
    b = 0x0000000000000000000000000000000000000000000000000000000000000007
    x = 0x79BE667EF9DCBBAC55A06295CE870B07029BFCDB2DCE28D959F2815B16F81798
    y = 0x483ADA7726A3C4655DA4FBFC0E1108A8FD17B448A68554199C47D08FFB10D4B8
    n = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141
    h = 1
    print("椭圆曲线：secp256k1")
    print("p:", hex(p))
    print("a:", hex(a))
    print("b:", hex(b))
    print("基点横坐标x:", hex(x))
    print("基点纵坐标y:", hex(y))
    print("椭圆曲线的阶n:", hex(n))
    # xK, yK, private_key, a, b, p, n, x, y = input_()
    private_key = random.randrange(1, n)
    print("私钥:", hex(private_key))
    xK, yK = get_publicKey(x, y, private_key, a, p) #x, y 基点
    print("公钥:(", hex(xK),", ", hex(yK), ")")
    #c = encrypt(x, y, xK, yK, private_key, a, p, n)
    #decrypt(c, private_key, a, p)

