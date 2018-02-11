import random, string


def coupon_ge(amount, length):
    with open(r'd:\gakki\coupon.txt', 'w') as f:
        choice = string.letters + string.digits
        for i in range(amount):
            temp = ''
            for j in range(length):
                temp += random.choice(choice)
            f.write(temp + '\n')


if __name__ == '__main__':
    coupon_ge(200, 20)