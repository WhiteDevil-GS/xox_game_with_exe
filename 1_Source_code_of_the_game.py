import time
import pygame
pygame.init()
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)
game_window = pygame.display.set_mode((500, 500))
pygame.display.set_caption("WHITE_DEVIL_GS")
pygame.display.set_icon(pygame.image.load("gs.png"))
i = -1
global box
verify_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
g1, g2 = 0, 0
draw_verify = [0]
x_list = []
y_list = []
img = pygame.image.load("play(play).jpg")
img_cir = img.get_rect()
img_cir.center = (114, 247)
selection_option = 0
img_pl1_vs_pl2 = pygame.image.load("pl1_vspl22.png")
img_pl1_cir = img_pl1_vs_pl2.get_rect()
img_pl1_cir.center = (300, 250)
img_GS_Logo = pygame.image.load("GS_logo.jpg")
img_GS_cir = img_GS_Logo.get_rect()
img_GS_cir.center = (250, 110)
# global c_x
# global c_o
img_XOX_title = pygame.image.load("gam_title(game).png")
img_XOX_title_cir = img_XOX_title.get_rect()
img_XOX_title_cir.center = (90, 70)
count_x = []
count_y = []
img_game_ex = pygame.image.load("exit_real(re1).jpg")
img_game_ex_cir = img_game_ex.get_rect()
img_game_ex_cir.center = (320, 390)
img1 = pygame.image.load("play(play).jpg")
img_cir1 = img1.get_rect()
img_cir1.center = (120, 390)

img_gm_over = pygame.image.load("gm_over(real).jpg")
img_gm_over_cir = img_gm_over.get_rect()
img_gm_over_cir.center = (250, 100)
text = pygame.font.SysFont("black chancery", 50)
x_color = (255, 165, 0)
y_color = (0, 127, 255)


def dr_line():
    pygame.draw.line(game_window, white, [160, 70], [160, 450], width=3)
    pygame.draw.line(game_window, white, [340, 70], [340, 450], width=3)
    pygame.draw.line(game_window, white, [485, 190], [15, 190], width=3)
    pygame.draw.line(game_window, white, [485, 310], [15, 310], width=3)


def cal_dis_fr_ex(x, y):
    d = (abs(x - 118) ** 2 + abs(y - 416) ** 2)
    return d ** 0.5


def cal_dis(x, y):
    d = (abs(x-97)**2 + abs(y-266)**2)
    return d**0.5


def draw_o(x, y):
    pygame.draw.circle(game_window, y_color, [x, y], radius=45, width=3)


def draw_x(x, y, a, b):
    pygame.draw.line(game_window, x_color, [x, y], [a, b], width=3)


def draw_line(x, y, a, b):
    pygame.draw.line(game_window, red, [x, y], [a, b], width=2)


def player_decision(box, order):
    text_emp = text.render("", True, red)
    game_window.blit(text_emp, (10, 10))
    if box == 1 and 1 not in verify_list:
        if order % 2 == 0:
            draw_x(44, 98, 122, 160)
            draw_x(44, 160, 122, 98)
            x_list.append(1)
        else:
            draw_o(78, 126)
            y_list.append(1)
    if box == 2 and 2 not in verify_list:
        if order % 2 == 0:
            draw_x(208, 98, 298, 160)
            draw_x(298, 98, 208, 160)
            x_list.append(2)
        else:
            draw_o(251, 130)
            y_list.append(2)
    if box == 3 and 3 not in verify_list:
        if order % 2 == 0:
            draw_x(369, 98, 458, 160)
            draw_x(458, 98, 369, 158)
            x_list.append(3)
        else:
            draw_o(416, 127)
            y_list.append(3)
    if box == 4 and 4 not in verify_list:
        if order % 2 == 0:
            draw_x(40, 221, 126, 281)
            draw_x(126, 221, 40, 281)
            x_list.append(4)
        else:
            draw_o(78, 250)
            y_list.append(4)
    if box == 5 and 5 not in verify_list:
        if order % 2 == 0:
            draw_x(211, 211, 303, 278)
            draw_x(298, 209, 209, 278)
            x_list.append(5)
        else:
            draw_o(248, 253)
            y_list.append(5)
    if box == 6 and 6 not in verify_list:
        if order % 2 == 0:
            draw_x(377, 220, 463, 278)
            draw_x(457, 215, 380, 280)
            x_list.append(6)
        else:
            draw_o(414, 253)
            y_list.append(6)
    if box == 7 and 7 not in verify_list:
        if order % 2 == 0:
            draw_x(40, 345, 118, 432)
            draw_x(125, 351, 34, 425)
            x_list.append(7)
        else:
            draw_o(78, 388)
            y_list.append(7)
    if box == 8 and 8 not in verify_list:
        if order % 2 == 0:
            draw_x(214, 345, 290, 421)
            draw_x(290, 345, 214, 422)
            x_list.append(8)
        else:
            draw_o(250, 388)
            y_list.append(8)
    if box == 9 and 9 not in verify_list:
        if order % 2 == 0:
            draw_x(377, 345, 450, 425)
            draw_x(450, 345, 380, 425)
            x_list.append(9)
        else:
            draw_o(417, 388)
            y_list.append(9)
    pygame.display.update()


