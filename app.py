from flask import Flask, request, jsonify, send_from_directory
from services.openai_client import get_completion
from services.storage import load_conversations, save_conversation
import os

app = Flask(__name__, static_folder='public')


@app.post('/webhook')
def webhook():
    data = request.get_json(force=True)
    user = data.get('from')
    message = data.get('message')
    if not user or not message:
        return jsonify({'error': 'Formato invalido'}), 400
    try:
        reply = get_completion(message)
        conv = save_conversation(user, message, reply)
        return jsonify({'reply': reply, 'conv': conv})
    except Exception as e:
        print(e)
        return jsonify({'error': 'Error procesando mensaje'}), 500


@app.get('/dashboard')
def dashboard():
    return send_from_directory(app.static_folder, 'dashboard.html')


@app.get('/api/conversations')
def api_conversations():
    return jsonify(load_conversations())


if __name__ == '__main__':
    port = int(os.getenv('PORT', 3000))
    app.run(host='0.0.0.0', port=port)
