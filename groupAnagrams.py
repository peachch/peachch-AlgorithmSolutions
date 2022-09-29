
def groupAnagrams(array):
    dict_new = {}
    final = []
    for i in array:
        keys = "".join(sorted(i))
        print(keys)
        if keys not in dict_new:
            dict_new[keys]=[i]
        else:
            dict_new[keys].append(i)
    # dict_final = {}
    # for j in dict_new.keys():
    #     j_sort = sorted(dict_new[j])
    #     dict_final.setdefault(str(j_sort),[]).append(j)
    #
    # final = []
    # for i in dict_final.values():
    #     final.append(i)
    final = [i for i in dict_new.values()]
    return final


array = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(groupAnagrams(array))