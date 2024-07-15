from flask import Flask, request, jsonify
from LLM_Model import *
app = Flask(__name__)

@app.route('/add', methods=['POST'])
def Call_Model():
    data = request.json
    prompt = data.get('prompt')
    category = data.get('category')
    response = Llama_output(prompt, category=category)
    return jsonify({"response": response})

if __name__ == '__main__':

    app.run(debug=True)
