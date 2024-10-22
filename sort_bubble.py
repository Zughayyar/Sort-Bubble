########################
#### Anas Zughayyar ####
########################
##### Bubble Sort #####
########################

def sort_bubble(some_list):
    n = len(some_list)
    for i in range(0,n):
        for j in range(0,n-i-1):
            if some_list[j] > some_list[j+1]:
                temp = some_list[j]
                some_list[j] = some_list[j+1]
                some_list[j+1] = temp
    return some_list

list_1 = [8,5,2,6,9,3,1,4,0,7]
list_2 = [81,53,12,-6,53,3,1,4,-2,7]
list_3 = [81,-6,53,3,-11,324,-22,100]

print(sort_bubble(list_1))
print(sort_bubble(list_2))
print(sort_bubble(list_3))
