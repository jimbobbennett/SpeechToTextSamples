# Mic drop sample

This sample shows the translation capabilities of the speech to text service, converting speech to text in multiple languages in a UI app. It also demonstrates using speech to control an app.

## Setup

Before you can run this sample, you will need to ensure you have your Python development environment set up, and do some setup on this project.

Follow the [Project Setup Instructions](./ProjectSetup.md) to get this project set up, including the environment variables, virtual environment and pip packages.

## Run the code

1. From the Visual Studio Code terminal, run the following command:

    ```sh
    python app.py
    ```

The app will launch a UI using Tkinter. Speak into your default microphone in English and you will see the words you have said output to the UI in English and Chinese. Say `stop` to end the program. Say `mic drop` for a surprise!

![OUtput from the UI](../images/ui-output.png)

## Change the detected language

This app is configured to listen for words spoken in English, and output the English text of the spoken words, as well as translations into Chinese. This configuration is set on line 93:

```python
translation_config = speechsdk.translation.SpeechTranslationConfig(subscription=key,
                                                                   region=region,
                                                                   speech_recognition_language='en-GB',
                                                                   target_languages=('zh-Hans'))
```

To change the recognized language, change the value of `'en-GB'` to a different language identifier, such as `'en-US'` for American English, or `'zh-CN'` for Chinese. You can find the list of supported languages in the [Language and voice support for the Speech service docs](https://docs.microsoft.com/azure/cognitive-services/speech-service/language-support?WT.mc_id=build2020_ca-github-jabenn) on Microsoft Docs.

To change the language that the speech is translated into, change the values of `target_languages`. When the text is translated, the `recognized` function is called with a list of translations in a dictionary. You will also need to change the code here to access the languages you have specified on line 81.

```python
output_text.set((args.result.text) + "\n\n" + args.result.translations['zh-Hans'])
```
