import speech_recognition as sr
import spotipy
from spotipy.oauth2 import SpotifyOAuth



class SpotifyVoiceReg():
    r = sr.Recognizer()
    client_id = 'b27f6cdd8312405fb66fd183e98a3b98'
    client_secret = '1dfe11f21c1a49468e1f4ae5b4d8207f'
    redirect_uri = 'http://localhost:8888'  # Must match the registered redirect URI in your Spotify Developer application settings

# Define the voice command to play a song
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

    # Continuously listen for voice commands
    while True:
        try:
            with sr.Microphone() as source:
                print('Listening...')
                audio = r.listen(source)

            # Use speech recognition to convert audio to text
            command = r.recognize_google(audio)

            # Process the voice command
            if 'play' in command.lower():
                song_name = command.split('play', 1)[1].strip()
                play_song(song_name)
            elif 'stop' in command.lower():
                # Stop the playback
                sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri))
                sp.pause_playback()
                print('Playback stopped.')

        except sr.UnknownValueError:
            print('Sorry, I could not understand your command.')
        except sr.RequestError as e:
            print('Error occurred: {0}'.format(e))
