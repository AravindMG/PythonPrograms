import pygame


def pmusic():
    Havanna = "/Users/aravind/Downloads/camila_cabello_havana_audio_ft._young_thug_mp3_50139.mp3"
    pygame.init()
    pygame.mixer.init()
    clock = pygame.time.Clock()
    pygame.mixer.music.load(Havanna)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        print("Playing...")
        clock.tick(250)
    pygame.mixer.music.stop()


def nextmusic():
    Havanna = "/Users/aravind/Downloads/camila_cabello_havana_audio_ft._young_thug_mp3_50139.mp3"
    pygame.init()
    pygame.mixer.init()
    clock = pygame.time.Clock()
    pygame.mixer.music.load(Havanna)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        print("Playing...")
        clock.tick(250)
    pygame.mixer.music.stop()


if __name__ == "__main__":
    pmusic()
    nextmusic()