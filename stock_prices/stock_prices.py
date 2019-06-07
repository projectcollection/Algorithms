#!/usr/bin/python

import argparse
import sys

def find_max_profit(prices):
  curr_low = curr_prof = -sys.maxsize
  for i, price in enumerate(prices):
    if price < curr_low:
      curr_low = price
    for j in range(i+1,len(prices)):
      if prices[j]-price > curr_prof:
        curr_prof = prices[j]-price 
  return curr_prof

  



if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))