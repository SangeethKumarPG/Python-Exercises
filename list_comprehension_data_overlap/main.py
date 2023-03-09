with open("list_comprehension_data_overlap/file1.txt") as file1:
    with open("list_comprehension_data_overlap/file2.txt") as file2:
        list_a = [int(i) for i in file1.readlines()]
        list_b = [int(j) for j in file2.readlines()]
        

common_items = [item for item in list_a if item in list_b]
print(list_a)
print(list_b)
print(f"Common items list : {common_items}")