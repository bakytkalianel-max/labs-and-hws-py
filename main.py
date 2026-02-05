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

#7
def palindrome_words(text):
    cleaned=""
    for ch in text:
        if ch.isalpha() or ch == " ":
            cleaned += ch
    words = cleaned.lower().split()
    palindromes=[]
    for x in words:
        if len(x) > 3 and x == x[::-1] and x not in palindromes:
            palindromes.append(x)
    palindromes.sort()
    palindromes.sort(key = len,reverse=True)

    return palindromes
print(palindrome_words(" level hello text edit abba"))

#8
x= lambda s: " ".join(
    f if any(ch.isdigit() for ch in f)
    else "VOWEL" if f[0].lower() in "aeiou"
    else "CONSONANT"
    for f in s.split()
)
a=" anel text leve1 sp1it "
print(x(a))

#9
def alternate_case_blocks(text, n):
    result = ""
    a=0
    for i in range(0, len(text), n):
        block=text[i:i+n]

        if a % 2 ==0:
            result += block.upper()
        else:
            result += block.lower()

        a += 1
    return result.replace(" ","")
print(alternate_case_blocks("Hello world Help",2))

#12
words1 = lambda s: [
    x for x in s.split()
    if len(x) >3
       and x[0].lower() == x[-1].lower()
       and x.lower() != x.lower()[::-1]
]
a="anea level aba adfah sahfs"
print(words1(a))

#13
def replace_every_nth(text, n, char):
    if n <= 0:
        return text
    soans = []
    i=0
    while i <len(text):
        if text[i] != " ":
            start = i
            while i < len(text) and text[i] != " ":
                i += 1
            end = i
            spans.append((start,end))
        else:
            i += 1
    short_idx = set()
    for start,end in spans:
        if end - start <3:
            for k in range(start,end):
                short_idx.add(k)
    chars= list(text)
    for idx, ch in enumerate(chars):
        pos = idx +1
        if pos % n == 0:
            if ch != " " and not ch.isdigit() and idx not in short_idx:
                chars[idx] = chars
    return "".join(chars)
print(replace_every_nth("Hello world Help",2," "))