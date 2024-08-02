from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample user details (static for this example)
USER_DETAILS = {
    "user_id": "john_doe_17091999",
    "email": "john@xyz.com",
    "roll_number": "ABCD123"
}

@app.route('/bfhl', methods=['POST'])
def handle_post():
    if not request.json or 'data' not in request.json:
        return jsonify({'is_success': False, 'message': 'Invalid request'}), 400

    data = request.json['data']

    if not isinstance(data, list):
        return jsonify({'is_success': False, 'message': 'Data should be a list'}), 400

    numbers = [item for item in data if item.isdigit()]
    alphabets = [item for item in data if item.isalpha()]

    highest_alphabet = []
    if alphabets:
        highest_alphabet = [max(alphabets, key=lambda x: x.upper())]

    response = {
        'is_success': True,
        'user_id': USER_DETAILS['user_id'],
        'email': USER_DETAILS['email'],
        'roll_number': USER_DETAILS['roll_number'],
        'numbers': numbers,
        'alphabets': alphabets,
        'highest_alphabet': highest_alphabet
    }

    return jsonify(response)

@app.route('/bfhl', methods=['GET'])
def handle_get():
    return jsonify({'operation_code': 1})

if __name__ == '__main__':
    app.run(debug=True)
