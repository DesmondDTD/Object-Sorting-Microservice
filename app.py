from flask import Flask, request, jsonify
import re

app = Flask(__name__)

def parse_value(value):
    """Convert numerical values (even with symbols like $) to float for sorting."""
    try:
        return float(re.sub(r'[^0-9.]', '', value))
    except ValueError:
        return value  # Return as string if conversion fails

@app.route('/sort', methods=['POST'])
def sort_data():
    try:
        data = request.json.get('data', [])
        key = request.json.get('key')
        order = request.json.get('order', 'asc').lower()

        if not data or not key:
            return jsonify({"error": "Missing required 'data' or 'key' parameters."}), 400

        if key not in data[0]:
            return jsonify({"error": f"Key '{key}' not found in dataset."}), 400

        sorted_data = sorted(data, key=lambda x: parse_value(x[key]), reverse=(order == 'desc'))
        return jsonify({"sorted_data": sorted_data, "index": list(range(1, len(sorted_data) + 1))})

    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True)
