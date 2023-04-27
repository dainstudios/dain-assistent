import argparse
import textwrap

from components.stt import STT
from components.tts import TTS
from components.gpt import GPT3

class Assistent:

    def __init__(self, name, name_ai, language):
        self.name = name
        self.name_ai = name_ai
        self.stt = STT(name=name_ai)
        self.tts = TTS(language=language)
        self.gpt = GPT3()
        self.language = self.tts.language

    def run(self):
        while True:
            text = self.stt()
            if text is not None:
                print(textwrap.fill(f'{args.name}: {text} \n', width=80))
                text += f' Only answer in {self.language}. Call me by my name {self.name}'
                text = self.gpt.request(text)
                print(textwrap.fill(f'{args.name_ai}: {text} \n', width=80))
                self.tts(text=text)

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--name', default='Silvio', type=str)
    parser.add_argument('--name_ai', default='Lemon', type=str)
    parser.add_argument('--language', default='english', type=str)
    return parser.parse_args()

def main():

    assistent = Assistent(name=args.name,
                          name_ai=args.name_ai,
                          language=args.language)
    assistent.run()

if __name__ == "__main__":
    args = parse_args()
    main()
