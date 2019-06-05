#!/usr/bin/python

import math
import sys

def recipe_batches(recipe, ingredients):
  servings = sys.maxsize
  for key in recipe:
    if(key in ingredients):
      serving_per_ingredient = ingredients[key]//recipe[key]
      servings = serving_per_ingredient if serving_per_ingredient < servings else servings
    else:
      return 0
  return servings

if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))