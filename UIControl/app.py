import os
import time
from dotenv import load_dotenv
import azure.cognitiveservices.speech as speechsdk
from tkinter import * 
from PIL import Image, ImageTk

# Load the speech key and region from the .env file
load_dotenv()
key = os.getenv('KEY')
region = os.getenv('REGION')

class MyLabel(Label):
    def __init__(self, master, filename):
        im = Image.open(filename)
        seq =  []
        try:
            while 1:
                seq.append(im.copy())
                im.seek(len(seq)) # skip to next frame
        except EOFError:
            pass # we're done

        try:
            self.delay = im.info['duration']
        except KeyError:
            self.delay = 100

        first = seq[0].convert('RGBA')
        self.frames = [ImageTk.PhotoImage(first)]

        Label.__init__(self, master, image=self.frames[0])

        temp = seq[0]
        for image in seq[1:]:
            temp.paste(image)
            frame = temp.convert('RGBA')
            self.frames.append(ImageTk.PhotoImage(frame))

        self.idx = 0

        self.cancel = self.after(self.delay, self.play)

    def play(self):
        self.config(image=self.frames[self.idx])
        self.idx += 1
        if self.idx == len(self.frames):
            self.idx = 0
        self.cancel = self.after(self.delay, self.play)        


root = Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight() - 20
root.geometry(str(screen_width) + "x" + str(screen_height))

output_text = StringVar()
output_text.set("Say something!")

padding = 20
label_width = screen_width-(padding * 2)

label = Label(root, textvariable=output_text, width=label_width, height=screen_height,
              font=("Courier", 72),
              justify=CENTER, anchor=CENTER, wraplength=label_width)
label.pack(padx=padding, pady=padding)

anim = MyLabel(root, 'mic-drop.gif')

# When a sentence is recognized, print it to the screen.
# If stop is said, stop the app
def recognized(args):
    global output_text
    global root
    global anim
    global label

    if args.result.text == "":
        return
    
    output_text.set(args.result.text)
    
    if args.result.text.lower().startswith("blue"):
        label.destroy()
        label = Label(root, textvariable=output_text, width=label_width, height=screen_height,
            font=("Courier", 72), foreground="blue",
            justify=CENTER, anchor=CENTER, wraplength=label_width)
        label.pack(padx=padding, pady=padding)
    
    if args.result.text.lower().startswith("green"):
        label.destroy()
        label = Label(root, textvariable=output_text, width=label_width, height=screen_height,
            font=("Courier", 72), foreground="green",
            justify=CENTER, anchor=CENTER, wraplength=label_width)
        label.pack(padx=padding, pady=padding)
    
    if args.result.text.lower().startswith("black"):
        label.destroy()
        label = Label(root, textvariable=output_text, width=label_width, height=screen_height,
            font=("Courier", 72), foreground="black",
            justify=CENTER, anchor=CENTER, wraplength=label_width)
        label.pack(padx=padding, pady=padding)

    if args.result.text.lower().startswith("mic drop"):
        time.sleep(1)
        label.pack_forget()
        anim.pack_propagate(0) #Don't allow the widgets inside to determine the frame's width / height
        anim.pack(fill=BOTH, expand=1)
    elif args.result.text == "Stop.":
        root.destroy()

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

root.mainloop()
