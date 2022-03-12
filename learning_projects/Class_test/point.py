import numpy as np

class Point:
    
    def __init__(self, initX, initY):
        self.x = initX
        self.y = initY
        
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    
    def distanceFromOrigin(self):
         return ((self.x ** 2) + (self.y ** 2)) ** 0.5
    
    def distanceFromPoint(self,target):
        x_sum = (target.getX() - self.x)
        y_sum = (target.getY() - self.y)
        return (x_sum**2 + y_sum**2) ** 0.5
    
    def reflect_x(self):
        return (self.x,-self.y)
    
    def slope_from_origin(self):
        return self.y/self.x
    
    def slope_from_point(self,target):
        x_diff = self.x - target.x
        y_diff = self.y - target.y
        if x_diff == 0:
            return 'Slope is undefined'
        else:   
            return y_diff/x_diff
    
    def get_line_to(self,target):
        m = self.slope_from_point(target)
        q_num = ((self.x*target.y)-(self.y*target.x))
        q_den = (self.x-target.x)
        if q_den == 0:
            return (m,0)
        else:
            return (m,q_num/q_den)
        
    def move(self,dx,dy):
        self.x += dx
        self.y += dy
        return Point(self.x,self.y)

    def get_circumference(self,p,q):
        left_side = np.array([[2*self.x, 2*self.y, 1], [2*p.x, 2*p.y, 1], [2*q.x, 2*q.y, 1]])
        right_side = np.array([-((self.x)**2)-((self.y)**2),-((p.x)**2)-((p.y)**2),-((q.x)**2)-((q.y)**2)])
        result = np.linalg.inv(left_side).dot(right_side)
        center = (-float(result[0]),-float(result[1]))
        radius = (((float(result[0]))**2)+((float(result[1]))**2)-(float(result[2]))) ** 0.5
        return result , center , radius
    
p = Point(0,0)
q = Point(4,3)
f = Point(12,3)
print(f.distanceFromOrigin())
print(q.distanceFromPoint(f))
print(Point(3,5).reflect_x())
print(Point(4, 10).slope_from_origin())
print(Point(4, 10).slope_from_point(Point(3,10)))
print(Point(4, 11).get_line_to(Point(4, 11)))
new_p = q.move(1,1)
print(new_p.x,new_p.y)

p1=Point(0,1)
q1=Point(1,0)
r1=Point(-1,0)

print(q1.get_circumference(p1,r1))
