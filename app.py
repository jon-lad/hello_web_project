import os
from flask import Flask, request

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==

@app.route('/count_vowels', methods=['POST'])
def count_vowels():
    text = request.form["text"]
    vowels = ('a','e', 'i', 'o', 'u')
    vowels_in_text = [char for char in text if char in vowels]
    return f'There are {len(vowels_in_text)} vowels in "{text}"'

@app.route('/sort-names', methods=["POST"])
def sort_names():
    names = request.form['names'].split(',')
    return ",".join(sorted(names))

@app.route('/names', methods=["GET"])
def add_name():
    names = request.args['add'].split(',')
    name_list = ['Julia', 'Alice', 'Karim'] + names
    return ", ".join(sorted(name_list))



# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))

