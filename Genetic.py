from random import randint

def mutation(li , n):
    mut = []
    for i in li:
        j = randint(0, n-1)
        print(f"For {i}, jth will be changed")
        if i[j] == '1':
            i = i[0:j] + "0" + i[j+1:]
            mut.append(i)
        elif i[j] == '0':
            i = i[0:j] + "1" + i[j+1:]
            mut.append(i)
    return mut

def cr(temp):
    n = 0
    for i in temp:
        if i == "1":
            n = n + 1
    return n

def crossing(li, n):
    crossed = []
    for i in range(0, n, 2):
        temp1 = li[i]
        j = i+1
        temp2 = li[j]
        cp = cr(temp1)
        print(f"Crossover point of {i} is {cp}")
        temp3 = temp1[cp:]
        temp4 = temp2[cp:]
        temp1 = temp1[0:cp] + temp4
        temp2 = temp2[0:cp] + temp3
        crossed.append(temp1)
        crossed.append(temp2)
    return crossed

def pp(li , ac, n):
    co = []
    index = []
    temp = []
    for i in range(n):
        if ac[i] == 1:
            co.append(li[i])
        elif ac[i] >= 2:
            for j in range(ac[i]-1):
                temp.append(li[i])
            co.append(li[i])
        elif ac[i] == 0 and len(temp) != 0:
            co.append(temp[0])
            temp.pop(0)
        elif ac[i] == 0 and len(temp) == 0:
            index.append(i)
    
    if len(index) != 0 and len(temp)!=0:
        for i in index:
            co.insert(i,temp[0])
            temp.pop(0)
    elif len(index) != 0 and len(temp) == 0:
        co.insert(i, li[i])

    return co


def selection(li):
    n = len(li)
    dec = list(map(lambda x : int(x,2),li))

    fit = list(map(lambda x : x*x,dec))

    s = sum(fit)
    prob = list(map(lambda x :round(x/s, 3), fit))

    avg = s/n
    exe = list(map(lambda x : round(x/avg, 3), fit))

    ac = list(map(lambda x : round(x), exe))

    return dec, fit, prob, exe, ac


n = int(input("Enter the number of sample: "))

sam = []

for i in range(n):
    sam.append(input("Enter gene: "))

m = int(input("Enter number of generation: "))
crossed = sam.copy()

for i in range(n):
    dec, fit, prob, exe, ac = selection(crossed)

    s = sum(ac)

    if s < n:
        maxi = max(ac)
        k = ac.index(maxi-1)
        ac[k] += 1
    if s > n:
        mini = min(ac)
        k = ac.index(mini)
        ac[k] -= 1

    print(f"---------------------------------- Generation {i} ----------------------------------")
    print("Population\tX Value\tFitness Val\tProbability\tExpected Count\tActual Count")
    for i in range(n):
        print(f"{crossed[i]}\t\t{dec[i]}\t\t{fit[i]}\t\t{prob[i]}\t\t{exe[i]}\t\t{ac[i]}")

    co = pp(crossed, ac, n)
    print("\nSelected genes for crossover:", co)

    crossed = crossing(co, n)

    print(f"Crossover - {crossed}")

    mutated = mutation(crossed, n)
    print(f"\nMutated - {mutated}")

print("\n GENERATION ", m, "-", mutated)