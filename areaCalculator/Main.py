import math

def paint_calc(height,width,cover):
    area = height*width
    num_cans = math.ceil(area/cover)
    print(f'You would need {num_cans} cans of paint')

test_h = int(input("height of the wall: "))
test_w = int(input("width of the wall: "))
coverage = 5
paint_calc(height = test_h, width = test_w, cover = coverage)
