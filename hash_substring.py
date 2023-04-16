#221RDB489 Rinalds Dobelis 16.grupa
def read_input():
    choose = input().strip()
    if choose == "F":
        with open("tests/06") as file:
            pattern = file.readline().strip()
            text = file.readline().strip()
    if choose == "I":
        pattern = input().strip()
        text = input().strip()

    return pattern, text


def print_occurrences(output):
    print(" ".join(str(x) for x in output))


def get_occurrences(pattern, text):
    p = 1000000007
    x = 1
    occurrences = []

    pattern_hash = 0
    for i in range(len(pattern)):
        pattern_hash = (pattern_hash + ord(pattern[i]) * x) % p
        x = (x * 263) % p

    n = len(text)
    m = len(pattern)

    if n < m:
        return []

    hash_values = [0] * (n - m + 1)
    hash_values[-1] = hash(text[n - m :])
    x = 1
    for i in range(m):
        x = (x * 263) % p

    for i in range(n - m - 1, -1, -1):
        hash_values[i] = (263 * hash_values[i + 1] + ord(text[i]) - x * ord(text[i + m])) % p

    for i in range(n - m + 1):
        if pattern_hash == hash_values[i] and text[i : i + m] == pattern:
            occurrences.append(i)

    return occurrences


if __name__ == "__main__":
    print_occurrences(get_occurrences(*read_input()))
