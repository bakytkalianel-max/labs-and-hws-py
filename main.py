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


# 3
def top_k_words(text, k):
    text = text.lower()

    cleaned = ""
    for x in text:
        if x.isalpha() or x == " ":
            cleaned += x
    words = cleaned.split()

    freq = []
    for w in words:
        found = False
        for item in freq:
            if item[0] == w:
                item[1] += 1
                found = True
                break
        if not found:
            freq.append([w, 1])
    n = len(freq)
    for i in range(n):
        for j in range(0, n - i - 1):
            if freq[j][1] < freq[j + 1][1]:
                freq[j], freq[j + 1] = freq[j + 1], freq[j]
            elif freq[j][1] == freq[j + 1][1]:
                if freq[j][0] > freq[j + 1][0]:
                    freq[j], freq[j + 1] = freq[j + 1], freq[j]
    result = []
    for i in range(min(k, len(freq))):
        result.append(freq[i][0])
    return result


print(top_k_words(" hello apple hello1 banana apple hello", 2))

#4
x=lambda s: " ".join(
    word.lower()
    for word in s.split()
    if sum(c.isupper() for c in word) == 1
    and not word[0].isupper()
    and not word[-1].isupper()
)
text=" word wOrd run hello file"
print(x(text))

#5
def compress_text(text):
    if not text:
        return ""

    result=""
    count=1
    for i in range(1,len(text)):
        if text[i].lower() == text[i-1].lower():
            count += 1
        else:
            if count > 1:
                result += text[i-1] +str(count)
            else:
                result += text[i-1]
            count = 1
    if count > 1:
        result += text[-1] + str(count)
    else:
        result += text[-1]
    return result

#6
x= lambda s: [
    d for d in s.split()
    if len(d) >= 4
    and not any(ch.isdigit() for ch in d)
    and len(set(d.lower())) == len(d)
]
a= " abcde anel hello world"
print(x(a))

print(compress_text("aaBBcDDD"))