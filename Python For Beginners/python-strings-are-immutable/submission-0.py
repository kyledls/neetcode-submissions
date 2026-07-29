def remove_fourth_character(word: str) -> str:
    first = word[0:3]
    second = word[4:]
    new = first + second
    return new

# do not modify below this line
print(remove_fourth_character("NeetCode"))
print(remove_fourth_character("Hello"))
