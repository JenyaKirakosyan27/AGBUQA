class TriangleOrNot():
    def __init__(self, sidea, sideb, sidec):
        self.sidea = sidea
        self.sideb = sideb
        self.sidec = sidec
    def is_valid_triangle(self, sidea, sideb, sidec):
        if sidea + sideb >= sidec and sideb + sidec >= sidea and sidec + sidea >= sideb:
            return True
        else:
            return False

    def type_of_triangle(self):
        if sidea == sideb and sideb == sidec:
            print('Triangle is Equilateral.')
        elif sidea == sideb or sideb == sidec or sidea == sidec:
            print('Triangle is Isosceles.')
        elif sidea + sideb >= sidec and sideb + sidec >= sidea and sidec + sidea >= sideb:
            print('Triangle is Scalane')
        else:

            print("Triangle is not possible from given sides.")



sidea = float(input('Enter the length of first side : '))
sideb = float(input('Enter the length of second side : '))
sidec = float(input('Enter the length of third side : '))



triangle = TriangleOrNot(sidea, sideb, sidec)
print(triangle.is_valid_triangle(sidea, sideb, sidec))
triangle.type_of_triangle()

