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
    pattern_len = len(pattern)
    text_len = len(text)
    d = 256
    q = 1000000007
    h = pow(d, pattern_len-1) % q

    pattern_hash = sum(ord(pattern[i]) * pow(d, pattern_len - i - 1, q) % q for i in range(pattern_len)) % q
    text_hash = sum(ord(text[i]) * pow(d, pattern_len - i - 1, q ) % q for i in range(pattern_len)) % q
    occurrences = []

    for i in range(text_len - pattern_len + 1):
        if pattern_hash == text_hash and pattern == text[i : i + pattern_len]:
            occurrences.append(i)
        if i < text_len - pattern_len:
            text_hash = (d * (text_hash - ord(text[i]) * h) + ord(text[i+pattern_len])) % q
    return occurrences



if __name__ == "__main__":
    print_occurrences(get_occurrences(*read_input()))
