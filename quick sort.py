
#WIP!!! DOESNT WORK!!

def quick(sequence):
    length = len(sequence)
    if length <= 1:
        return sequence
    else:
        pivot = sequence.pop()
        
    
    items_g = [] #greater
    items_l = [] #lower
    
    for item in sequence:
        if item > pivot:
            items_g.append(item)
            
        else:
            items_l.append(item)
        
    return quick(items_l) + [pivot] + qick(items_g)

print(quick([5, 6, 3, 6, 6, 2, 4, 6, 7, 3, 2, 9]))
               
    
