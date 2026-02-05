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


# 1
def analyze_text(text):
    vowels = "аеиоуыэюяaeiouy"
    uniq_vowels = []
    words = []
    word = ""

    for x in text.lower():
        if x.isalpha():
            word += x
        else:
            if word != "":
                for c in word:
                    if c in vowels and c not in uniq_vowels:
                        uniq_vowels.append(c)
                if len(word) >= 5 and word[0] == word[-1] and word not in words:
                    words.append(word)
            word = ""
    if word != "":
        for c in word:
            if c in vowels and c not in uniq_vowels:
                uniq_vowels.append(c)
        if len(word) >= 5 and word[0] == word[-1] and word not in words:
            words.append(word)

    return (len(uniq_vowels), " ".join(words))


text = input("Введите текст:")
print(analyze_text(text))

#2
process = lambda s: " ".join(
    filter(lambda word: len(word) % 2==0,
           map( lambda word: word[::-1],
                filter(lambda word: not any( x.isdigit() for x in word),
                        s.split()
                )
           )
    )
)
print(process("hello anel sa33 level even"))
