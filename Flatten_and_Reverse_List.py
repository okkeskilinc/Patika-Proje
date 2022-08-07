"""
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
"""   
_list=[]   
def flatten_for(non_flatten):
    for i in non_flatten:
        if type(i)==list:
            flatten_for(i)
        else:
            _list.append(i)
    return _list

_rList=[]
def reverse_list(n):
    for i in reversed(n):
        if type(i)==list:
            _rList.append(i[::-1])
        else:
            _rList.append(i)
    return _rList
    
x=[[1,'a',['cat'],2],[[[3]],'dog'],4,5]
y=[[1, 2], [3, 4], [5, 6, 7]]

x_f=flatten_for(x)
y_r=reverse_list(y)
print(x_f)
print(y_r)
