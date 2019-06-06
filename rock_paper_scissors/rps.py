#!/usr/bin/python

import sys
rps = [['rock'], ['paper'], ['scissors']]

def getCartesianProduct(A,B):
  prod = []
  a_counter = 0
  for a in A: # a ['r'] || O(3^n)
    a_counter += 1
    for b in B: # b ['r'] || O(3) since B is always `rps`
      ordered_list = a + b
      prod.append(ordered_list)
  return prod

def rock_paper_scissors(n):
  counter = 1
  if n <= 0:
    return [[]]

  res = rps
  while counter != n: # O(n)
    res = getCartesianProduct(res, rps)
    counter += 1
   
  return res

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')