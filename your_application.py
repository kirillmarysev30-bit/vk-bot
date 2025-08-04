from flask import Flask, request
import vk_api
import json
import os

app = Flask(__name__)

TOKEN = "vk1.a.FU73i4lWQ9cL8TtEtKtjtkpqyPQkNOj-2W6mfOLFcd4m9wpDT0iEvNlNXEeKtQKO_dprKZcGSp46pTBxHd6dFJKOSs_jExTImdotxmLufnsDkfN20ARFb18dt5uPfGG_hRMQFkQRx6EBa_9FfArkbhkNYD2-6a4kh9PQ0Kdw57RRvsFcrDpCKmQNFer_l3R-Gj6vyGqEqYn0V--9sWKJMA"
CONFIRMATION_CODE = "d35e0a1dfa89d2009be6e0d85fa2a68e9fe9179e"

vk_session = vk_api.VkApi(token=TOKEN)
vk = vk_session.get_api()

@app.route('/', methods=['POST'])
def vk_bot():
    data = json.loads(request.data)

    if 'type' in data:
        if data['type'] == 'confirmation':
            return CONFIRMATION_CODE
        elif data['type'] == 'message_new':
            user_id = data['object']['message']['from_id']
            message = data['object']['message']['text']

            vk.messages.send(
                user_id=user_id,
                message=f"Вы написали: {message}",
                random_id=0
            )

    return 'ok'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)

