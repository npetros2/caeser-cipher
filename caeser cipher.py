# Caesar encryption/decryption

### Returns string which contains only letters
def input_phrase():
    phrase = ' '
    while not phrase.isalpha():
        phrase = input('Enter the text: ')
        if not phrase.isalpha():
            print('Phrase contains non-letter symbols. Please try again.')
    return phrase

### Returns integer key in range of (0..25)
def input_key():
    keys = range(26)
    key = 26
    while key not in keys:
        try:
            key = int(input('Enter the key value (0..25): '))
            if key not in keys:
                print('Key is not in (0..25). Please try again.')
        except ValueError:
            print("That's isn't an integer, try again!")
            key = 26
    return key

### Returns a 'char' encoded with 'key'
def encoded(char, key):
    return chr(ord('a') + (ord(char) - ord('a') + key) % 26)

### Returns a 'phrase' encoded with 'key'
def translate(phrase, key):
    return ''.join([encoded(char, key) for char in phrase])

### Encryption function
def encrypt(phrase, key):
    return translate(phrase, key)

### Decryption function
def decrypt(phrase, key):
    return translate(phrase, -key)

def main():
    cmds = {'e': encrypt, 'd': decrypt}
    cmd = ''
    while cmd not in cmds:
        cmd = input('Do you wish to (e)ncrypt or (d)ecrypt a cipher? ')
        cmd = cmd.lower()
        if cmd not in cmds:
            print('Invalid selection, please try again.')

    phrase_type = 'plain' if cmd == 'e' else 'cipher'
    phrase, key = input_phrase().lower(), input_key()
    result = cmds[cmd](phrase, key)
    print(result)
    input()

if __name__ == '__main__':
    main()
