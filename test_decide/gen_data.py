''' 
This module generates random valid input to decide.py.
'''

import sys
import math
from json import dump
from random import randint, uniform

num_points = int(sys.argv[1])
axis_range = int(sys.argv[2])
l1 = uniform(0,axis_range) 
r1 = uniform(0,axis_range)
eps = uniform(0,math.pi)
a1 = uniform(0,axis_range)
q_pts = randint(2, num_points)
quads = randint(1,3)
dist = uniform(0,axis_range)
n_pts = randint(3, num_points) 
k_pts = randint(2, num_points-2)
a_pts = randint(1,int((num_points-3)/2))
b_pts = randint(1,int((num_points-3)/2))
c_pts = randint(1,int((num_points-3)/2))
d_pts = randint(1,int((num_points-3)/2))
e_pts = randint(1,int((num_points-3)/2)) 
f_pts = randint(1,int((num_points-3)/2)) 
g_pts = randint(1,num_points-2) 
l2 = uniform(0,axis_range)
r2 = uniform(0,axis_range)
a2 = uniform(0,axis_range)


def gen_connector():
    r = randint(1,3)
    if r == 1: return 'NOTUSED'
    if r == 2: return 'ORR'
    if r == 3: return 'ANDD'

data : dict = { 
    "numpoints"  : num_points,
    "datapoints" : [ [uniform(-1000,1000), uniform(-1000,1000)] 
                     for _ in range(num_points) ],
    "lcm"        : [ [gen_connector() for _ in range(15)]
                     for _ in range(15)],
    "puv"        : [ bool(randint(0,1)) for _ in range(15)],
    "parameters" : {
        "length1"   : l1,
        "radius1"   : r1,
        "epsilon"   : eps,
        "area1"     : a1,
        "qpts"      : q_pts,
        "quads"     : quads,
        "dist"      : dist,
        "npts"      : n_pts,
        "kpts"      : k_pts,
        "apts"      : a_pts,
        "bpts"      : b_pts,
        "cpts"      : c_pts,
        "dpts"      : d_pts,
        "epts"      : e_pts,
        "fpts"      : f_pts,
        "gpts"      : g_pts,
        "length2"   : l2,
        "radius2"   : r2,
        "area2"     : a2
    }
}
dump(data,sys.stdout)
print()
