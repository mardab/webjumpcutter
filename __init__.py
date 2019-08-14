import os, flask, pexpect, logging
app = flask.Flask(__name__)

@app.route("/", methods = ['GET'])
def input_page():
   if(os.environ.get('WEBJUMPCUTTER_MONGO')!=None):
      gdpr = 'This service stores anonymized usage data for statistics and research purposes and is compliant with General Data Protection Regulations'
   else:
      gdpr = 'This service does not store any information subject to General Data Protection Regulations'
      return flask.render_template('main.html', gdpr=gdpr)

@app.route("/process", methods = ['POST'])
def output_page():
   form_params = flask.request.form
   video_file = flask.request.files['data_file']
   file_content = video_file.stream.read().decode("utf-8")
   result = process(file_content)
   response = flask.make_response(result)
   response.headers["Content-Disposition"] = "attachment; filename="+video_file.filename
   return

def process():



if __name__ == '__main__':
   app.run('0.0.0.0',8080)