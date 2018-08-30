from flask import Flask

#-------------------------------------------------------
#Setup flask
app = Flask(__name__)
PORT = 8000
DEBUG = True

@app.errorhandler(404)
def not_found(error):
    return "Not Found."


#-------------------------------------------------------
#init
@app.route('/', methods=['POST','GET'])
def init():
    print('With flask4')
    return 'App connections with: 1. /webhookasana: To connect asana to todoist /// 2. /webhooktodoist: To connect Todoist to asana'







#-------------------------------------------------------
if __name__ == '__main__':
    app.run(port = PORT, debug = DEBUG)
