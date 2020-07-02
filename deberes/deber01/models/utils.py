import re


def advanced_compare_of_search(original, search):
    pattern = r".*"+(search.strip().lower())+".*"
    # print(pattern, re.search(pattern, original.strip().lower()))
    return re.search(pattern, original.strip().lower())

