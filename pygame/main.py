import pygame

pygame.init()

clock = pygame.time.Clock()
screen = pygame.display.set_mode((1200, 675))
pygame.display.set_caption('First_game')


back = pygame.image.load('images/back.png').convert_alpha()
walk_left = [
    pygame.image.load('images/player_go_left/left1.png').convert_alpha(),
    pygame.image.load('images/player_go_left/left2.png').convert_alpha(),
    pygame.image.load('images/player_go_left/left3.png').convert_alpha(),
    pygame.image.load('images/player_go_left/left4.png').convert_alpha()]

walk_right = [
    pygame.image.load('images/player_go_right/right1.png').convert_alpha(),
    pygame.image.load('images/player_go_right/right2.png').convert_alpha(),
    pygame.image.load('images/player_go_right/right3.png').convert_alpha(),
    pygame.image.load('images/player_go_right/right4.png').convert_alpha()]

player_anim_count = 0
back_x = 0

player_speed = 5
player_x = 400
player_y = 540

monstr_list_in_game = []

slyz = pygame.image.load('images/slyz.png').convert_alpha()
slyz_x = 1202
slyz_y = 545

jump = False
jump_count = 8

slyz_timer = pygame.USEREVENT + 1
pygame.time.set_timer(slyz_timer, 2000)

text = pygame.font.Font('fonts/Oswald-VariableFont_wght.ttf', 70)
text_lose = text.render('Вы проиграли', False, (244, 9, 58))

game_play = True

running = True
while running:

    screen.blit(back, (back_x, 0))
    screen.blit(back, (back_x + 1200, 0))

    if game_play:

        player_rect = walk_left[0].get_rect(topleft=[player_x, player_y])

        if monstr_list_in_game:
            for elem in monstr_list_in_game:
                screen.blit(slyz, elem)
                elem.x -= 10
                if player_rect.colliderect(elem):
                    game_play = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            screen.blit(walk_left[player_anim_count], (player_x, player_y))

        else:
            screen.blit(walk_right[player_anim_count], (player_x, player_y))

        if keys[pygame.K_LEFT] and player_x > 50:
            player_x -= player_speed
        elif keys[pygame.K_RIGHT] and player_x < 600:
            player_x += player_speed

        if not jump:
            if keys[pygame.K_SPACE]:
                jump = True
        else:
            if jump_count >= -8:
                if jump_count > 0:
                    player_y -= (jump_count ** 2) / 2
                else:
                    player_y += (jump_count ** 2) / 2
                jump_count -= 1
            else:
                jump = False
                jump_count = 8
        if player_anim_count == 3:
            player_anim_count = 0
        else:
            player_anim_count += 1

        back_x -= 3
        if back_x == -1200:
            back_x = 0

        slyz_x -= 8

    else:
        screen.fill((87, 88, 89))
        screen.blit(text_lose, (400, 250))

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        if event.type == slyz_timer:
            monstr_list_in_game.append(slyz.get_rect(topleft=[1202, 545]))

    clock.tick(15)