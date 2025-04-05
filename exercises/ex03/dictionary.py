"""EX03: Dictionary"""

__author__: str = "730464690"


def invert(original: dict[str, str]) -> dict[str, str]:
    inverted = {}
    for k in original.keys():
        if original[k] in inverted:
            raise KeyError("duplicate key")
        inverted[original[k]] = k
    return inverted


def count(items: list[str]) -> dict[str, int]:
    """Count how many times each value in a list occurs"""
    counts = {}  # Initialize an empty dictionary
    for item in items:  # Loop thru each item
        if item in counts:
            counts[item] += 1
        else:
            counts[item] = (
                1  # Initializes items that are encountered for the first time as occurring once
            )
    return counts


def favorite_color(colors: dict[str, str]) -> str:
    """Returns the most popular color, or the first color encountered (out of the colors that are tied) if there's a tie"""
    color_tally = count(
        list(colors.values())
    )  # Using the count function to helps us count occurrences!
    max_tally = 0
    winning_color = ""
    for color in colors.values():
        if color_tally[color] > max_tally:
            max_tally = color_tally[color]
            winning_color = color
    return winning_color


def bin_len(words: list[str]) -> dict[int, set[str]]:
    """Bins a list of strings into a new dictionary where the keys are the string lengths and the values are a new set of words of that specific length"""
    length_bins = (
        {}
    )  # initialize an empty dictionary where the keys are word lengths and the values are the number of words of that length
    for word in words:
        length = len(word)  # compute each word's length
        if length not in length_bins:
            length_bins[length] = (
                set()
            )  # if encountering a new length, initialize an empty set and add the word to it
        length_bins[length].add(word)
    return length_bins  # return final dictionary
