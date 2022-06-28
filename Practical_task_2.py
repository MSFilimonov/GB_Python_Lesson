source_ist = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
more_list = [el for el in source_ist if el > source_ist[source_ist.index(el)-1]]
print(more_list)
