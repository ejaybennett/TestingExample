from point import Point

EPSILON = .0000001

#Use python -m pip install pytest to install pytest, then, in the command line, enter py.test, or if that fails,
#python -m py.test test_point.py
#Pytest will run the file and report on the outcome of tests in that file! If we don't specify a file, it will run tests
# in all files starting with test or ending with _test

#We use Epsilon for equality because with floating point numbers, rounding errors can cause errors: 
def test_distance():
    assert abs(Point(1,1).distance(Point(0,0)) - 2**.5) < EPSILON,"Distance Failed"

def test_magnitude():
    assert abs(Point(1,1).magnitude() - 2**.5) < EPSILON,"MagnitudeFailed"

def test_rounding():
    assert (3**.5)**2==3, "This is why we use rounding!"