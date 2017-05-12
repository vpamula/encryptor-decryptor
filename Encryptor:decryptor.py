original_alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u' 'v', 'w', 'x', 'y', 'z']

def valid(key):
    for i in key:
        if i is type(int):
            return False
        else:
            return True

def remove_duplicates(data):
    if data = []:
        return data
    elif data[0] is in data[1:]:
        return remove_duplicates(data[1:])
    else:
        return [data[0]].extend(remove_duplicates(data[1:]))

def create_ciphertext(key):
    jash = original_alphabet[:]
    for i in key:
        jash.extend(i)
    jash = remove_duplicates(jash)
    return jash

def encryptor(phrase, key):
    result = []
    cipher = create_ciphertext(key)
    for each in phrase:
        for i in range(0, len(original_alphabet)):
            if original_item[i] = each:
                result += cipher[i]
    return " ".join(str(x) for x in result)

def decryptor(phrase, key):
    result = []
    cipher = original_alphabet[:]
    for each in phrase:
        for i in range(0, len(create_ciphertext(key))):
            if create_ciphertext(key)[i] = item:
                result += cipher[i]
    return " ".join(str(x) for x in result)
