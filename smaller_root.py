# Compute the smaller root of a quadratic equation.

###################################################
# Smaller quadratic root formula
# Student should enter function on the next lines.
def smaller_root(a, b, c):
    """
    Returns the smaller root of the quadratic equation
    if one exists
    """
    
    discriminant = (b ** 2) - (4 * a * c)
    
    #if discriminant is positive, 2 sol'ns
    #if dicriminant is 0, 1 sol'n
    #if discriminant is negative, no sol'ns
    if discriminant > 0:
        #2 sol'n
        quad_1 = (-b + (discriminant ** 0.5)) / (2 * a)
        quad_2 = (-b - (discriminant ** 0.5)) / (2 * a)
        return (quad_1 if quad_1 <= quad_2 else quad_2)
    elif discriminant == 0:
        #1 sol'n
        return -b / (2 * a)
    else:
        #discriminant < 0, no solutions
        print "Error: No real solutions"
        
    


###################################################
# Tests
# Student should not change this code.

def test(a, b, c):
    """Tests the smaller_root function."""
    
    print "The smaller root of " + str(a) + "x^2 + " + str(b) + "x + " + str(c) + " is:" 
    print str(smaller_root(a, b, c))
        

test(1, 2, 3)
test(2, 0, -10)
test(6, -3, 5)

###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

#The smaller root of 1x^2 + 2x + 3 is:
#Error: No real solutions
#None
#The smaller root of 2x^2 + 0x + -10 is:
#-2.2360679775
#The smaller root of 6x^2 + -3x + 5 is:
#Error: No real solutions
#None