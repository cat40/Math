import numpy
import math
import sys
import cat
from itertools import product

#takes a standard quadratic/cubic/quartic... regression
def reg(xs, ys, retdeg=False):
    deg = len(xs)-1
    array = numpy.zeros((deg+1, deg+1))
    for i, x in enumerate(xs):
        for i2, __ in enumerate(array[i]):
            array[i][i2] = x**(deg-i2)
    A = numpy.matrix(array)
    array = numpy.zeros((deg+1, 1))
    for i, y in enumerate(ys):
        array[i][0] = y
    X = numpy.matrix(array)
    B = A.I*X
    coeffs = [float(i[0]) for i in B]
    eq = ''
    for i, c in enumerate(coeffs):
        #use for comparison; apparently floats are too imprecise
        cr = round(c, 2)
        if c < 10**-10 and c > -(10**-10):
            c = 0  
        if cr == 1:
            eq += 'x**%s+' % (deg-i)
        elif cr:
            eq += '%s*x**%s+' % (float(c), deg-i)
        #finds actual degree of equation
        if c == deg:
            deg -= 1
    #formats equation to make more readable
    eq = eq.rstrip('+')
    
    if retdeg:
        return eq, deg, coeffs
    else:
        return eq

#takes root regression
#uses principal that root equations are the inverse of thier regular counterparts
def root(xs, ys):
    eq, deg, coeffs = reg(ys, xs, True)
    eq = eq.replace('x', 'y')
    #perform limited 'algebra'
    if eq.count('y') == 1:
        c = str(coeffs[len(coeffs)-1-deg])
        c = '' if round(float(c), 2) == 1 else c
        eqt = eq.split('+')
        eql = eq.split('*')
        r = eqt[len(eqt)-1] if eqt[len(eqt)-1] == eql[len(eql)-1] else 0
        if r:
            return str(c)+'x**(1/'+str(deg)+')+'+r
        else:
            return str(c)+'x**(1/'+str(deg)+')'
    else:
        return eq
        

def comb(r):
    if r == 0:
        yield nums
    else:
        for e in product(nums, ops, repeat=r):
            s = ''
            for p in e:
                s += str(p)
            #extra step to end with number instead of operator
            for newe in product([s], nums):
                yield ''.join(newe)
                 
xs = raw_input("What is the input number set, separated with commaspaces?\n").split(', ')
ys = raw_input("What is the output number set, separated with commaspaces?\n").split(', ')
xs = [eval(x) for x in xs]
ys = [eval(y) for y in ys]

nums = ['x']+[str(float(a+b)) for a, b in product(list('0123456789'), repeat=2)]
for i, n in enumerate(nums):
    nums[i] = n.lstrip('0')
ops = ['+', '/', '-', '*', '**', '%', '+(', '-(', '*(', '/(', '%(' '**(', ')-', ')+', ')-', ')*', ')/', ')**', ')%']

eq = reg(xs, ys)
print eq
if raw_input('does this match your equation? (y/n)').lower() != 'y':
    print root(xs, ys)
    if raw_input('does this match your equlation (y/n)').lower() != 'y':
        limit = cat.input.getnum('input complexity limit')
        print'recomputing. this may take a while.'
        running = True
        reps = 0
        while running and reps <= limit:
            print reps
            for eq in comb(reps):
                running = False
                for x, y in zip(xs, ys):
                    try: z = eval(eq)
                    except:
                        running = True
                        pass
                    else:
                        if z != y:
                            running = True
                            break

                if not running:
                    print('your equation is\n %s' % eq)
                    if raw_input('Does this make sense? (y/n)\n').lower != 'y':
                            running = True
                    else:
                        running = False
                        break
            reps += 1
sys.exit()
