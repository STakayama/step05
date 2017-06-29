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
    whether_closs=(tc*td<0)&(ta*tb<0)
    return whether_closs
  #true:cross


def solve(cities):
    N = len(cities)#512
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
        append_flag=True
        for_break_flag=False

        for i in range(1,len(solution)):
            for j in range(i+1,len(solution)):
                if crossing_judge(cities[solution[i]],cities[solution[j]],cities[solution[-1]],cities[next_city]):
                    append_flag=False
                    for_break_flag=True
                    #print solution
                    #solution.append(next_city)
                    #solution[-1],solution[j]=solution[j],solution[-1]
                    solution.insert(j,solution[-1])
                    solution.pop()
                    for_break_flag=True
                #    break
            #if for_break_flag:
             #   break
        unvisited_cities.remove(next_city)
        #if append_flag:
           #print len(solution)
        solution.append(next_city)
        current_city = next_city


    #sorted(set(solution),key=solution.index)
    print len(solution)
    print solution
    return solution


if __name__ == '__main__':
    assert len(sys.argv) > 1
    solution = solve(read_input(sys.argv[1]))#solution:answer
    print_solution(solution)
