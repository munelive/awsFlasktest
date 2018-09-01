from flask import Flask

#-------------------------------------------------------
#Setup flask
app = Flask(__name__)
PORT = 80
DEBUG = True
HOST = '0.0.0.0'

@app.errorhandler(404)
def not_found(error):
    return "Not Found."


#-------------------------------------------------------
#init
@app.route('/', methods=['POST','GET'])
def init():
    print('With flask2')
    return '2222App connections with: 1. /webhookasana: To connect asana to todoist /// 2. /webhooktodoist: To connect Todoist to asana'







#-------------------------------------------------------
if __name__ == '__main__':
    #app.run(host = HOST, port = PORT, debug = DEBUG)
    app.run(host = HOST, port = PORT)
