#10
words = lambda s: sum(
    1 for x in s.split()
    if any(ch.isdigit() for ch in x)
    and not x[0].isdigit()
    and len(x) >= 5
)
text="hello worl5s star1 fre2 pyth0n"
print(words(text))

#11
def common_unique_chars(s1,s2):
    result = ""
    for ch in s1:
        if (
            ch in s2
            and ch not in result
            and not ch.isdigit()
            and ch != " "
        ):
            result += ch
    return result
print(common_unique_chars("hello worl5s", "abs c1a5d"))
