# python3
from collections import namedtuple
from itertools import combinations
from math import sqrt
import math


Point = namedtuple('Point', 'x y')


def distance_squared(first_point, second_point):
    return (first_point.x - second_point.x) ** 2 + (first_point.y - second_point.y) ** 2


def minimum_distance_squared_naive(points):
    min_distance_squared = float("inf")

    for p, q in combinations(points, 2):
        min_distance_squared = min(min_distance_squared,
                                   distance_squared(p, q))

    return min_distance_squared
def distance(pts1,pts2):
	return math.sqrt((pts1[0] - pts2[0])**2 + (pts1[1] - pts2[1])**2 )


def minimum_distance_squared(points):
    pts=points
    if len(pts)==2:
		return distance(pts[0],pts[1])
	elif len(pts) == 3:
		return min(distance(pts[0],pts[1]),distance(pts[2],pts[1]),distance(pts[0],pts[2]))
	if len(pts)<2:
		return 0
	d1 = minimum_distance_squared(pts[:len(pts)//2])
	d2 = minimum_distance_squared(pts[len(pts)//2:])
	d = min(d1,d2)
	mid = (pts[len(pts)//2][0] + pts[len(pts)//2+1][0])/2
	s1 = [i for i in pts if abs(mid-i[0])<d]
	if len(s1)==0:
		return d
	s1.sort(key = lambda x: x[1])
	for i in range(len(s1)-1):
		j = 0
		while i+j+1<len(s1)  :
			if(j>5): break
			j+=1
			d = min(d,distance(s1[i],s1[i+j]) )
	return d



if __name__ == '__main__':
    input_n = int(input())
    input_points = []
    for _ in range(input_n):
        x, y = map(int, input().split())
        input_point = Point(x, y)
        input_points.append(input_point)

    print("{0:.9f}".format(sqrt(minimum_distance_squared_naive(input_points))))
