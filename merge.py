
def merge(intervals):
    intervals.sort(key=lambda x:x[0])
    merged = [intervals[0]]
    for list in intervals[1:]:
        #print(merged)
        if list[0] > merged[-1][1]:
            merged.append(list)
        elif list[0] <= merged[-1][1]:

            merged.append([merged[-1][0],max(list[1],merged[-1][1])])
            merged.pop(-2)


    return merged

intervals = [[1, 3],[8, 10], [2, 6],  [15, 18]]
print(merge(intervals))