import sentry_sdk
from bottle import Bottle, request
from sentry_sdk.integrations.bottle import BottleIntegration

sentry_sdk.init(
    dsn="https://1f307140b37e44c7988c75f6c4e8abbf@sentry.io/1433178",
    integrations=[BottleIntegration()]
)

MENU =  "<a href=\"../success\">Успех</a><br><a href=\"../fail\">Провал</a>"


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


app.run(host='localhost', port=8080)
