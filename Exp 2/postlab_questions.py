import speech_recognition as sr
import string

def extract_text_from_audio(audio_file_path):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_file_path) as source:
        audio = recognizer.record(source)
        try:
            text = recognizer.recognize_google(audio)
            return text
        except sr.UnknownValueError:
            return None

def add_punctuations(text):
    # Add appropriate punctuations to the text
    cleaned_text = text.strip() + "."
    return cleaned_text

audio_file_path = "path_to_your_audio_file.wav"
extracted_text = extract_text_from_audio(audio_file_path)
if extracted_text:
    text_with_punctuations = add_punctuations(extracted_text)
    print(text_with_punctuations)
else:
    print("Unable to extract text from audio.")



import re

def extract_urls(text):
    urls = re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', text)
    return urls

text = "Here is a link to Google: https://www.google.com and another link: http://www.example.com"
urls = extract_urls(text)
print("Extracted URLs:")
for url in urls:
    print(url)
