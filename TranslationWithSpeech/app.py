import os
import time
from dotenv import load_dotenv
import azure.cognitiveservices.speech as speechsdk

# Load the speech key and region from the .env file
load_dotenv()
key = os.getenv('KEY')
region = os.getenv('REGION')

stop = False

# Create a speech configuration using the key and region
speech_config_cn = speechsdk.SpeechConfig(subscription='key', region='region')
speech_config_en = speechsdk.SpeechConfig(subscription='key', region='region')

# Sets the synthesis language.
# The full list of supported languages can be found here:
# https://docs.microsoft.com/azure/cognitive-services/speech-service/language-support#text-to-speech
speech_config_cn.speech_synthesis_language = "zh-CN"
speech_config_en.speech_synthesis_language = "en-GB"

# Creates a speech synthesizer for the specified language, using the default speaker as audio output.
speech_synthesizer_cn = speechsdk.SpeechSynthesizer(speech_config=speech_config_cn)
speech_synthesizer_en = speechsdk.SpeechSynthesizer(speech_config=speech_config_en)

# Create a speech translation configuration using the key and region
# This also specifies the languages to translate to
translation_config = speechsdk.translation.SpeechTranslationConfig(subscription='key', 
                                                                   region='region',
                                                                   speech_recognition_language='en-GB',
                                                                   target_languages=('zh-Hans', 'en', 'fr', 'de'))

# Creates a translation recognizer
recognizer = speechsdk.translation.TranslationRecognizer(translation_config=translation_config)

# When a sentence is recognized, print it to the screen.
# If stop is said, stop the app
def recognized(args):
    global stop
    global recognizer
    if args.result.reason == speechsdk.ResultReason.TranslatedSpeech:
        print("Chinese   :", args.result.translations['zh-Hans'])
        print("English   :", args.result.translations['en'])
        print("French    :", args.result.translations['fr'])
        print("German    :", args.result.translations['de'])
        print()

        # Pause recognition so the spoken text isn't automatically translated
        recognizer.stop_continuous_recognition()

        # Speak the translated text
        speech_synthesizer_cn.speak_text(args.result.translations['zh-Hans'])
        speech_synthesizer_en.speak_text(args.result.translations['en'])

        # Restart continuous recognition
        recognizer.start_continuous_recognition()

        if args.result.translations['en'] == "Stop.":
            stop = True

# Connect up the recognized event
recognizer.recognized.connect(recognized)

# Start continuous recognition
# This happens in the background, so the app continues to run, hence the need for an infinite loop
recognizer.start_continuous_recognition()

print("Say something! Say stop when you are done.")

# Loop until we hear stop
while not stop:
    time.sleep(0.1)
