#Look at test_point.py first!
from triangle import Triangle

#Add a test case here to test Triangle's perimeter function. 
#Remember to use epsilon!
#This is a unit test- it checks if a function gives a correct output for a given input

def test_perimeter():
    pass

#Add a test case here to test Triangle's area function. 
#Remember to use epsilon!
#When unit testing, we often try to give a typical example, then what are called edge cases.
#Edge cases are inputs outside the norm which could break our code. For example,
#What does our code give if we give all zeros for points? Or have a triangle with points that have negative values?
def test_area():
    pass

#Now let's do an integration test. An integration test checks multiple components of a program working together
#In this case, we'll use an integration test to check how many triangles there are in a list of points.
#This will test Triangle.__eq__, Triangle.area, unique_triangles, and all_triangles.
#Make a helper function which figures out how many triangles there are in a list of points, then check if that function gives the
#correct number of trianges on a couple of lists. Make sure your function does not include repeats (using unique_triangles)
#or triangles with zero_area
def integration_test():
    pass