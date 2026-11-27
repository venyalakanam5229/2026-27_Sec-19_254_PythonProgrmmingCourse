def rectangle_area_perimeter(length, breadth):
    area = length * breadth
    perimeter = 2 * (length + breadth)
    return area, perimeter
length = 5
breadth = 31
area, perimeter = rectangle_area_perimeter(length, breadth)
print("Area:", area)
print("Perimeter:", perimeter)
