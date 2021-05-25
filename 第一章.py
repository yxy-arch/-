import random
import copy
import math
import string
# r-1.1
def is_multiple (n,m):
    if n%m == 0:
        return True
    else:
        return False

# r-1.2
def is_even (k):
    k = str(bin(k))
    if k[-1] == '0':
        return True
    else:
        return False

# r-1.3
def minmax(data):
    minnum = data[0]
    maxnum = data[0]
    for i in range(len(data)):
        if (data[i] > maxnum):
            maxnum = data[i]
        if (data[i] < minnum):
            minnum = data[i]
    return maxnum,minnum

# r-1.4
def sumsquare(n):
    sum = 0
    for i in range(1,n+1):
        sum += i**2
    return sum

# r-1.5
# sum([i**2 for i in range(1,n+1)])

# r-1.6
def oddsquare(n):
    sum = 0
    for i in range(1,n+1):
        if i%2 != 0:
            sum += i**2
    return sum

# r-1.7
# sum([i*i for i in range(1,n+1) if i%2 != 0])

# r-1.8
def foundindex(data,n):
    for i in range(n):
        m = i - n
        print(i,data[i])
        print(m,data[m])

# r-1.9
# range(50,90,10)

# r-1.10
# range(8,-10,-2)

# r-1.11
# a = [chr(ord('a') + i) for i in range(26)]

# r-1.12
def mychoice(data):
    return data[random.randrange(len(data))]

# r-1.13
def myreverse(data,n):
    data1 = copy.deepcopy(data)
    for i in range(n):
        data[i] = data1[n-1-i]
    return data

# r-1.14
def oddproduct(data):
    product = []
    for i in range(len(data)):
        for j in range(len(data)):
            if i == j:
                continue
            if ((a[i]*a[j]) % 2 != 0):
                product.append((a[i],a[j]))
    return product
def judge1(data):
    a = [i for i in data if i%2 != 0]
    return (len(a) > 0)

# r-1.15
def judge2(data):
    return (len(data) == len(set(data)))

# r-1.16 创造一个新的实例，将实例赋值给原来的索引。

# r-1.17 改变了val的值，但没有改变data中原本对应的值。

# r-1.18
# a = [i*(i+1) for i in range(10)]

# r-1.19
# a = [ord(chr('a')+i) for i in range(26)]

# r-1.20
def MyShuffle(data):
    for i in range(len(data)):
        data[i] = data[random.randint(0,len(data)-1)]
    return data
def shuffle_(n):
    import random
    s= list()
    for i in range(len(n)-1,-1,-1):
        s.append(n.pop(random.randint(0,i)))
    return s

# r-1.21
def eof():
    flag = 1
    words = []
    try:
        while flag:
            words.append(input())
    except EOFError:
        for word in words[::-1]:
            print(word)

# r-1.22
def dot(a,b):
    for i in range(len(a)):
        a[i] *= b[i]
    return a

# r-1.23
def get_index(data,i):
    try:
        return data[i]
    except IndexError:
        print('IndexError')

# r-1.24
def voewl(data):
    letter = {}
    for i in range(len(data)):
        if data[i] in ('a','e','i','o','u'):
            letter[data[i]] = letter.get(data[i],0) + 1
    return letter

# r-1.25
def removepunct(string):
    string1 = ''
    for i in string:
        if i in [chr(ord('a') + i) for i in range(26)] or i in [chr(ord('A') + i) for i in range(26)]:
            string1 += i
    return string1

# r-1.26
def equal():
    a = eval(input())
    b = eval(input())
    c = eval(input())
    return a + b == c or a == b -c or a * b == c

