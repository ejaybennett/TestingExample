#Look at test_point first!
from point import Point
EPSILON = .00000001
#given a list, return a list of all possible arrangements of that list
#Notice the use of recursion to make this easier
def permutations(l):
    if len(l) <=1:
        return [l]
    else:
        ps = []
        for i in range(len(l)):
            ps = ps + [ [l[i]] + p for p in permutations(l[0:i]+(l[i+1:] if i !=len(l)-1 else []) )]
        return ps

class Triangle:
    def __init__(self, point1, point2, point3):
        self.point1 = point1
        self.point2 = point2
        self.point3 = point3
    def perimeter(self):
        return self.point1.distance(self.point2) + self.point2.distance(self.point3) + self.point3.distance(self.point1)
    def side_lengths(self):
        return [self.point1.distance(self.point2), self.point2.distance(self.point3), self.point3.distance(self.point1)]
    def area(self):
        #Calculates the area using Heron's formula
        s = self.perimeter()/2
        a, b ,c = self.side_lengths()
        return (s*(s-a)+(s-b)+(s-c))**.5
    def __eq__(self, other):
        def check_arrangement(triangle1Points, triangle2Points):
            #Helper method to check if a given arrangement of points (eg, [a,b,c] and [d,e,f] or [a,b,c] and [f,d,e]) are equal
            return all([p1.distance(p2) < EPSILON for p1, p2 in zip(triangle1Points, triangle2Points)])
        points1 = [self.point1, self.point2, self.point3]
        points2 = [other.point1, other.point2, other.point3]
        return any([check_arrangement(rearranged, points2) for rearranged in permutations(points1)])
    def __repr__(self):
        return f"[{self.point1}, {self.point2}, {self.point3}]"

def all_triangles(list_of_points):
    #Give all triangles in a list of points
    triangles = [Triangle(p1,p2,p3) for p1 in list_of_points for p2 in list_of_points for p3 in list_of_points]
    return triangles

def unique_triangles(triangles):
    #Take in a list of triangles, then return a list of the unique triangles in that list (no repeats)
    triangles = [triangles[i] for i in range(len(triangles)) if\
         not any([triangles[j] == triangles[i] for j in range(i)])]
    return triangles

if __name__ == "__main__":
    l = [Point(0,0), Point(1,1), Point(0,1), Point(1,0)]
    possible_triangles = all_triangles(l)
    uniques = unique_triangles(possible_triangles)
    print(uniques)

