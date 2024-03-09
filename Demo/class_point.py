# class Point:
#     def draw(self):
#         print('draw')

# point = Point()
# print(type(point))
# print(isinstance(point, int))

# syntax of CONSTRUCTOR DECLARATION
class Math:
    z = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, other):
      
        print("Sum is ", self.y + self.x)

p1 = Math(67, 76)
p2 = Math(43, 532)
combined = p1 + p2
print(combined)
