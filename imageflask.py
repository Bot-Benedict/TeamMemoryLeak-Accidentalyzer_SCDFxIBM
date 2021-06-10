import flask
from flask import request, jsonify, Flask, render_template, request

app = flask.Flask(__name__)
app.config['UPLOAD_FOLDER'] = './'
app.config["DEBUG"] = False


@app.route('/api/imageprocessing', methods=['GET'])
def api_id():
    if 'url' in request.args:
        url = str(request.args['url'])
    else:
        return "Error: No image path provided."
    if 'cameraid' in request.args:
        cameraid = int(request.args['cameraid'])
    #call function, take in image path and return event type
    return {
        "cameraId": cameraid,
        "eventType": url,
    }

@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      f.save(f.filename)
      return 'file uploaded successfully'

app.run()
