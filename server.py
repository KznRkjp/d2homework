import os
import sentry_sdk
from bottle import Bottle, request
from sentry_sdk.integrations.bottle import BottleIntegration

#Достаем строку с ключом sentry из переменнных heroku
#не забываем прописать в heroku APP_LOCATION!
DSN = os.environ.get("DSN")

#меню по умолчанию
MENU =  "<a href=\"../success\">Успех</a><br><a href=\"../fail\">Провал</a>"

sentry_sdk.init(
    dsn=DSN,
    integrations=[BottleIntegration()]
)


app = Bottle()

@app.route('/')
def index():
    return MENU

@app.route('/success')
def index():
    return MENU

@app.route('/fail')
def index():
    raise RuntimeError("There is an error!")
    return


if os.environ.get("APP_LOCATION") == "heroku":
    app.run(host="0.0.0.0", port = int(os.environ.get("PORT", 5000)), debug=False)
else:
    app.run(host="localhost", port=8080, debug=True)
