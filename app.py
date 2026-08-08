from flask import Flask, jsonify, request
import math

app = Flask(__name__)
app.json.ensure_ascii = False


@app.route("/")
def home():
    return "Hello World"


@app.route("/score")
def calculate_score():
    score_str = request.args.get("score")

    # Rule 1: score phải được cung cấp
    if score_str is None:
        return jsonify({"error": "Score parameter is required"}), 400

    # Rule 2: score không được rỗng
    if score_str.strip() == "":
        return jsonify({"error": "Score cannot be empty"}), 400

    # Rule 3: score phải là số
    try:
        score = float(score_str)
    except ValueError:
        return jsonify({"error": "Score must be a valid number"}), 400

    # Rule 3.5: Reject NaN và Infinity
    if math.isnan(score) or math.isinf(score):
        return jsonify({"error": "Score must be a valid number"}), 400

    # Rule 4: score phải nằm trong khoảng 0 đến 10
    if score < 0 or score > 10:
        return jsonify({"error": "Score must be between 0 and 10"}), 400

    # Quy tắc xếp loại
    if score < 5:
        classification = "Yếu"
    elif score < 6.5:
        classification = "Trung bình"
    elif score < 8:
        classification = "Khá"
    else:
        classification = "Giỏi"

    return jsonify({
        "score": score,
        "classification": classification
    }), 200


if __name__ == "__main__":
    app.run(debug=True)