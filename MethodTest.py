import Player

def merge(first, second):
    result = []
    while first or second:
        if not first:
            result.append(second.pop(0))
        elif not second:
            result.append(first.pop(0))
        elif first[0] < second[0]:
            result.append(first.pop(0))
        else:
            result.append(second.pop(0))
    return result


def sort(unsorted):
    if not unsorted:
        return unsorted
    if len(unsorted) == 1:
        return unsorted
    midpoint = len(unsorted)//2
    return merge(sort(unsorted[:midpoint]), sort(unsorted[midpoint:]))


# print(sort([5, 2, 3, 6, 1, 4]))

player = Player.Player(1)
print(player.roll_dice())
