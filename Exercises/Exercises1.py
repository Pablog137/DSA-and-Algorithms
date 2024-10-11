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


