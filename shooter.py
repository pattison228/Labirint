from pygame import *
win_width = 700
win_height = 500

window = display.set_mode((win_width, win_height))
display.set_caption("Maze")
background = transform.scale(image.load(
    "background.jpg"), (win_width, win_height))

    
mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.play()

mixer.music.set_volume(0.05)

money = mixer.Sound('money.ogg')
kick = mixer.Sound('kick.ogg')