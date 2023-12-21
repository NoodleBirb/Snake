# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pygame
import time
import random


# initial snake speed
snake_speed = 15

# Window Size
window_width = 720
window_height = 480

# Different colors
green = pygame.Color(0, 255, 0)
red = pygame.Color(255, 0, 0)
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)

# Initialize pygame
pygame.init()

pygame.display.set_caption("Snake Game (hopefully)")

game_window = pygame.display.set_mode((window_width, window_height))

fps = pygame.time.Clock()

# Starting snake position
snake_position = [100, 360]

# Initial Direction
direction = "right"

# Starting snake body
snake_body = [[100, 360],
              [90, 360],
              [80, 360],
              [70, 360]]

# Fruit position
fruit_position = [random.randrange(0, window_width, 10), random.randrange(0, window_height, 10)]

# create points variable
fruits = 0

# displaying Score function
def show_score(color, font, size):
   
    # creating font object score_font
    score_font = pygame.font.SysFont(font, size)
     
    # create the display surface object
    # score_surface
    score_surface = score_font.render('Fruits : ' + str(fruits), True, color)
     
    # create a rectangular object for the text
    # surface object
    score_rect = score_surface.get_rect()
     
    # displaying text
    game_window.blit(score_surface, score_rect)

def game_over():
    
    game_window.fill(black)

    # creating font object score_font
    game_over_font = pygame.font.SysFont("Comic Sans MS", 20)
     
    # create the display surface object
    # score_surface
    game_over_surface = game_over_font.render("Game Over! Your final score was: " + str(fruits) + " fruits!", True, white)
     
    # create a rectangular object for the text
    # surface object
    game_over_rect = game_over_surface.get_rect()
    
    # center the text object
    game_over_rect.midtop = (window_width / 2, window_height / 4)
    
    # display the text
    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
        
    time.sleep(5)
    
    pygame.quit()


# MAIN GAME

while True:
    
    # Check for keypress
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if (event.key == pygame.K_UP or event.key == pygame.K_w) and direction != "down":
                direction = "up"
            elif (event.key == pygame.K_RIGHT or event.key == pygame.K_d) and direction != "left":
                direction = "right"
            elif (event.key == pygame.K_DOWN or event.key == pygame.K_s) and direction != "up":
                direction = "down"
            elif (event.key == pygame.K_LEFT or event.key == pygame.K_a) and direction != "right":
                direction = "left"
            break
   
    # Check for snake head and fruit overlap
    if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
        # Increment fruits and move the fruit
        fruits+=1
        fruit_position = [random.randrange(0, window_width, 10), random.randrange(0, window_height, 10)]
        extra_segments = snake_body[-1]
        for i in range(3):
            snake_body.append(extra_segments.copy())
    
    
    # move snake head in "direction"
    if direction == "up":
        snake_position[1] -= 10
    elif direction == "right":
        snake_position[0] += 10
    elif direction == "down":
        snake_position[1] += 10
    elif direction == "left":
        snake_position[0] -= 10
    
    # move entire snake
    snake_body.pop(-1)
    snake_body.insert(0, snake_position.copy())
    
    # draw everything
    game_window.fill(black)
    show_score(white, "Comic Sans MS", 20)
    
    for segments in snake_body:
        pygame.draw.rect(game_window, green, pygame.Rect(segments[0], segments[1], 10, 10))
    pygame.draw.rect(game_window, red, pygame.Rect(fruit_position[0], fruit_position[1], 10, 10))
    
    # Lose if hit wall
    if snake_position[0] > window_width or snake_position[0] < 0 or snake_position[1] > window_height or snake_position[1] < 0:
        game_over()
    
    # Lose if hit body
    for snake_bodies in snake_body[1:]:
        if snake_bodies[0] == snake_position[0] and snake_bodies[1] == snake_position[1]:
            game_over()
    
    # update display
    pygame.display.update()
    
    fps.tick(snake_speed)

