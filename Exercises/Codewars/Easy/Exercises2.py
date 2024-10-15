### ! EXERCISE 4

"""Matryoshka dolls are traditionally wooden dolls that can be nested
by fitting smaller dolls into larger ones. Similarly, we can nest lists
by placing smaller lists into larger ones, following specific rules.

Rules for Nesting:

List A can be nested inside List B if:
 - The minimum value in List A is greater than the minimum value in List B.
 - The maximum value in List A is smaller than the maximum value in List B.

Examples :
List A: [2, 3, 9, 5]
List B: [10, 2, 1]
Explanation:

    min(A) = 2 > 1 = min(B)
    max(A) = 9 < 10 = max(B)

Result: A can be nested inside B


List A: [7, 1]
List B: [7, 6, 5, 4, 3, 2]
Explanation:
Both lists share the same maximum value (7).
Result: A cannot be nested properly inside B.

"""


# Solution 1


def matryoshka(nested_list: list):
    for i in range(len(nested_list)):
        for j in range(i + 1, len(nested_list)):
            min_A = min(nested_list[i])
            min_B = min(nested_list[j])
            max_A = max(nested_list[i])
            max_B = max(nested_list[j])

            if not (
                (min_A > min_B and max_A < max_B) or (min_B > min_A and max_B < max_A)
            ):
                return False
    return True


### ! EXERCISE 5

"""You probably know the "like" system from Facebook and other pages. 
People can "like" blog posts, pictures or other items. We want to create 
the text that should be displayed next to such an item.

Implement the function which takes an array containing the names of people that like an item.
It must return the display text as shown in the examples:

[]                                -->  "no one likes this"
["Peter"]                         -->  "Peter likes this"
["Jacob", "Alex"]                 -->  "Jacob and Alex like this"
["Max", "John", "Mark"]           -->  "Max, John and Mark like this"
["Alex", "Jacob", "Mark", "Max"]  -->  "Alex, Jacob and 2 others like this"

Note: For 4 or more names, the number in "and 2 others" simply increases.


"""


# Solution 1


def likes(names):
    if len(names) == 0:
        return "no one likes this"
    elif len(names) == 1:
        return f"{names[0]} likes this"
    elif len(names) == 2:
        return f"{names[0]} and {names[1]} like this"
    elif len(names) == 3:
        return f"{names[0]}, {names[1]} and {names[2]} like this"
    else:
        return f"{names[0]}, {names[1]} and {len(names) - 2} others like this"


# Solution 2


def likes2(names: list[str]) -> str:
    match len(names):
        case 0:
            return "no one likes this"
        case 1:
            return f"{names[0]} likes this"
        case 2:
            return f"{names[0]} and {names[1]} like this"
        case 3:
            return f"{names[0]}, {names[1]} and {names[2]} like this"
        case _:
            return f"{names[0]}, {names[1]} and {len(names) - 2} others like this"


# print(likes(["Peter", "Jacob", "Sara", "Juan", "Pepe"]))
