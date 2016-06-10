import numpy
import math
import sys
import cat
from itertools import product
#takes a standard quadratic/cubic/quartic... regression
def reg(xs, ys):
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
    if r == 0:
        yield nums
    else:
        for e in product(nums, ops, repeat=r):
            s = ''
            for p in e:
                s += str(p)
            #extra step to end with number instead of operator
            for newe in product([s], nums):
                yield sumstring(newe)
                 
xs = raw_input("What is the input number set, separated with commaspaces?\n").split(', ')
ys = raw_input("What is the output number set, separated with commaspaces?\n").split(', ')
xs = [int(x) for x in xs]
ys = [int(y) for y in ys]

nums = ['x']+[a+b for a, b in product(list('0123456789'), repeat=2)]
for i, n in enumerate(nums):
    nums[i] = n.lstrip('0')
ops = ['+', '/', '-', '*', '**', '%', '+(', '-(', '*(', '/(', '%(' '**(', ')-', ')+', ')-', ')*', ')/', ')**', ')%']

eq = reg(xs, ys)
print eq
if raw_input('does this match your equation? (y/n)').lower() != 'y':
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
                else:s
                    if z != y:
                        running = True
                        break

            if not running:
                print('your equation is\n %s' % eq)
                if raw_input('Does this make sense? (y/n)\n').lower != 'y':
                        running = True
                else:
                    break
        reps += 1
sys.exit()
