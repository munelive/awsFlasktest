from flask import Flask, request

#-------------------------------------------------------
#Setup flask
app = Flask(__name__)
PORT = 8000
DEBUG = True
HOST = '0.0.0.0'

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
#webhook Asana To Todoist (create a task in Asana -> Create task in Todoist)
@app.route('/createwebhookasana', methods=['POST','GET'])
def createwebhookasana():
    print('starthook')
    dat = request.headers
    print(str(dat))
    xhook = request.headers['X-Hook-Secret']

    print(xhook)
    #xhook = request.form['X-Hook-Secret']
    #url = request.form['target']
    #r=requests.post("https://09ffd427.ngrok.io/webhookasana")
    #r = requests.post(str(url))
    #print(r.content)
    #request.headers.get(str(xhook))
    #return(str(xhook)+ ' ' + str(url))
    #return(r.headers)

    return(xhook)




#-------------------------------------------------------
if __name__ == '__main__':
    app.run(host = HOST, port = PORT, debug = DEBUG)
