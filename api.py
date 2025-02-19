from flask import Flask, request, jsonify
import sys
import os

sys.path.append(os.path.abspath("./model-serving"))
sys.path.append(os.path.abspath("./model-training"))
sys.path.append(os.path.abspath("./data-processing"))
sys.path.append(os.path.abspath("./visualisation"))
sys.path.append(os.path.abspath("./experiments"))
sys.path.append(os.path.abspath("./deployment"))
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")

from model_serving.script.evaluate import evaluate_model, load_preprocessed_model
from model_serving.script.generate import generate_and_save_model
from model_training.script.train import train_model

app = Flask(__name__)

@app.route("/generate", methods=["POST"])
def generate():
    data = request.json
    num_models = data.get("num_models", 1)
    is_2d = data.get("is_2d", False)

    try:
        generate_and_save_model(num_models=num_models, is_2d=is_2d)
        return jsonify({"message": "Modèles générés avec succès."}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/evaluate", methods=["POST"])
def evaluate():
    data = request.json
    model_path = data.get("model_path")
    ground_truth_path = data.get("ground_truth_path")

    try:
        model = load_preprocessed_model(model_path)
        ground_truth = load_preprocessed_model(ground_truth_path)
        result = evaluate_model(model, ground_truth)
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
