
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


