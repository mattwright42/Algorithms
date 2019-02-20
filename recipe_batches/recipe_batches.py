#!/usr/bin/python

import math
import operator


def recipe_batches(recipe, ingredients):
  # get the max value from ingredients.items
    batches = max(ingredients.items(), key=operator.itemgetter(1))[1]
  # loop through the recipes dict
    for rkey in recipe.items():
        # if the key from the recipe does NOT appear in ingredietns, batches = 0
        if rkey[0] not in ingredients.keys():
            batches = 0
        # loop through ingredients dict
        for ikey in ingredients.items():
          # if the key of ingredients matches the key of recipe
            if ikey[0] == rkey[0]:
              # check whether we have more ingredients than is called for in the recipe
                if ikey[1] > rkey[1]:
                    # if so, check whether the division is smaller than the current total number of batches
                    if (ikey[1] // rkey[1]) < batches:
                        # if it is lower, then we decrease the total number of batches can be made
                        batches = (ikey[1] // rkey[1])

    # return total number of batches that can be made
    return batches


if __name__ == '__main__':
                    # Change the entries of these dictionaries to test
                    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 132, 'butter': 51, 'flour': 51}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
