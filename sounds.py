import pygame

pygame.init()

SOUND_CORRECT_GUESS = "correct_guess.wav"
SOUND_WRONG_GUESS = "wrong_guess.wav"
SOUND_WIN = "win.wav"
SOUND_LOSE = "loose.wav"

def play_sound(sound_file):
    try:
        som = pygame.mixer.Sound(sound_file)
        som.play()
    except:
        pass

def play_correct_guess_sound():
    play_sound(SOUND_CORRECT_GUESS)

def play_wrong_guess_sound():
    play_sound(SOUND_WRONG_GUESS)

def play_win_sound():
    play_sound(SOUND_WIN)

def play_lose_sound():
    play_sound(SOUND_LOSE)