# r-1.27
def factors(n):
    s=[]
    for i in range(1,int(n**0.5)+1):
        if n%i ==0:
            yield i
            s.append(n//i)
        if i*i==n:
            s.remove(i)
    while s:
        yield s.pop()

# r-1.28
def norm(v,p):
    val = 0
    for i in range(len(v)):
        val += pow(v[i],p)
    return pow(val,1/p)

# r-1.29
def permutation(n):
    if len(n)>1:
        for i in range(0,len(n)):
            print(n[i])
            if i !=0:
                permutation(n[:i-1]+n[i+1:])
            else:
                permutation(n[i+1:])
    if len(n)==1:
        print(n[0]+'\n\n')
        return 0

# r-1.30
def divide(n):
    count = 0
    while n >= 2:
        n = n//2
        count += 1
    return count

# r-1.31
def pocketmoney(a,b):
    money = [1,2,5,10,20,50,100]
    num = {}
    while (a != b):
        n = money.pop()
        if (b-a)//n:
            num[n] = (b-a)//n
            b = b - ((b-a)//n)*n
        else:
            continue
    return num

# r-1.32
def calculator():
    words = ''
    flag = 1
    while flag:
        a = input("'quit' to quit")
        if a == 'quit':
            flag = 0
        else:
            words += a
    return eval(words)

# r-1.33
def handcalculator():
    def calculator():
        words = ''
        flag = 1
        while flag:
            a = input("'quit' to quit")
            if a == 'quit':
                flag = 0
            else:
                words += a
        print(eval(words))
        return 0

# r-1.34
def mu_rror(n,m):                           #n为重复数，m为错误数
    import random
    rl = set()
    while len(rl)<m:
        rl.add(random.randint(0,n-1))
    rl = sorted(list(rl),reverse=True)
    word = 'I never spam my friends agin.'
    for i in range(n):
        if len(rl) > 0  and i == rl[-1]:
            rl.pop()
            rror_l = list(word)
            num = random.randint(0,len(word)-1)
            rror_l[num] = chr(ord(rror_l[num])+random.randint(0,1000))
            print(''.join(rror_l))
        else:
            print(word)
# r-1.35
def birth_age(num):
    a = 1
    for i in range(num):
        a *= (365-i)/365
    prop = 1-a
    return prop

def birthday():
    import random
    resort = []
    for i in range(5,101,5):
        s= random.choices(range(1,366),k=i)
        resort.append(len(s)==len(set(s)))
    return resort

# r-1.36
def count(words):
    dict = {}
    words = words.strip(string.punctuation).split(' ')
    for i in words:
        dict[i] = dict.get(i,0) + 1
    return dict

def num_word():
    import string
    temp = input("Please input a string: \n").strip(string.punctuation).split(" ")
    keys = list(set(temp))
    result = dict(zip(keys,[0]*len(keys)))
    for item in temp:
        result[item] += 1
    return result

# 测试
if __name__ == '__main__':
    # r-1.1
    print(is_multiple(6,2))
    print(is_multiple(7,2))

    # r-1.2
    print(is_even(1))
    print(is_even(6))

    # r-1.3
    a = [random.randint(0,100) for i in range(10)]
    print(a)
    print(minmax(a))

    # r-1.4
    print(sumsquare(4))

    # r-1.5
    print(sum([i**2 for i in range(1,5)]))

    # r-1.6
    print(oddsquare(4))

    # r-1.7
    print(sum([i*i for i in range(1,5) if i%2 != 0]))

    # r-1.8
    foundindex([random.randint(0,100) for i in range(10)],10)

    # r-1.9
    print(list(range(50, 90, 10)))

    # r-1.10
    print(list(range(8,-10,-2)))

    # r-1.11
    a = [pow(2, i) for i in range(9)]
    print(a)

    # r-1.12
    l1 = [i**2 for i in range(1,5)]
    print(random.choice(l1))
    print(mychoice(l1))

    # r-1.13
    a = [i for i in range(10)]
    print(myreverse(a,10))

    # r-1.14
    a = [i for i in range(10)]
    print(oddproduct(a))
    print(judge1(a))

    # r-1.15
    print(judge2(a))
    # a[0] = 1;
    # print(judge2(a))

    # r-1.18
    a = [i * (i + 1) for i in range(10)]
    print(a)

    # r-1.19
    a = [chr(ord('a') + i) for i in range(26)]
    print(a)

    # r-1.20
    print(MyShuffle(a))
    print(shuffle_(a))

    # r-1.21
    # eof()

    # r-1.22
    # a = dot(list(range(5)),list(range(5)))
    # print(a)

    # r-1.23
    a = [chr(ord('a') + i) for i in range(26)]
    print(get_index(a,15))
    print(get_index(a,27))

    # r-1.24
    a = 'qweqdsbsibndioansfsdcsvgdsexu'
    print(voewl(list(a)))

    # r-1.25
    a = 'HELLo,.; WORL#D'
    print(removepunct(a))

    # r-1.26
    # print(equal())

    # r-1.27
    for factor in factors(100):
        print(factor)

    # r-1.28
    print(norm([3,4],2))

    # r-1.29
    permutation('catdog')

    # r-1.30
    a =divide(8)
    print(a)

    # r-1.31
    print(pocketmoney(20,100))

    # r-1.32
    # print(calculator())

    # r-1.33
    # handcalculator()

    # r-1.34
    mu_rror(100,8)

    # r-1.35
    print(birth_age(23))
    print(birth_age(22))

    # r-1.36
    print(count('he apple world tree apple!'))
    print(num_word())