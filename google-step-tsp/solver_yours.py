#!/usr/bin/env python3

import sys
import math
import copy

from common import print_solution, read_input


def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)


def crossing_judge(city1,city2,city3,city4):
    ta = (city3[0]-city4[0]) * (city1[1]-city3[1]) + (city3[1]-city4[1]) * (city3[0]-city1[0]);
    tb = (city3[0]-city4[0]) * (city2[1]-city3[1]) + (city3[1]-city4[1]) * (city3[0]-city2[0]);
    tc = (city1[0]-city2[0]) * (city3[1]-city1[1]) + (city1[1]-city2[1]) * (city1[0]-city3[0]);
    td = (city1[0]-city2[0]) * (city4[1]-city1[1]) + (city1[1]-city2[1]) * (city1[0]-city4[0]);
    
    return tc*td<0 and ta*tb<0
    #true:cross


def distance_sum(solution,cities):
    the_distance=distance(cities[solution[-1]],cities[solution[0]])
    for l in range(0,len(solution)-1):
        the_distance+=distance(cities[solution[l]],cities[solution[l+1]])
    return  the_distance


def deal_cross(solution,cities):
    old_distance=distance_sum(solution,cities)
    print old_distance
    deal_solution=copy.deepcopy(solution)
    for a in range(40):
        change_times=0
        for i in range(0,len(solution)-1):
            for j in range(i+1,len(solution)-1):
                if crossing_judge(cities[solution[i]],cities[solution[i+1]],cities[solution[j]],cities[solution[j+1]]):
                    change_times+=1
                    solution[i+1] , solution[j] = solution[j] , solution[i+1]
        #for i in range(0,len(solution)-1):
           # if crossing_judge(cities[solution[i]],cities[solution[i+1]],cities[solution[-1]],cities[solution[0]]):
               # solution[i+1] ,solution[-1] = solution[-1] , solution[i+1]
               # change_times+=1
        new_distance=distance_sum(solution,cities)
        if old_distance>new_distance:
            old_distance=new_distance
            print old_distance
            deal_solution=copy.deepcopy(solution)
        if change_times==0:
            print 'break!!!!!!!!!!!!!!'
            break
    return deal_solution


def solve(cities):
    N = len(cities)
    print N
    dist = [[0] * N for i in range(N)]
    for i in range(N):
        for j in range(N):
            dist[i][j] = dist[j][i] = distance(cities[i], cities[j])
            current_city = 0
            unvisited_cities = set(range(1, N))
            solution = [current_city]

    def distance_from_current_city(to):
        return dist[current_city][to]

    while unvisited_cities:
        #print 'unvisited:',len(unvisited_cities)
        next_city = min(unvisited_cities, key=distance_from_current_city)
        unvisited_cities.remove(next_city)
        solution.append(next_city)
        current_city = next_city
    solution=deal_cross(solution,cities)
    return solution


if __name__ == '__main__':
    assert len(sys.argv) > 1
    solution = solve(read_input(sys.argv[1]))#solution:answer
    print_solution(solution)
