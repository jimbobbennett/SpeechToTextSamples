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
    print(args.result.text)

    if args.result.text == "Stop.":
        stop = True

# Create a speech configuration using the key and region
speech_config = speechsdk.SpeechConfig(subscription=key, 
                                       region=region, 
                                       speech_recognition_language='en-GB')

# Create a speech recognizer
recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config)

# Connect up the recognized event
recognizer.recognized.connect(recognized)

# Start continuous recognition
# This happens in the background, so the app continues to run, hence the need for an infinite loop
recognizer.start_continuous_recognition()

print("Say something! Say stop when you are done.")

# Loop until we hear stop
while not stop:
    time.sleep(0.1)