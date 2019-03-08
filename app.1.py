from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

LINE_CHANNEL_ACCESS_TOKEN = "97AwvIwOhsrOlcXmjLpqJgaI6SzeJCpwkgi4S4VhVc2Pgw0lpV1I1CBLDDiMHAZDb+PCK40DKBmdQAfVv5LI1hcC3V3yJEFrzTro1yZBYrQ3G5hkkw/chNYFEbbJMameCQnnRLnYLBigLEUkMl3CdQdB04t89/1O/w1cDnyilFU="
LINE_CHANNEL_SECRET = "853cd587ae9045687ca5c8f80a0e606b"

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    print("signature:",signature)
    exit()

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))


if __name__ == "__main__":
    app.debug = True
    app.run()