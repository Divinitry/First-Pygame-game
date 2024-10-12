import pygame

pygame.init()
# player_screen = pygame.display.get_desktop_sizes()[0]
# screen_size_x = player_screen[0]
# screen_size_y = player_screen[1]
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0
player_size = 20

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill("#8cff92")

    pygame.draw.circle(screen, "black", player_pos, player_size) 

    keys = pygame.key.get_pressed()
    # Up (W) 
    if keys[pygame.K_w] and player_pos.y > 0 + player_size:
        player_pos.y -= 300 * dt 
    # Down (S)
    if keys[pygame.K_s] and player_pos.y < 720 - player_size:
        player_pos.y += 300 * dt 
    # Left (A)
    if keys[pygame.K_a] and player_pos.x > 0 + player_size:
        player_pos.x -= 300 * dt
    # Right (D)
    if keys[pygame.K_d] and player_pos.x < 1280 - player_size:
        player_pos.x += 300 * dt
    
    mouse_pressed = pygame.mouse.get_pressed()

    if mouse_pressed[0] == True:
        screen.fill("black")


    pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()

