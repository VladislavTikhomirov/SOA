import pygame, math, sys
from functions.online_ops import find_my_ip,get_random_advice, get_random_joke,play_on_youtube, search_on_google, search_on_wikipedia, send_email, weather, order_pizza
import pyttsx3
import speech_recognition as sr

from datetime import datetime
from functions.os_ops import open_camera, open_cmd, open_notepad, open_discord, open_spotify
from random import choice
from utils import opening_text
from pprint import pprint


import speech_recognition as sr
import spotipy
from spotipy.oauth2 import SpotifyOAuth

import threading

from SOA import SOA_uncensored

scope = "user-read-playback-state"




USERNAME = 'Vlad'
BOTNAME = 'Jarvis'


    
engine = pyttsx3.init('sapi5')

# Set Rate
engine.setProperty('rate', 190)

# Set Volume
engine.setProperty('volume', 1.0)

# Set Voice (Female)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

convinience =  "For your convenience, I am printing it on the screen."
#openai feature


# Text to Speech Conversion
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Greet the user
def greet_user():
    hour = datetime.now().hour
    if (hour >= 6) and (hour < 12):
        speak(f"Good Morning {USERNAME}")
    elif (hour >= 12) and (hour < 16):
        speak(f"Good afternoon {USERNAME}")
    elif (hour >= 16) and (hour < 19):
        speak(f"Good Evening {USERNAME}")
    speak(f"{BOTNAME} System online. How may I assist you today?")

def play_song(song_name):
    client_id = 'b27f6cdd8312405fb66fd183e98a3b98'
    client_secret = '1dfe11f21c1a49468e1f4ae5b4d8207f'
    redirect_uri = 'http://localhost:8888'  # Must match the registered redirect URI in your Spotify Developer application settings
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri,scope='user-modify-playback-state'))
    results = sp.search(q='track:' + song_name, type='track', limit=1)
    if results['tracks']['items']:
        track_uri = results['tracks']['items'][0]['uri']
        sp.start_playback(uris=[track_uri])
        print('Playing song: ' + song_name)
    else:
        print('Song not found: ' + song_name)


def chat_response(query):
    SOA = SOA_uncensored(model_name="wizardlm-uncensored:13b")
    response = SOA.generate_response(query)
    return response

# Takes Input from User
def take_user_input():
    global is_listening
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening....')
        r.pause_threshold = 1
        r.phrase_threshold = 0.1
        r.non_speaking_duration = 0.2
        audio = r.listen(source)

    try:
        print('Interpretating...')
        query = r.recognize_google(audio, language='en-Us')
        if not 'exit' in query:
            speak(choice(opening_text))
        if 'play' in query.lower():
            song_name = query.split('play', 1)[1].strip()
            play_song(song_name)
            input("Press Enter to start voice recognition again...")
        if'soa' or 'SOA' or 'chat' or 'ai' in query.lower():
            speak(chat_response(query))
    except Exception:
        print("Invalid command")
        query = 'None'
    
    return query



def jarvis_visual():
    # Initialize Pygame
    pygame.init()

    # Set up the display
    width, height = 400, 400
    screen = pygame.display.set_mode((width, height))
    icon = pygame.image.load("jarv.jpg")
    pygame.display.set_icon(icon)
    pygame.display.set_caption("Jarvis")

    # Colors
    BLACK = (0, 0, 0)

    # Main game loop
    running = True
    angle1 = 0
    angle3 = 90  # Angle offset for the third line

    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Clear the screen
        screen.fill(BLACK)

        # Calculate the position of the first spinning line
        radius1 = 100
        center_x, center_y = width // 2, height // 2
        line_length1 = 120  # Length of the first curved line segment

        # Calculate the start and end angles of the first curved line segment
        start_angle1 = math.radians(angle1)
        end_angle1 = math.radians(angle1 + 90)

        # Calculate the color for the first curved line segment
        color1 = pygame.Color(255, 0, 0)
        color1.hsla = (angle1 % 360, 100, 50, 100)

        # Draw the first spinning curved line segment
        pygame.draw.arc(screen, color1, (center_x - radius1, center_y - radius1, radius1 * 2, radius1 * 2), start_angle1, end_angle1, 4)

        # Calculate the position of the second spinning line
        radius2 = 150
        line_length2 = 180  # Length of the second curved line segment

        # Calculate the start and end angles of the second curved line segment
        start_angle2 = math.radians(-angle1)
        end_angle2 = math.radians(-angle1 - 90)

        # Calculate the color for the second curved line segment
        color2 = pygame.Color(255, 0, 0)
        color2.hsla = ((angle1 + 180) % 360, 100, 50, 100)

        # Draw the second spinning curved line segment
        pygame.draw.arc(screen, color2, (center_x - radius2, center_y - radius2, radius2 * 2, radius2 * 2), start_angle2, end_angle2, 6)

        # Calculate the position of the third spinning line
        radius3 = 200
        line_length3 = 240  # Length of the third curved line segment

        # Calculate the start and end angles of the third curved line segment
        start_angle3 = math.radians(angle3)
        end_angle3 = math.radians(angle3 + 90)

        # Calculate the color for the third curved line segment
        color3 = pygame.Color(255, 0, 0)
        color3.hsla = ((angle3 + 90) % 360, 100, 50, 100)

        # Draw the third spinning curved line segment
        pygame.draw.arc(screen, color3, (center_x - radius3, center_y - radius3, radius3 * 2, radius3 * 2), start_angle3, end_angle3, 8)

        # Update the angles
        angle1 += 1
        angle3 += 1.5

        # Update the display
        pygame.display.flip()

        # Delay between frames (5 milliseconds in this case)
        pygame.time.delay(5)

    # Quit Pygame
    pygame.quit()

if __name__ == '__main__':
    visual_thread = threading.Thread(target=jarvis_visual)
    visual_thread.start()

    greet_user() 
    while True:
        query = take_user_input().lower()
        
        if 'ip address' in query:
            ip_address = find_my_ip()
            speak(f'Your IP Address is {ip_address}.\n For your convenience, I am printing it on the screen.')
            print(f'Your IP Address is {ip_address}')

        elif 'wikipedia' in query:
            speak('What do you want to search on Wikipedia?')
            search_query = take_user_input().lower()
            results = search_on_wikipedia(search_query)
            speak(f"According to Wikipedia, {results}")
            speak(convinience)
            print(results)

        elif 'youtube' in query:
            speak('What do you want to play on Youtube?')
            video = take_user_input().lower()
            play_on_youtube(video)

        elif 'google' in query:
            speak('What do you want to search on Google?')
            query = take_user_input().lower()
            search_on_google(query)

        elif 'send an email' in query:
            speak("Which email address should I use? Please enter in the console: ")
            receiver_address = input("Enter email address: ")
            speak("What should the subject be?")
            subject = take_user_input().capitalize()
            speak("What is the message.?")
            message = take_user_input().capitalize()
            if send_email(receiver_address, subject, message):
                speak("I've sent the email.")
            else:
                speak("Something went wrong while I was sending the mail. Please check the error logs.")

        elif 'joke' in query:
            speak(f"This one is a favourite of mine.")
            joke = get_random_joke()
            speak(joke)
            speak(convinience)
            print(joke)

        elif 'advice' in query:
            speak(f"Here's some advice for you.")
            advice = get_random_advice()
            speak(advice)
            speak(convinience)
            print(advice)
        
        elif 'weather' in query:
            speak(f"Here is the weather for you.")
            weather()

        elif 'pizza' in query:
            speak("Hungry are we.")
            order_pizza()

       