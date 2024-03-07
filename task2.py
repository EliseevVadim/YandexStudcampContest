def is_palindrome(s):
    return s == s[::-1]


def find_palindrome_pairs(lines):
    palindrome_pairs = []
    string_indices = {s: i for i, s in enumerate(lines)}

    for i, line in enumerate(lines):
        reversed_string = line[::-1]
        if reversed_string in string_indices and string_indices[reversed_string] != i:
            palindrome_pairs.append((i, string_indices[reversed_string]))

        for j in range(1, len(line)):
            prefix, suffix = line[:j], line[j:]
            if is_palindrome(prefix) and suffix[::-1] in string_indices:
                palindrome_pairs.append((string_indices[suffix[::-1]], i))
            if is_palindrome(suffix) and prefix[::-1] in string_indices:
                palindrome_pairs.append((i, string_indices[prefix[::-1]]))

    return palindrome_pairs


n = int(input())
strings = []

for _ in range(n):
    strings.append(input())

pairs = find_palindrome_pairs(strings)
sorted_pairs = sorted(pairs, key=lambda x: x[0])

for pair in sorted_pairs:
    print(pair[0] + 1, pair[1] + 1)
