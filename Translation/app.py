import os
import time
from dotenv import load_dotenv
import azure.cognitiveservices.speech as speechsdk

# Load the speech key and region from the .env file
load_dotenv()
key = os.getenv('KEY')
region = os.getenv('REGION')

stop = False

# When a sentence is recognized, print it to the screen.
# If stop is said, stop the app
def recognized(args):
    global stop
    if args.result.reason == speechsdk.ResultReason.TranslatedSpeech:
#       print("Any Variable   :", args.result.translations['Spoken Language will be converted to this language.'])
        print("Chinese   :", args.result.translations['zh-Hans'])
        print("English   :", args.result.translations['en'])
        print("French    :", args.result.translations['fr'])
        print("German    :", args.result.translations['de'])
        print()

        if args.result.translations['en'] == "Stop.":
            stop = True

# Create a speech translation configuration using the key and region
# This also specifies the languages to translate to
translation_config = speechsdk.translation.SpeechTranslationConfig(subscription=key, 
                                                                   region=region,
# Here in speech_recognition_language below 'en-GB' Means that It recognizes your language as English with British Accent
# This can be changed to other languages You Desire. Go to the link below to view available languages. 
# See: https://docs.microsoft.com/en-us/azure/cognitive-services/speech-service/language-support?WT.mc_id=build2020_ca-github-jabenn
                                                                   speech_recognition_language='en-GB',
                                                                   target_languages=('zh-Hans', 'en', 'fr', 'de'))

# Creates a translation recognizer
recognizer = speechsdk.translation.TranslationRecognizer(translation_config=translation_config)

# Connect up the recognized event
recognizer.recognized.connect(recognized)

# Start continuous recognition
# This happens in the background, so the app continues to run, hence the need for an infinite loop
recognizer.start_continuous_recognition()

print("Say something! Say stop when you are done.")

# Loop until we hear stop
while not stop:
    time.sleep(0.1)
