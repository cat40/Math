import numpy
import math
from itertools import product

#takes a standard quadratic/cubic/quartic... regression
def reg(xs, ys):
    deg = len(xs)-1
    array = numpy.zeros((deg+1, deg+1))
    for i, x in enumerate(xs):
        for i2, __ in enumerate(array[i]):
            array[i][i2] = x**(deg-i2)
        #array[i] = col
    A = numpy.matrix(array)
    array = numpy.zeros((deg+1, 1))
    for i, y in enumerate(ys):
        array[i][0] = y
    X = numpy.matrix(array)
    B = A.I*X
    coeffs = [i[0] for i in B]
    eq = ''
    for i, c in enumerate(coeffs):
        if c < 10**-10 and c > -(10**-10):
            c = 0
        if c != 0:
            eq += '%s*x**%s+' % (float(c), deg-i)
    return eq.rstrip('+')

def sumstring(l):
    s = ''
    for i in l:
        s += i
    return s

def comb(r):
    if r == 1:
        yield nums
    else:
        for e in product(nums, ops, repeat=r-1):
            s = ''
            for p in e:
                s += str(p)
            #extra step to end with number instead of operator
            for newe in product([s], nums):
                #print(newe)
                yield sumstring(newe)
                
        
##def exp(xs, ys):
##    if len(xs) < 5:
##        raise IndexError('List of lenth %s is too short to define equation. List of lenth 5 required' % len(xs))
    
xs = raw_input("What is the input number set, separated with commaspaces?\n").split(', ')
ys = raw_input("What is the output number set, separated with commaspaces?\n").split(', ')
xs = [int(x) for x in xs]
ys = [int(y) for y in ys]

nums = ['x']+[a+b for a, b in product(list('0123456789'), repeat=2)]
#will need to inplement psecific parenthese handling to prefvent 1(5)
ops = ['+', '/', '-', '*', '**', '%']

eq = reg(xs, ys)
print eq
if raw_input('does this match your equation? (y/n)').lower() != 'y':
    print'recomputing. this may take a while.'
    done = False
    reps = 1
    #problem: reps += 1 even if all reps at that level have not been exausted
    #need ot get a generator of all possible combonations at a given leve, then do that
    #checking step i snot working for some reason
    while not done:# and reps <= 50:
        print reps
        for eq in comb(reps):
            done = True
            for x, y in zip(xs, ys):
                print eq
                try: #z = eval(eq)
                    if eval(eq) != y:
                        done = False
                except:
                    done = False
                    print '     error'
                    pass
##                except:
##                    done = False
##                    print'    error'
##                    pass
##                else:
##                    #print(z, y)
##                    print'noerror'
##                    if z == y:
##                        #break
##                        #done = True
##                        None
##                    else:
##                        done = False
                #del x
        reps += 1
    print('equation is')
    print('y='+eq)
