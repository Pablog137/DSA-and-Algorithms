### ! EXERCISE 1

"""Complete the method/function so that it converts dash/underscore delimited words into camel casing.
The first word within the output should be capitalized only if the original word was capitalized.
The next words should be always capitalized.

Examples :
"the-stealth-warrior" gets converted to "theStealthWarrior"
"The_Stealth_Warrior" gets converted to "TheStealthWarrior"
"""


# Solution 1
def to_camel_case(text: str):
    result = ""
    capitalize_next = False

    for i in range(len(text)):
        if text[i] in ["-", "_"]:
            capitalize_next = True
        else:
            if capitalize_next:
                result += text[i].upper()
                capitalize_next = False
            else:
                result += text[i]
    return result


example_1 = "the_Stealth-Warrior"
example_2 = "The_Stealth_Warrior"
# print(to_camel_case(example_1))


### ! EXERCISE 2

"""In this kata you will create a function that takes a list of non-negative integers and strings and returns a new list with the strings filtered out.

Examples : 
filter_list([1,2,'a','b']) == [1,2]
filter_list([1,'a','b',0,15]) == [1,0,15]
filter_list([1,2,'aasf','1','123',123]) == [1,2,123]

"""

# Solution 1


def filter_list(listX: list):
    result_list = []

    if listX.count == 0:
        return listX

    for i in listX:
        if type(i) is int:
            result_list.append(i)

    return result_list


# Solution 2


def filter_list2(listX: list):
    return list(filter(lambda x: type(x) is int, listX))


# print(filter_list2([1, 2, "a", "b"]))
# print(filter_list2([1, "a", "b", 0, 15]))
# print(filter_list2([1, 2, "aasf", "1", "123", 123]))
# print(filter_list2([]))


### ! EXERCISE 3

"""Your task is to make a function that can take any non-negative integer as an argument and return it with its digits in descending order. Essentially, rearrange the digits to create the highest possible number.

Examples:
Input: 42145 Output: 54421
Input: 145263 Output: 654321
Input: 123456789 Output: 987654321

"""

# Solution 1


def descending_order(num: int):
    return int("".join(sorted(list(str(num)), reverse=True)))


print(descending_order(42145))
print(descending_order(145263))
print(descending_order(123456789))
print(descending_order(0))
