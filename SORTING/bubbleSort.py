def shortBubbleSort (alist):
    exchanges = True
    passnum = len(alist) -1
    while passnum > 0 and exchanges:
        exchanges = False
        for i in range(passnum):
            if alist[i] > alist[i+1]:
                exchanges=True
                temp = alist[i]
                alist[i]=alist[i+1]
                alist[i+1] = temp
        passnum = passnum -1
alist = [90,80,70,60,50,40]
shortBubbleSort(alist)
print alist
