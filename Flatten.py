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
_list=[]   
def flatten_for(non_flatten):
    for i in non_flatten:
        if type(i)==list:
            flatten_for(i)
        else:
            _list.append(i)
    return _list

x=[[1,'a',['cat'],2],[[[3]],'dog'],4,5]
y=[[1,'a',['cat'],2],[[[3]],'dog'],4,5]
y_f=flatten_for(y)
y_r=y[::-1]
print(flatten_list(x))
print(y_f)
print(y_r)
