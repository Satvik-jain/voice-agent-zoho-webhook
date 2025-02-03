from flask import Flask, request, jsonify
from fetch_data_from_zoho import fetch_data_from_zoho

app = Flask(__name__)

@app.route("/retell", methods=["POST"])
def retell_custom_function():
    data = request.get_json()
    args = data.get("args", {})

    response = fetch_data_from_zoho(args)
    
    return jsonify({"result": response})

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
