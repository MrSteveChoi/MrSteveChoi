def caesar_cipher():
    n = int(input('input caesar num: ')) % 26
    input_text = input('input text: ')
    
    result = ''
    for i in input_text:
        if i.isupper():
            if ord(i) + n > 90:
                result += chr((ord(i) + n) - 90 + 64)
            else:
                result += chr(ord(i) + n)
                
        elif i.islower():
            i = i.upper()
            print(i)
            if ord(i) + n > 90:
                result += chr((ord(i) + n) - 90 + 64).lower()
            else:
                result += chr(ord(i) + n).lower()
        else:
            result += i
    return result

if __name__ == '__main__':
    print(ceasar_cipher())
