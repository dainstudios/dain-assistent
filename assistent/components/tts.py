import os
import azure.cognitiveservices.speech as speechsdk
from dotenv import load_dotenv

load_dotenv()

key = os.getenv('AZURE_SPEECH_KEY')
region = os.getenv('AZURE_SPEECH_REGION')
speech_config = speechsdk.SpeechConfig(subscription=key, region=region)


class TTS:

    def __init__(self, language, filename=None, use_default_speaker=True):
        self.languages = {'german': 'de-DE-AmalaNeural',
                          'english': 'en-AU-KimNeural',
                          'finnish': 'fi-FI-SelmaNeural',
                          'french': 'fr-BE-CharlineNeural',
                          'spanish': 'es-VE-PaolaNeural',
                          'italy': 'it-IT-ElsaNeural',
                          'österreich': 'de-AT-IngridNeural'}

        self.language = language if language in self.languages.keys() else 'english'
        self.filename = filename
        self.voice = self.languages[self.language]
        self.use_default_speaker = use_default_speaker

    def __call__(self, *args, **kwargs):
        if 'text' in kwargs:
            text = kwargs['text']
        else:
            return

        audio_config = speechsdk.audio.AudioOutputConfig(use_default_speaker=self.use_default_speaker,
                                                         filename=self.filename)

        # The language of the voice that speaks.
        speech_config.speech_synthesis_voice_name = self.voice

        speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)
        speech_synthesis_result = speech_synthesizer.speak_text_async(text).get()
        print(speech_synthesis_result)

        if speech_synthesis_result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
            print("Speech synthesized")
        elif speech_synthesis_result.reason == speechsdk.ResultReason.Canceled:
            cancellation_details = speech_synthesis_result.cancellation_details
            print("Speech synthesis canceled: {}".format(cancellation_details.reason))
            if cancellation_details.reason == speechsdk.CancellationReason.Error:
                if cancellation_details.error_details:
                    print("Error details: {}".format(cancellation_details.error_details))
