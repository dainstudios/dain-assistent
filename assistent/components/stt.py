import os

import speech_recognition as sr
import openai

folder = "./audio"
filename = "microphone-results"
audio_file_path = f"{folder}/{filename}.wav"

class STT:
    def __init__(self, name):
        self.name = name
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()

    def speech_to_text(self, audio):

        if not os.path.exists(folder):
            os.mkdir(folder)

        with open(audio_file_path, "wb") as f:
            f.write(audio.get_wav_data())

        print(f'{self.name}: Understanding...')
        f = open(audio_file_path, "rb")

        transcript = openai.Audio.translate("whisper-1", f, api_key=os.getenv('OPENAI'))
        speech_to_text = transcript['text']

        if self.name not in speech_to_text:
            return None
        else:
            return speech_to_text.split(self.name)[-1]

    def __call__(self, *args, **kwargs):
        with self.microphone as source:
            self.recognizer.adjust_for_ambient_noise(source)
            print(f'{self.name}: Listen!')
            speech = self.recognizer.listen(source)

        text = self.speech_to_text(speech)
        return text