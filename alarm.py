import pygame

pygame.init()
pygame.mixer.init()

def play_alarm():

    pygame.mixer.music.load("alarm.mp3")

    pygame.mixer.music.play(-1)

def stop_alarm():

    pygame.mixer.music.stop()