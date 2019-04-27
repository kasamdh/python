'''
Implement function swapFL() that takes a list as input and swaps the first and last elements of the list.
You may assume the list will be nonempty.
The function should not return anything.
>>> ingredients = ['flour', 'sugar', 'butter', 'apples']
>>> swapFL(ingredients)
>>> ingredients
['apples', 'sugar', 'butter', 'flour']
'''
def swapFL(ingredients):
    ingredientFirst=ingredients[0]
    ingredientLast=ingredients[-1]

    ingredients[0]= ingredientLast
    ingredients[-1]=ingredientFirst

    return(ingredients)
ingredients = ['flour', 'sugar', 'butter', 'apples']
print(swapFL(ingredients))
