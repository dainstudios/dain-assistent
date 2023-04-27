# dain-assistant
An AI assistant based on speech-to-text -> GTP3.5-turbo -> text-to-speech

## Parameter
```
name : Name of the User 
name_ai : Name of the Assistent 
language : Language (english, german, finnish, spanish, italy, french)
```
# API-Keys
Create an file ".env" and add the following keys 
```
AZURE_SPEECH_KEY=4e094d57fb1949e89699b2ebf30e5ce0 
AZURE_SPEECH_REGION=westeurope

OPENAI=sk-xxx 
OPENAI_ORGANIZATION=org-T3LbgBaVGfLP5QJ5wQCSWc0z
```
## Installation
```
sudo apt-get install portaudio19-dev python-all-dev python3-all-dev && sudo pip install pyaudio

pip install -r requirements.txt

or

poetry install
```
## Usage

Just tell the name of the AI-Assistent following by the question.

#### Example:

If the name of the AI-Assistent is Lemon. 
```
Lemon: Listening! 
User: "Lemon create a meme about wednesday." 
Lemon: Understanding... 
Lemon: Lemon it's wednesday!
```
