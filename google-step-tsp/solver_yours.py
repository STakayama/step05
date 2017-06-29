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
        print len(unvisited_cities)
        solution.append(next_city)
        current_city = next_city
        not_cross_solution=copy.deepcopy(solution)
    #print crossing_judge(cities[solution[2]],cities[solution[3]],cities[solution[4]],cities[solution[5]])
    for i in range(1,len(solution)-1):
        for j in range(i+1,len(solution)-1):
                    if crossing_judge(cities[not_cross_solution[i]],cities[not_cross_solution[i+1]],cities[not_cross_solution[j]],cities[not_cross_solution[j+1]]):
                        # if l==len(solution):
                        append_flag=False
                        for_break_flag=True
                        #print solution
                        #solution.append(next_city)
                        #print i
                        #print j
                        #print not_cross_solution
                        not_cross_solution[i+1] , not_cross_solution[j] = not_cross_solution[j] , not_cross_solution[i+1]
                        #print not_cross_solution

                        #solution.insert(j,k)
                        #solution.pop()
                        #for_break_flag=True
                        #    break
                        #if for_break_flag:
                        #   break
                        #if append_flag:
                        #print len(solution)


    #sorted(set(solution),key=solution.index)
    #solution=copy.deepcopy(not_cross_solution)
    #print len(solution)
    return not_cross_solution


if __name__ == '__main__':
    assert len(sys.argv) > 1
    solution = solve(read_input(sys.argv[1]))#solution:answer
    print_solution(solution)
