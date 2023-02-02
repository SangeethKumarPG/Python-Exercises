import math
def paint_calc(test_h,test_w,coverage):
    number_of_cans = math.ceil((test_h * test_w) / coverage)
    print(f"You will need {number_of_cans} of paint") 

test_h = int(input("Enter the height of the wall : "))
test_w = int(input("Enter the width of the wall : "))
cover = 5
paint_calc(test_w=test_w,test_h=test_h,coverage=cover)

