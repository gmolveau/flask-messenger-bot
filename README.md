# Flask boilerplate facebook messenger bot

```bash
git clone https://github.com/gmolveau/flask-messenger-bot
cd flask-messenger-bot
virtualenv venv -p python3
source venv/bin/activate
pip3 install -r requirements.txt
gunicorn app:app
```

## How to create a (private) facebook messenger bot

First of all you need a facebook account, logged in.

1. Create a new FB App [here](https://developers.facebook.com/quickstarts/?platform=web), just type in the name of your app (choose wisely, difficult to change afterwards), your contact mail and a captcha. Then click on "pass everything" on the top right.

2. Create a new FB Page [here](https://www.facebook.com/pages/create), choose a category, a name (there's a special naming convention. choose wisely, also difficult to change afterwards).

3. Go back to your app and click on "configure" on the messenger's tab.

4. In the "token generation" section, select the page you create earlier to generate an ACCESS_TOKEN. Keep it somewhere, as it will be used as an environment variable later.

	(it's a big string like : EAACrKioFH4oBAM89bjAPrFmY[...])

5. Create a VERIFY_TOKEN [with uuid](https://www.uuidgenerator.net/version4), keep it somewhere, it will be used as an environment variable later. (for example : b030bde8-bd27-419d-a0b3-[...])

6. Deploy your app. You will need a HTTPS url. Heroku provides free plans to host an app, and it should work out of the box.

	[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

	> You can choose a more suitable name if you want than the generated one by heroku.

7. Click 'Setup Webhooks' back in the Facebook Developers page (still in the Messenger tab). Paste the callback URL wihch should be something like `https://your_super_flask_app.herokuapp.com/webhook`, and paste your VERIFY_TOKEN created earlier.

Check at least the 'messages' box in Subscription Fields, others are optional for the moment.

8. Verify and Save

9. If you did it correctly, your page should respond correctly. You app is now accessible only for you. If you want to make it public, read the next section `submit your app` ;)

## How to make your messenger bot public (submit your app)


1. You will need :
	* a 1024x1024 png icon for your app
	* a facebook cover (optional)
	* a facebook profile picture (optional)
	* a on-hand recorded video of the bot in action
2. todo [...]
