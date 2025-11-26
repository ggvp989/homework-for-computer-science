#сортировка колоды
from random import*
def deck_card(x):

    if len(x)<=4:
        return sorted(x)

    else:
        pivot=randint(1, max(x))
        lt=[]
        rt=[]
        for i in x:
            if i>pivot:
                rt.append(i)

            elif i<=pivot:
                lt.append(i)

        return (deck_card(lt)+deck_card(rt))
print(deck_card([4, 2, 7, 1, 3, 5]))
print(deck_card([10, 5, 3, 8]))
print(deck_card([1]))
print(deck_card([3, 2]))
print(deck_card([7, 3, 3, 4, 1, 2, 5]))
