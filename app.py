from flask import Flask, request, Response
import requests, json, random, os
app = Flask(__name__)

# env_variables
# token to verify that this bot is legit
verify_token = os.getenv('VERIFY_TOKEN', None)
# token to send messages through facebook messenger
access_token = os.getenv('ACCESS_TOKEN', None)

@app.route('/webhook', methods=['GET'])
def webhook_verify():
    if request.args.get('hub.verify_token') == verify_token:
        return request.args.get('hub.challenge')
    return "Wrong verify token"

@app.route('/webhook', methods=['POST'])
def webhook_action():
    data = json.loads(request.data)
    for entry in data['entry']:
        user_message = entry['messaging'][0]['message']['text']
        user_id = entry['messaging'][0]['sender']['id']
        response = {
            'recipient': {'id': user_id},
            'message': {}
        }
        response['message']['text'] = handle_message(user_id, user_message)
        r = requests.post(
            'https://graph.facebook.com/v2.6/me/messages/?access_token=' + access_token, json=response)
    return Response(response="EVENT RECEIVED",status=200)

@app.route('/webhook_dev', methods=['POST'])
def webhook_dev():
    # custom route for local development
    data = json.loads(request.data)
    user_message = data['entry']['messaging'][0]['message']['text']
    user_id = data['entry']['messaging'][0]['sender']['id']
    response = {
        'recipient': {'id': user_id},
        'message': {}
    }
    response['message']['text'] = handle_message(user_id, user_message)
    return Response(
        response=json.dumps(response),
        status=200,
        mimetype='application/json'
    )

def handle_message(id, message):
    # DO SOMETHING with the user_message ... ¯\_(ツ)_/¯
    return "Hello World ! You just sent me : " + message

@app.route('/privacy', methods=['GET'])
def privacy():
    # needed route if you need to make your bot public
    return "This facebook messenger bot's only purpose is to [...]. That's all. We don't use it in any other way."

@app.route('/', methods=['GET'])
def index():
    return "Hello there, I'm a facebook messenger bot."


if __name__ == '__main__':
    if verify_token is None:
        print("VERIFY_TOKEN env variable is not set ...")
        os._exit(1)
    if access_token is None:
        print("ACCESS_TOKEN env variable is not set ...")
        os._exit(1)
    app.run(debug=True, host='0.0.0.0')
