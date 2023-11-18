from flask import Flask, request
import requests
from env_vars.config import ACCESS_TOKEN, BOT_EMAIL
import json

app = Flask(__name__)

headers = {
    "Authorization": f"Bearer {ACCESS_TOKEN}",
    "Content-Type": "application/json"
}


def send_message(room_id, message):
    url = "https://api-usgov.webex.com/v1/messages"
    data = {"roomId": room_id, "text": message}
    requests.post(url, headers=headers, data=json.dumps(data))


@app.route("/", methods=['POST'])
def webhook():
    json_data = request.json
    room_id = json_data['data']['roomId']
    message_id = json_data['data']['id']
    get_message_url = f"https://api-usgov.webex.com/v1/messages/{message_id}"
    message_data = requests.get(get_message_url, headers=headers).json()

    if 'personEmail' in message_data.keys() and message_data['personEmail'] == BOT_EMAIL:
        return "Message from bot, ignoring", 200

    send_message(room_id, "Hello! You said: " + message_data['text'])
    return "Message sent", 200


if __name__ == "__main__":
    app.run(debug=True)
