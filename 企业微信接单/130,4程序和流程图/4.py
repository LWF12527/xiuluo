#coding=utf-8
def encrypt_password():
    password = input("请输入密码: ")

    numbers = ''
    letters = ''

    for char in password:
        if char.isdigit():
            numbers += char
        else:
            letters += char

    encrypted_password = numbers + letters[::-1].swapcase()

    print("加密后的密码为:", encrypted_password)


# 测试第四题
encrypt_password()