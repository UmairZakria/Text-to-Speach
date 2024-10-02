import pyttsx3
import os
import io
import tempfile
import threading

engine = pyttsx3.init()
engine.setProperty('rate', 150)
engine.setProperty('volume', 1.0)
voices = engine.getProperty('voices')

lock = threading.Lock() 
def set_voice(engine, voice):
    voices = engine.getProperty('voices')
    if voice == 'Male':
        engine.setProperty('voice', voices[0].id)
    elif voice == 'Female':
        engine.setProperty('voice', voices[1].id)
    else:
        engine.setProperty('voice', voices[0].id)  # 

def texttosound(text,voice):
    with tempfile.NamedTemporaryFile(delete=False, suffix='.wav') as tmp_file:
        tmp_filename = tmp_file.name

    with lock:
        set_voice(engine, voice)
        engine.save_to_file(text, tmp_filename)
        engine.runAndWait()

    audio_stream = io.BytesIO()
    with open(tmp_filename, 'rb') as f:
        audio_stream.write(f.read())
    audio_stream.seek(0)

    os.remove(tmp_filename)  # Clean up the temporary file

    return audio_stream