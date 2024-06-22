from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

API_KEY = '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'  # আপনার API Key

@app.route('/api', methods=['GET'])
def get_answer():
    question = request.args.get('question')
    if not question:
        return jsonify({'error': 'Question parameter is required'}), 400
    
    try:
        response = requests.post(
            'https://api.openai.com/v1/engines/davinci-codex/completions',
            headers={
                'Authorization': f'Bearer {API_KEY}',
                'Content-Type': 'application/json'
            },
            json={
                'prompt': question,
                'max_tokens': 100
            }
        )
        response_data = response.json()
        answer = response_data['choices'][0]['text'].strip()
        return jsonify({'question': question, 'answer': answer})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