def cout_x():
    if (1 in x_list) and (2 in x_list) and (3 in x_list):
        count_x.append(1)
    if (4 in x_list) and (5 in x_list) and (6 in x_list):
        count_x.append(1)
    if (7 in x_list) and (8 in x_list) and (9 in x_list):
        count_x.append(1)
    if (1 in x_list) and (4 in x_list) and (7 in x_list):
        count_x.append(1)
    if (2 in x_list) and (5 in x_list) and (8 in x_list):
        count_x.append(1)
    if (3 in x_list) and (6 in x_list) and (9 in x_list):
        count_x.append(1)
    if (1 in x_list) and (5 in x_list) and (9 in x_list):
        count_x.append(1)
    if (5 in x_list) and (3 in x_list) and (7 in x_list):
        count_x.append(1)


def cout_y():
    if (1 in y_list) and (2 in y_list) and (3 in y_list):
        count_y.append(1)
    if (4 in y_list) and (5 in y_list) and (6 in y_list):
        count_y.append(1)
    if (7 in y_list) and (8 in y_list) and (9 in y_list):
        count_y.append(1)
    if (1 in y_list) and (4 in y_list) and (7 in y_list):
        count_y.append(1)
    if (2 in y_list) and (5 in y_list) and (8 in y_list):
        count_y.append(1)
    if (3 in y_list) and (6 in y_list) and (9 in y_list):
        count_y.append(1)
    if (1 in y_list) and (5 in y_list) and (9 in y_list):
        count_y.append(1)
    if (5 in y_list) and (3 in y_list) and (7 in y_list):
        count_y.append(1)


def final_touch():
    if (1 in x_list) and (2 in x_list) and (3 in x_list):
        draw_line(33, 131, 463, 131)
    if (1 in y_list) and (2 in y_list) and (3 in y_list):
        draw_line(33, 131, 463, 131)
    if (4 in x_list) and (5 in x_list) and (6 in x_list):
        draw_line(33, 252, 463, 252)
    if (4 in y_list) and (5 in y_list) and (6 in y_list):
        draw_line(33, 252, 463, 252)
    if (7 in x_list) and (8 in x_list) and (9 in x_list):
        draw_line(33, 383, 470, 383)
    if (7 in y_list) and (8 in y_list) and (9 in y_list):
        draw_line(33, 383, 470, 383)
    if (1 in x_list) and (4 in x_list) and (7 in x_list):
        draw_line(79, 71, 79, 450)
    if (1 in y_list) and (4 in y_list) and (7 in y_list):
        draw_line(79, 71, 79, 450)
    if (2 in x_list) and (5 in x_list) and (8 in x_list):
        draw_line(250, 67, 250, 450)
    if (2 in y_list) and (5 in y_list) and (8 in y_list):
        draw_line(250, 67, 250, 450)
    if (3 in x_list) and (6 in x_list) and (9 in x_list):
        draw_line(415, 67, 415, 450)
    if (3 in y_list) and (6 in y_list) and (9 in y_list):
        draw_line(415, 67, 415, 450)
    if (1 in x_list) and (5 in x_list) and (9 in x_list):
        draw_line(17, 91, 485, 418)
    if (1 in y_list) and (5 in y_list) and (9 in y_list):
        draw_line(17, 91, 485, 418)
    if (5 in x_list) and (3 in x_list) and (7 in x_list):
        draw_line(472, 100, 4, 418)
    if (5 in y_list) and (3 in y_list) and (7 in y_list):
        draw_line(472, 100, 4, 418)


