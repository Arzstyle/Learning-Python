if __name__ == '__main__':
    N = int(input())

29
N.append(1)
N.append(6)
N.append(10)
N.append(8)
N.append(9)
N.append(2)
N.append(12)
N.append(7)
N.append(3)
N.append(5)
N.insert(8, 66)
N.insert(1, 30)
N.insert(6, 75)
N.insert(4, 44)
N.insert(9, 67)
N.insert(2, 44)
N.insert(9, 21)
N.insert(8, 87)
N.insert(1, 75)
print(N)

N.reverse()
print(N)

N.sort()
print(N)

N.append(2)
N.append(5)
N.remove(2)
print(N)