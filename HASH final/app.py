from flask import Flask, render_template, request

app = Flask(__name__)

# Hash table initialization
hash_table = [[] for _ in range(32)]

# Hash functions
def hash_function_1(key):
    return key % 32

def hash_function_2(key):
    return ((1731 * key + 520123) % 524287) % 32

# Default Python hash function (hash function 3)
def hash_function_3(key):
    return hash(key) % 32


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/process', methods=['POST'])
def process():
    global hash_table  

    selected_hash_function = request.form.get('hash_function')
    num_commands = int(request.form.get('num_commands'))
    commands = request.form.get('commands').split('\n')

    
    hash_table = [[] for _ in range(32)]

    
    def insert_into_hash_table(word):
        word = word.strip()  
        key = sum(ord(char) for char in word)
        if selected_hash_function == 'Hash Function 1':
            index = hash_function_1(key)
        elif selected_hash_function == 'Hash Function 2':
            index = hash_function_2(key)
        else:
            index = hash_function_3(key)

        hash_table[index].insert(0, word)

   
    def delete_from_hash_table(word):
        word = word.strip()  
        key = sum(ord(char) for char in word)
        if selected_hash_function == 'Hash Function 1':
            index = hash_function_1(key)
        elif selected_hash_function == 'Hash Function 2':
            index = hash_function_2(key)
        else:
            index = hash_function_3(key)

        if word in hash_table[index]:
            hash_table[index].remove(word)

    
    for command in commands:
        if command.startswith('del '):
            delete_from_hash_table(command[4:])
        else:
            insert_into_hash_table(command)

    
    return render_template('index.html', hash_table=hash_table)


@app.route('/output')
def output():
    return render_template('output.html', hash_table=hash_table)


if __name__ == '__main__':
    app.run(debug=True)