exit_game = 0
play_img_bool = 0
while not exit_game:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONUP:
            k = str(event).split('{')
            r = str(k).split("pos" and " ")
            pos_x = (r[3].removeprefix("(")).removesuffix(",")
            pos_y = (r[4].removesuffix(",")).removesuffix(")")
            if event.type == pygame.QUIT or len(x_list) + len(y_list) > 8:
                exit_game = 1
            else:
                box = 0
                if play_img_bool == 0:
                    game_window.blit(img, img_cir)
                    game_window.blit(img_GS_Logo, img_GS_cir)
                    game_window.blit(img_pl1_vs_pl2, img_pl1_cir)
                    game_window.blit(img_XOX_title, img_XOX_title_cir)
                    game_window.blit(img_game_ex, img_game_ex_cir)
                    game_window.blit(img1, img_cir1)
                    pygame.display.flip()
                    if cal_dis(int(pos_x), int(pos_y)) < 40:
                        box = 0
                        game_window.fill(black)
                        selection_option = 1
                        play_img_bool = 1
                    if cal_dis_fr_ex(int(pos_x), int(pos_y)) < 45:
                        exit_game = 1
                if play_img_bool == 1 and selection_option == 1 and box == 0:
                    if (int(pos_x) > 15 and int(pos_x) < 160) and (
                            int(pos_y) > 70 and int(pos_y) < 185) and 1 in verify_list:
                        box = 1
                        verify_list.remove(1)
                        draw_verify.append(1)
                        i = i + 1
                    if (int(pos_x) > 160 and int(pos_x) < 330) and (
                            int(pos_y) > 70 and int(pos_y) < 185) and 2 in verify_list:
                        box = 2
                        verify_list.remove(2)
                        draw_verify.append(2)
                        i = i + 1
                    if (int(pos_x) > 331 and int(pos_x) < 475) and (
                            int(pos_y) > 70 and int(pos_y) < 185) and 3 in verify_list:
                        box = 3
                        verify_list.remove(3)
                        draw_verify.append(3)
                        i = i + 1
                    if (int(pos_x) > 15 and int(pos_x) < 160) and (
                            int(pos_y) > 190 and int(pos_y) < 310) and 4 in verify_list:
                        box = 4
                        verify_list.remove(4)
                        draw_verify.append(4)
                        if i == -1:
                            game_window.fill(black)
                            dr_line()
                            pygame.display.update()
                            verify_list.append(4)
                            draw_verify.remove(4)
                        i = i + 1
                    if (int(pos_x) > 160 and int(pos_x) < 330) and (
                            int(pos_y) > 190 and int(pos_y) < 310) and 5 in verify_list:
                        box = 5
                        verify_list.remove(5)
                        draw_verify.append(5)
                        i = i + 1
                    if (int(pos_x) > 331 and int(pos_x) < 475) and (
                            int(pos_y) > 190 and int(pos_y) < 310) and 6 in verify_list:
                        box = 6
                        verify_list.remove(6)
                        draw_verify.append(6)
                        i = i + 1
                    if (int(pos_x) > 15 and int(pos_x) < 160) and (
                            int(pos_y) > 310 and int(pos_y) < 444) and 7 in verify_list:
                        box = 7
                        verify_list.remove(7)
                        draw_verify.append(7)
                        i = i + 1
                    if (int(pos_x) > 160 and int(pos_x) < 330) and (
                            int(pos_y) > 310 and int(pos_y) < 444) and 8 in verify_list:
                        box = 8
                        verify_list.remove(8)
                        draw_verify.append(8)
                        i = i + 1
                    if (int(pos_x) > 331 and int(pos_x) < 475) and (
                            int(pos_y) > 310 and int(pos_y) < 444) and 9 in verify_list:
                        box = 9
                        verify_list.remove(9)
                        draw_verify.append(9)
                        i = i + 1
                    dr_line()
                    player_decision(box, i)
                    box = 0

                final_touch()
            pygame.display.update()
        elif event.type == pygame.QUIT and i > 0:
            exit_game = 1
if exit_game == 1:
    cout_x()
    cout_y()
    game_window.fill(black)
    game_window.blit(img_gm_over, img_gm_over_cir)
    pygame.display.flip()
    text_turn_x = text.render("Player X --> " + str(len(count_x)), True, (255, 165, 0))
    text_turn_y = text.render("Player O --> " + str(len(count_y)), True, (0, 127, 255))
    game_window.blit(text_turn_x, (100, 200))
    game_window.blit(text_turn_y, (100, 300))
    pygame.display.update()
    time.sleep(2)
pygame.quit()
