# Basic speech to text sample

This sample shows the basic speech to text functionality, converting speech to text in a single language.

## Setup

Before you can run this sample, you will need to ensure you have your Python development environment set up, and do some setup on this project.

Follow the [Project Setup Instructions](./ProjectSetup.md) to get this project set up, including the environment variables, virtual environment and pip packages.

## Run the code

1. From the Visual Studio Code terminal, run the following command:

    ```sh
    python app.py
    ```

The app will run in the terminal and listen for your voice. Speak into your default microphone in English and you will see the words you have said output to the terminal. Say `stop` to end the program.

```output
(.venv) ➜  BasicSpeechToText git:(master) ✗ python app.py
Say something! Say stop when you are done.
Hello World.
Stop.
(.venv) ➜  BasicSpeechToText git:(master) ✗
```

## Change the detected language

This app is configured to listen for words spoken in English. This configuration is set on line 23:

```python
speech_config = speechsdk.SpeechConfig(subscription=key,
                                       region=region,
                                       speech_recognition_language='en-GB')
```

To change the recognized language, change the value of `'en-GB'` to a different language identifier, such as `'en-US'` for American English, or `'zh-CN'` for Chinese. You can find the list of supported languages in the [Language and voice support for the Speech service docs](https://docs.microsoft.com/azure/cognitive-services/speech-service/language-support?WT.mc_id=speechtotextsamples-github-jabenn) on Microsoft Docs.
