# Create a function to safely open and read a file

# Include proper error handling and resource cleanup
def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except IOError as e:
        print(f"IOError: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Create a Flask API endpoint that:

# - Accepts POST requests with JSON data

# - Validates the input has 'username' and 'email' fields

# - Returns a 400 error if validation fails

# - Returns a 200 success if validation passes
from flask import Flask, request, jsonify
app = Flask(__name__)
@app.route('/api/user', methods=['POST'])
def validate_user():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid JSON"}), 400
    if 'username' not in data or 'email' not in data:
        return jsonify({"error": "Missing 'username' or 'email' field"}), 400
    # Additional validation can be added here (e.g., email format)
    return jsonify({"message": "User data is valid"}), 200  

if __name__ == '__main__':
    app.run(debug=True)