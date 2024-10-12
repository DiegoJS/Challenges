"""
Input: test = "()[]{}"
Output: true
------------
Input: test = "()[]]{}"
Output: false
"""

def explodeList(stack: list):
    if len(stack) % 2 != 0:
        return []

    item_to_find = '';
    item_depth = 0

    if (stack[0] == '('):
        item_to_find = ')'
    elif (stack[0] == '{'):
        item_to_find = '}'
    elif (stack[0] == '['):
        item_to_find = ']'

    for index in range(1, len(stack)):
        # si el elemento actual es igual al elemento a buscar
        if (stack[0] == stack[index]):
            item_depth += 1

        if (stack[index] == item_to_find):
            if (item_depth > 0):
                item_depth -= 1
            else:
                break

        elif index == len(stack) - 1:
            return []

    new_stack = stack[0:index+1]

    return new_stack


def checkIsValid(stack_to_explore: list):

    new_stack = explodeList(stack_to_explore)

    if len(new_stack) == 0:
        return False

    if len(new_stack) == 2:
        new_stack = []
        return True
    
    if (len(new_stack) < len(stack_to_explore)):
        new_stack_to_explore = stack_to_explore[len(new_stack)::]
        return checkIsValid(new_stack) and checkIsValid(new_stack_to_explore)
    
    # eliminar el primer y ultimo elemento de la lista new_stack
    new_stack = new_stack[1:-1]

    return checkIsValid(new_stack)


test = "([{[]}]){[{}]}{}"

stack_to_explore = list(test)

print(checkIsValid(stack_to_explore))
