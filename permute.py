import itertools
import sys
import time

def run(n):
    n = int(sys.argv[1])
    l = [0]*(n-1)
    start_time = time.time()
    for i in range(n+1):
        l.append(i)
    permute = list(itertools.permutations(l))

    list_permute = []
    for i in permute:
        string = ''
        for k in i:
            string += str(k)
        list_permute.append(string + '\n')
    print("%s секунд" % (time.time() - start_time))

    f = open('text.txt', 'w')
    for index in list_permute:
        f.write(index)

    f.close()

    print(f'Для чисел от 0 до {n} существует {len(list_permute)} перестановки(ок)')
