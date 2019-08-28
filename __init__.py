import os, flask, subprocess, logging
from werkzeug import secure_filename
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
   video_data = flask.request.files['video'].save()
   ifname = flask.secure_filename(video_file.filename)
   video_file = video_data.save(os.path.join(os.environ.get('WJC_UPLOAD_FOLDER'), ifname))
   #file_content = video_file.stream.read().decode("utf-8")
   process_result = process(video_file, form_params)
   response = flask.make_response(process_result).headers["Content-Disposition"] = "attachment; filename="+ifname
   response.headers["Cache-Control"] = "must-revalidate"
   response.headers["Pragma"] = "must-revalidate"
   return response

def process(input_file, params):
   processed_video = input_file
   return processed_video
   
if __name__ == '__main__':
   app.run('0.0.0.0',8080)