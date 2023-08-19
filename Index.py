import os
import pygame

pygame.init()

pygame.display.set_caption("My Music Player")

win = pygame.display.set_mode((600, 300))

music_dir = "/home/nambela/Desktop/py pro/music/"

music_files = os.listdir(music_dir)

pygame.mixer.init()

def play_music(file_path):
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()

def display_music_list(start_index, num_visible):
    font = pygame.font.Font(None, 30)
    font_color = (255, 255, 0)  # Yellow font color
    
    for i in range(start_index, min(start_index + num_visible, len(music_files))):
        file = music_files[i]
        text = font.render(str(i+1) + ". " + file, True, font_color)
        win.blit(text, (10, (i - start_index) * 30 + 10))

# Game loop
running = True
start_index = 0  # Index of the first visible music file
num_visible = 10  # Number of visible music files at a time

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif pygame.K_1 <= event.key <= pygame.K_9:  # Handle keys 1 to 9
                index = event.key - pygame.K_1
                selected_index = start_index + index
                if 0 <= selected_index < len(music_files):
                    play_music(os.path.join(music_dir, music_files[selected_index]))
            elif event.key == pygame.K_DOWN:
                start_index = min(start_index + 1, len(music_files) - num_visible)
            elif event.key == pygame.K_UP:
                start_index = max(start_index - 1, 0)
    
    background_color = (96, 96, 96) #gray
    win.fill(background_color)  # Clear the window
    display_music_list(start_index, num_visible)  # Display the list of music files
    pygame.display.update()  # Update the display

pygame.mixer.quit()  # Quit pygame mixer
pygame.quit()  # Quit pygame
