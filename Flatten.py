def flatten_list(non_flatten):
    flatten_list=[]
    while(non_flatten):
        empty=non_flatten.pop()
        if type(empty)==list:
            non_flatten.extend(empty)
        else:
           flatten_list.append(empty)
    
    #flatten_list.sort()
    return flatten_list

x=[[1,'a',['cat'],2],[[[3]],'dog'],4,5]
print(flatten_list(x))
