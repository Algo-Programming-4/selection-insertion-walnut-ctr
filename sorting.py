def bubble(ary):
    """sorts an array with bubble sort"""
    sorted = False
    times = len(ary)
    while sorted == False:
        sorted = True
        times -= 1
        for i in range(times):
            if ary[i] > ary[i+1]:
                sorted = False
                checking = 0
                swap = ary[i+1]
                ary[i+1] = ary[i - checking]
                ary[i] = swap
    return ary

def selection(ary):
    for i in range(len(ary)):
        min = i
        for j in range(len(ary[i:])):
            if ary[j+i] < ary[min]:
                min = j+i
        swap = ary[i] 
        ary[i] = ary[min]
        ary[min] = swap
    return ary

def insertion(ary):
    for i in range(len(ary) - 1):
        j = i
        while j > 0 and ary[j-1] > ary[j]:
            swap = ary[j] 
            ary[j] = ary[j-1]
            ary[j-1] = swap
            j -= 1          
    return ary

