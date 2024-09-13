def all_variants(text):
    substrings = []
    add_substring = lambda x: substrings.append(x) if x else None
    for i, _ in enumerate(text):
        for j, _ in enumerate(text):
            add_substring(text[i: j + 1])
    substrings.sort(key=len)

    for substring in substrings:
        yield substring



a = all_variants("abc")
for i in a:
    print(i)