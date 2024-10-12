"""
Merge two list
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
"""

list1 = []
list2 = [1,3,4]

list_merged = []

len_list1 = len(list1)
len_list2 = len(list2)

max_leng = max(len_list1, len_list2)

for i in range(max_leng):
    if i < len_list1:
        list_merged.append(list1[i])

    if i < len_list2:
        list_merged.append(list2[i])

print(list_merged)
