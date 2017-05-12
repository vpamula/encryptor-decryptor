original_alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u' 'v', 'w', 'x', 'y', 'z']

def valid(key):
    for i in key:
        if i is type(int):
            return False
        else:
            return True

def flatten(data):
    return [item for branch in data for item in branch]

def remove_duplicates(data):
    if data == []:
        return data
    elif data[0] in data[1:]:
        return remove_duplicates(data[1:])
    else:
        return flatten([data[0], remove_duplicates(data[1:])])

def create_ciphertext(key):
    jash = original_alphabet[:]
    for i in key:
        jash.append(i)
    y = remove_duplicates(jash)
    return y

def encryptor(phrase, key):
    result = []
    cipher = create_ciphertext(key)
    for each in phrase:
        for i in range(0, len(original_alphabet)):
            if original_alphabet[i] == each:
                result.append(cipher[i])
    return " ".join(str(x) for x in result)

def decryptor(phrase, key):
    result = []
    cipher = original_alphabet[:]
    decrypt_text = create_ciphertext(key)
    for each in phrase:
        for i in range(0, len(decrypt_text)):
            if decrypt_text[i] == each:
                result.append(decrypt_text[i])
    return " ".join(str(x) for x in result)


print(encryptor('more chune for ya head top so watch how you speak on my name you know', 'goat'))
print(decryptor('more chune for ya head top so watch how you speak on my name you know', 'goat'))
