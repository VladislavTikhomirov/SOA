import pyttsx3

engine = pyttsx3.init()

# Retrieve the list of available voices
voices = engine.getProperty('voices')

# Print voice details
for voice in voices:
    print("Voice:")
    print(" - ID: %s" % voice.id)
    print(" - Name: %s" % voice.name)
    print(" - Languages: %s" % voice.languages)
    print(" - Gender: %s" % voice.gender)
    print(" - Age: %s" % voice.age)