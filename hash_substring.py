def read_input():
    input_type = input().strip().upper()
    if input_type == 'F':
        with open('tests/06', 'r') as f:
            pattern = f.readline().strip()
            text = f.readline().strip()
    if input_type == "I":
        pattern = input().strip()
        text = input().strip()
    return pattern, text


def print_occurrences(output):
    print(' '.join(map(str, output)))


def get_occurrences(pattern, text):
    p = 10**9 + 7
    x = 263
    pattern_hash = sum(ord(pattern[i]) * pow(x, i, p) for i in range(len(pattern))) % p
    n = len(text)
    m = len(pattern)
    hashes = [None] * (n - m + 1)
    hashes[n - m] = sum(ord(text[i]) * pow(x, i, p) for i in range(n - m, n)) % p
    factor = pow(x, m - 1, p)
    for i in range(n - m - 1, -1, -1):
        hashes[i] = (x * hashes[i + 1] + ord(text[i]) - factor * ord(text[i + m])) % p
    return [i for i in range(n - m + 1) if hashes[i] == pattern_hash]


if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))
