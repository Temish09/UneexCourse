def union_intervals(inter1, inter2):
    
    if inter1[1] < inter2[0]:
        return [False]
    if inter2[1] < inter1[0]:
        return [False]
    
    if inter1[0] <= inter2[0]: 
        if inter1[1] < inter2[1]:
            return [True, (inter1[0], inter2[1])]
        else:
            return [True, inter1]
    
    if inter2[0] < inter1[0]:
        if inter2[1] < inter1[1]:
            return [True, (inter2[0], inter1[1])]
        else:
            return [True, inter2]

def len_inter(inter):
    return inter[1] - inter[0]
    
def union_list_sorted(lst):
    index = 0
    while index < len(lst)-1:
        res = union_intervals(lst[index], lst[index+1])
        if res[0] == True:
            del lst[index]
            del lst[index]
            lst.insert(index, res[1])
        else:
            index += 1
    return lst

lst = list(eval(input()))

lst = union_list_sorted(sorted(lst))
    
sum_inter = 0
for inter in lst:
    sum_inter += len_inter(inter)

print(sum_inter)