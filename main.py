from icecream import ic

def main():
    path = "books/frankenstein.txt"
    with open(path) as f:
        file_contents = f.read()
        words = file_contents.split()
        chars = char_num_in_text(words)
        # ic(chars)
        chars = dict(sorted(chars.items(), key=lambda item:item[1], reverse=True))
    print(f"""--- Begin report of {path} ---
{len(words)} words found in the document\n""")
    for entry in chars:
        if entry.isalpha():
            print(f"The '{entry}' character was found {chars[entry]} times")
    print("--- End report ---")

def char_num_in_text(words):
    output = {}
    for word in words:
        word1 = word.lower()
        for char in word1:
            if char not in output:
                output[char] = 0
            output[char] += 1
    return output


def sort_on(chars):
    return chars["num"]

if __name__ == '__main__':
    main()