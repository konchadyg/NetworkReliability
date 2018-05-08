#####################################
#CS 6385.001 | PROJECT-3            #
#Author: Konchady Gaurav Shenoy     #
#NETID: kxs168430                   #
#####################################

import sys
import random


# Matric Generation

def generate_matrix():
    edgematrix = [combo_gen(i) for i in range(1024)]
    return edgematrix

# Generate combo for 10

def combo_gen(n):
    combo = [i for i in range(10)]
    combolen = len(combo)
    for i in range(combolen - 1, -1, -1):
        combo[i] = n % 2	
        n /= 2
    return combo


# Calculate the connectivity for the given combination matrix edgematrixrix and
# link reliability p
def calc_reliability(edgematrix, p):
    if p == 0.0:
        return 0.0 #Duh

    net_reliability = 0.0
    for i in edgematrix:

        adjacent_mat = [[0 for x in range(5)] for x in range(5)] #Generating the adjacent
        adj_i, adj_j = 0, 1
        for j in range(10):

            if adj_j == 5 and adj_i == 0:
                adj_i, adj_j = 1, 2
            if adj_j == 5 and adj_i == 1:
                adj_i, adj_j = 2, 3
            if adj_j == 5 and adj_i == 2:
                adj_i, adj_j = 3, 4

            if adj_j <= 4:
                # print m,',',n
                adjacent_mat[adj_i][adj_j] = i[j]
                adjacent_mat[adj_j][adj_i] = i[j]
                adj_j += 1

        if is_connected(adjacent_mat):
            net_reliability += get_reliability(i, p) # Add up individual reliabilities to get net reliability

    return net_reliability
    # print  count


def get_reliability(edgematrix, p):
    rel = 1.0
    for col in edgematrix:
        if col == 1:
            rel = rel * p # p hence UP
        else:
            rel = rel * (1.0 - p) # 1-p hence DOWN
    return rel


def rel_range_p(begin, end, increment):
    r = begin
    while r <= end:
        yield r
        r += increment


def reliability_k(edgematrix, k):

    while k>0:
        i = random.randint(0,1023) #Generate from 0 to 1023
        edgematrix[i] = toggle_state(edgematrix[i])
        k -= 1
    return calc_reliability(edgematrix, 0.85)

# toggle link state. 0->1 or 1->0
def toggle_state(edgematrix):

    for i in range(10):
		edgematrix[i] = (edgematrix[i]+1)%2
    return edgematrix


def part1(edgematrix):

    print '*****************************'
    print '[p]\t\tReliability'
    print '*****************************'
    listp = []
    listr = []
    for p in rel_range_p(0.0, 1.0, 0.04): #Increments for 0.04
        listp.append(p)
        val = calc_reliability(edgematrix, p)
        listr.append(val)
        print p, '\t', val
    print '*****************************'
    print


def part2(edgematrix):
    print 'Value of p = 0.85'
    print '*****************************'
    print '[k]\tReliability'
    print '*****************************'

    for k in range(26):
        k_rel_value = reliability_k(edgematrix, k)
        print k, '\t', k_rel_value
    print '*****************************'

def is_connected(adjacent_mat):
    visited = [False for i in range(5)]
    dfs_traverse(adjacent_mat, visited, 0)
    for i in visited:
        if i is False:
            return False
    return True

def dfs_traverse(adjacent_mat, visited, j):
    visited[j] = True
    for k in range(5): # n=5 nodes
        if adjacent_mat[j][k] == 1 and visited[k] == False:
            dfs_traverse(adjacent_mat, visited, k)	

def main():
    edgematrix = generate_matrix()
    part1(edgematrix)
    part2(edgematrix)


if __name__ == '__main__':
    main()	