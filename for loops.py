#print 0 to 9
i = 1
for i in range (0,10):
    print(str(i))
print('the end')
print('\n')

#
number = [5, 2, 5, 2, 2]
for i in number:
    print("#" * i)
print('\n')

class Point:
    def draw(self):
        print("draw")
    def move(self):
        print("move")
    def align(self):
        print('align')

point1 = Point()
point1.align

from pathlib import Path
path = Path()
for file in path.glob('*.py'):
    print(file)
    
