import matplotlib.pyplot as plt
import random
import math
import time

def solution(x, y):
    '''
    :param x is the x coordinates of points:
    :param y is the y coordinates of points:
    :return closest pair of points :
    '''
    points = list(zip(x, y))   # zipping x and y coordinates as (x,y)
    points_x = sorted(points, key=lambda x: x[0])   # pre-sorting points x-wise
    points_y = sorted(points, key=lambda x: x[1])   # pre-sorting points y-wise
    p1, p2, md = closest_pair(points_x, points_y, len(points_x))
    return p1, p2, md

def getdist(p, q):
    '''
    :param p is a point:
    :param q is a point:
    :return euclidean distance between p and q:
    '''

    return ((p[0] - q[0])**2 + (p[1] - q[1])**2) ** 0.5

def bruteforce(ax, len):
    '''
    :param ax is a list of points:
    :param len is length of ax:
    :return the points with min distance in ax and min distance:
    '''

    dist_min = 0
    p1, p2 = [], []
    for i in range(max(len-1,1)):
        for j in range(i+1, max(len,2)):
            dist_temp = getdist(ax[i], ax[j])
            if (i == 0 and j == 1) or dist_temp < dist_min:
                dist_min = dist_temp
                p1, p2 = ax[i], ax[j]
    return p1, p2, dist_min

def closest_split_pair(ax, ay, min_dist, min_point, leng):
    '''
    :param ax: points sorted x-wise
    :param ay: points sorted y-wise
    :param min_dist: minimum distance so far
    :param min_point: two points with minimum distance so far
    :param leng: length ax (or ay)
    :return:
    '''

    Sy = list()
    ln_y = 0
    mid_x = ax[int(math.ceil(leng/2))]

    for i in range(leng):
        if abs(ay[i][0] - mid_x[0]) <= min_dist:
            Sy.append(ay[i])
            ln_y += 1

    best = min_dist
    best_pair = min_point

    for i in range(ln_y - 1):
        for j in range(i+1, min(i + 7, ln_y)):
            p, q = Sy[i], Sy[j]
            dst = getdist(p, q)
            if dst < best:
                best_pair = p, q
                best = dst
    return best_pair[0], best_pair[1], best

def closest_pair(ax, ay, leng):
    #plot()
    if leng <= 3:
        return bruteforce(ax, leng)
    else:
        index = int(math.ceil(leng/2.))
        Qx = ax[:index]
        Rx = ax[index:]
        Qy = []
        Ry = []
        midpoint = ax[index-1][0]
        for x in ay:
            if x[0] <= midpoint:
                Qy.append(x)
            else:
                Ry.append(x)
        p1, q1, dist1 = closest_pair(Qx, Qy, index)
        p2, q2, dist2 = closest_pair(Rx, Ry, index - 1)
        min_dist = 0
        min_point = ()
        if dist1 < dist2:
            min_point = (p1, q1)
            min_dist = dist1
        else:
            min_point = (p2, q2)
            min_dist = dist2

        p3, q3, dist3 = closest_split_pair(ax, ay, min_dist, min_point, leng)

        return p3, q3, dist3

sample = 200
for i in range(1):
    start = time.time()
    sample = sample*2
    x, y = random.sample(range(sample), sample), random.sample(range(sample), sample)
    fig = plt.figure()
    ax = fig.add_subplot(111)
    p_1, p_2, min_dist = solution(x,y)
    end = time.time()
    print("Input size: ",sample,", Running time in second: ", end-start)
    print(p_1)
    x_list, y_list = [], []
    x_list.append(p_1[0])
    x_list.append(p_2[0])
    y_list.append(p_1[1])
    y_list.append(p_2[1])
    plt.scatter(x, y, color="green")
    plt.scatter(x_list, y_list, color="blue")
    plt.show()

