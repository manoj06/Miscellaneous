s = raw_input("Enter a string to make histogram:\t")
def histogram(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    items = [(v, k) for k, v in d.items()]
    print items
    items.sort()
    items = [(v,k) for k,v in items]
    
    items.reverse()
    print items

     
histogram(s)
