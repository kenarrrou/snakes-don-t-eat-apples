import pygame
import random

pygame.init()

screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Snakes don't eat apples")
clock = pygame.time.Clock()

bg = pygame.image.load('bg.jpg')
head_img = pygame.image.load('head.png')
body_img = pygame.image.load('body.png')
food_img = pygame.image.load('food.png')

while True:

    x = 50 
    y = 50
    size = 30
    speed = 3
    color = (12, 122, 100)
    direction = None
    
    food_x = random.randint(0, 600 - size)
    food_y = random.randint(0, 400 - size)
    size1 = 20
    color1 = (150, 0, 0)
    tail = []
    score = 0

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and direction != 'down':
                    direction = 'up'
                if event.key == pygame.K_DOWN and direction != 'up':
                    direction = 'down'
                if event.key == pygame.K_LEFT and direction != 'right':
                    direction = 'left'
                if event.key == pygame.K_RIGHT and direction != 'left':
                    direction = 'right'
            
        if x < 0 or x > 600 - size or y < 0 or y > 400 - size:
            running = False
        
        if abs(x - food_x) < size and abs(y - food_y) < size:
            score += 1
            food_x = random.randint(0, 600 - size)
            food_y = random.randint(0, 400 - size)
             
        if direction == 'up':
            y -= speed
        elif direction == 'down':
            y += speed
        elif direction == 'left':
            x -= speed
        elif direction == 'right':
            x += speed
                
        if direction == 'right':
            current_head = head_img
        elif direction == 'up':
            current_head = pygame.transform.rotate(head_img, 90)
        elif direction == 'left':
            current_head = pygame.transform.rotate(head_img, 180)
        elif direction == 'down':
            current_head = pygame.transform.rotate(head_img, 270)
        else:
            current_head = head_img
    
        screen.blit(bg, (0, 0))
       
        tail.append([x, y])
        for segment in tail[:-1]:
             screen.blit(body_img, (segment[0], segment[1]))
        if len(tail) > score + 1:
            tail.pop(0)
            
        for segment in tail[:-1]:
            if segment[0] == x and segment[1] == y:
                running = False
        
    
        screen.blit(current_head, (x, y))
        screen.blit(food_img, (food_x, food_y))
        pygame.display.flip()
        clock.tick(60)

    play_again = None
    while play_again == None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                play_again = False
                break
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    play_again = True
                    break
                if event.key == pygame.K_q:
                    play_again = False
                    break
        pygame.time.wait(10)            
    if not play_again:
        break
        
pygame.quit()