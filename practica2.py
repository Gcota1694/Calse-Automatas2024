import json

def read_file(file_to_read):
    with open(file_to_read, 'r') as file:
        content = file.read()
        return content

def tokenize_content(file):
    tokens = []
    for character in file:
        if character == '\n':
            tokens.append('[Enter]')
        elif character == ' ':
            tokens.append('[SPACE]')
        else:
            tokens.append(ord(character))
    return tokens

def show_content_tokens(file, tokens):
    for i, character in enumerate(file):
        if tokens[i] == '\n':
            print(f'{tokens[i]}=[Enter]')
        elif tokens[i] == ' ':
            print(f'{tokens[i]}=[SPACE]')
        else:
            print(f'{tokens[i]}={character}')

def write_document(file, tokens):
    with open('salida.txt', 'w') as output:
        for i, character in enumerate(file):
            if tokens[i] == '\n':
                output.write(f'{tokens[i]}=[ENTER]\n')
            elif tokens[i] == ' ':
                output.write(f'{tokens[i]}=[SPACE]\n')
            else:
                output.write(f'{tokens[i]}={character}\n')

def is_json(content):
    try:
        json.loads(content)
        return True
    except ValueError:
        print('no es archivo json')
        exit()

def tokenize_string(array):
    tokens = []
    agrupados = False
    for value in array:
        if (48 <= value <= 57) or (value == 91) or (value == 93) or (value == 123) or (value == 125):
            if not agrupados:
                tokens.append(200)
                agrupados = True
            else:
                agrupados = False
                tokens.append(value)
        else:
            agrupados = False
            tokens.append(value)
    return tokens

def is_string(array):
    flag = True
    for value in array:
        if value == 34:
            flag = not flag
    if flag == False:
        print("ERROR: las comillas no se cerraron")
        exit()

def main():
    file = read_file('json_example.json')
    is_json(file)
    tokens = tokenize_content(file)
    print(tokens)
    group_string = tokenize_string(tokens)
    show_content_tokens(file, tokens)
    write_document(file, tokens)
    print(tokens)
    print(group_string)
    print(is_string(tokens))

if __name__ == '__main__':
    main()