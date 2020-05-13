# Translation sample

This sample shows the translation capabilities of the speech to text service, converting speech to text in multiple languages.

## Setup

Before you can run this sample, you will need to ensure you have your Python development environment set up, and do some setup on this project.

Follow the [Project Setup Instructions](./ProjectSetup.md) to get this project set up, including the environment variables, virtual environment and pip packages.

## Run the code

1. From the Visual Studio Code terminal, run the following command:

    ```sh
    python app.py
    ```

The app will run in the terminal and listen for your voice. Speak into your default microphone in English and you will see the words you have said output to the terminal in Chinese, English, French and German. Say `stop` to end the program.

```output
(.venv) ➜  Translation git:(master) ✗ python app.py
Say something! Say stop when you are done.
Chinese   : 世界您好。
English   : Hello world.
French    : Salut tout le monde.
German    : Hallo Welt.

Chinese   : 停止。
English   : Stop.
French    : Arrêter.
German    : Stoppen.

(.venv) ➜  Translation git:(master) ✗
```

## Change the detected language

This app is configured to listen for words spoken in English, and output the English text of the spoken words, as well as translations into Chinese, English, French and German. This configuration is set on line 29:

```python
translation_config = speechsdk.translation.SpeechTranslationConfig(subscription=key,
                                                                   region=region,
                                                                   speech_recognition_language='en-GB',
                                                                   target_languages=('zh-Hans', 'en', 'fr', 'de'))
```

To change the recognized language, change the value of `'en-GB'` to a different language identifier, such as `'en-US'` for American English, or `'zh-CN'` for Chinese. You can find the list of supported languages in the [Language and voice support for the Speech service docs](https://docs.microsoft.com/azure/cognitive-services/speech-service/language-support?WT.mc_id=speechtotextsamples-github-jabenn) on Microsoft Docs.

To change the language that the speech is translated into, change the values of `target_languages`. When the text is translated, the `recognized` function is called with a list of translations in a dictionary. You will also need to change the code here to access the languages you have specified.

```python
def recognized(args):
    global stop
    if args.result.reason == speechsdk.ResultReason.TranslatedSpeech:
        print("Chinese   :", args.result.translations['zh-Hans'])
        print("English   :", args.result.translations['en'])
        print("French    :", args.result.translations['fr'])
        print("German    :", args.result.translations['de'])
        print()

        if args.result.translations['en'] == "Stop.":
            stop = True
```
