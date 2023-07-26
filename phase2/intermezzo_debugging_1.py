# def say_hello(name):
#     return f"hello {name}"


# # Intended output:
# #
# # > say_hello("kay")
# # => "hello kay"

# def encode(text, key):
#     cipher = make_cipher(key)

#     ciphertext_chars = []
#     for i in text:
#         ciphered_char = chr(65 + cipher.index(i))
#         print(f'This is ciphered_ char \n{ciphered_char} \n')
#         ciphertext_chars.append(ciphered_char)

#     return "".join(ciphertext_chars)


# def decode(encrypted, key):
#     cipher = make_cipher(key)

#     plaintext_chars = []
#     for i in encrypted:
#         plain_char = cipher[ord(i) - 65]
#         print(f'This is plain_char \n {plain_char} \n')
#         plaintext_chars.append(plain_char)

#     return "".join(plaintext_chars)


# def make_cipher(key):
#     alphabet = [chr(i + 97) for i in range(0, 26)]
#     print(f'This is alphabet \n {alphabet} \n')
#     cipher_with_duplicates = list(key) + alphabet

#     cipher = []
#     for i in range(0, len(cipher_with_duplicates)):
#         if cipher_with_duplicates[i] not in cipher_with_duplicates[:i]:
#             cipher.append(cipher_with_duplicates[i])

#     return cipher

# # When you run this file, these next lines will show you the expected
# # and actual outputs of the functions above.
# print(f"""
#  Running: encode("theswiftfoxjumpedoverthelazydog", "secretkey")
# Expected: EMBAXNKEKSYOVQTBJSWBDEMBPHZGJSL
#   Actual: {encode('theswiftfoxjumpedoverthelazydog', 'secretkey')}
# """)

# print(f"""
#  Running: decode("EMBAXNKEKSYOVQTBJSWBDEMBPHZGJSL", "secretkey")
# Expected: theswiftfoxjumpedoverthelazydog
#   Actual: {decode('EMBAXNKEKSYOVQTBJSWBDEMBPHZGJSL', 'secretkey')}
# """)


def get_most_common_letter(text):
    print(f'Input starts as: \n {text}\n')
    counter = {}
    for char in text.replace(' ', ''):
        print(f'Loop iteration starts')
        print(f'Counter starts as: \n {counter}\n')
        
        counter[char] = counter.get(char, 0) + 1
        print(f'Counter[char] = {char} starts as: {counter[char]} ')
    letter = sorted(counter.items(), key=lambda item: item[1], reverse = True)[0][0]
    print(f'Sorted letter list: \n {sorted(counter.items(), key=lambda item: item[1], reverse = True)}')
    print(f'Letter is: \n {letter} \n The type of Letter is {type(letter)}')
    return letter


print(f"""
Running:  get_most_common_letter("the roof, the roof, the roof is on fire!"))
Expected: o
Actual:   {get_most_common_letter("the roof, the roof, the roof is on fire!")}
""")

'''
We are going to avoid the space character as it is not a letter
We are also going to ensure that the key representing the letter
is being returned, rather than the value representing the count
'''