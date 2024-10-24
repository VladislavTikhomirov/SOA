import os
import subprocess as sp

paths = {
    'notepad': "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Accessories",
    'discord': "C:\\Users\\Vlad\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Discord Inc\\Discord.lnk",
    'spotify': "C:\\Users\\Vlad\\AppData\\Roaming\\Spotify\\Spotify.exeC:\\Users\\Vlad\\AppData\\Roaming\\Spotify\\Spotify.exe",
}


def open_notepad():
    os.startfile(paths['notepad'])


def open_discord():
    os.startfile(paths['discord'])

def open_spotify():
    os.startfile(paths['spotify'])

def open_cmd():
    os.system('start cmd')


def open_camera():
    sp.run('start microsoft.windows.camera:', shell=True)


