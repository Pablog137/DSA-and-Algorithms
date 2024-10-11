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
