

#Bitmasks
def add(set,q):
    #add int 5 to set
    set = set | (1<<(q-1))
    return set

    pass
def remove(set,q):
#from the set want to remove q
    set = (set ^ (1<<(q-1)))
    return set
    pass

def display(set):
    n = 10
    subset=[]
    idx=0
    for i in range(0,10):
        if (set & (1<<i)) != 0:
            subset.append(i+1)
    print(subset)
    pass

if __name__=="__main__":
    set = 15
    print(bin(set))
    display(set)
    set = remove(set, 2)
    # display()
    display((add(set,4)))