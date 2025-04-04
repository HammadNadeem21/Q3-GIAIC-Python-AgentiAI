def triangle():
    triangle_side_1:float = float(input("What is the length of side 1? ")) 
    triangle_side_2:float = float(input("What is the length of side 2? ")) 
    triangle_side_3:float = float(input("What is the length of side 3? ")) 
    triangle_perimeter = triangle_side_1 + triangle_side_2 + triangle_side_3


    print(f"The perimeter of the triangle is {triangle_perimeter}")

triangle()