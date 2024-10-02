from flask import Flask, render_template, request, send_file
from Texttosound import texttosound

app = Flask(__name__)


x= True
@app.route('/speak', methods=['POST'])
def speak():
    text = request.form['text']
    selected_voice = request.form['voice']
    
    audio_file = texttosound(text, selected_voice)
    return send_file(audio_file, mimetype='audio/wav')
@app.route('/')
def Home():
    return render_template('index.html', x='Male', y='Female')

if __name__ == "__main__":
    app.run(debug=True)
