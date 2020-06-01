import pygame, sys, time, os

os.environ["SDL_VIDEO_CENTERED"] = "1"

win_width = 900
win_height = 700
fps = 60
white = (255, 255, 255)
transparent = (255, 255, 255, 0)
black = (0, 0, 0)
grey = (150, 150, 150)
q_note = 98
w_note = 188
o_note = 278
p_note = 368


class Game:
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.fps = 60
        self.init = pygame.init()
        self.caption = pygame.display.set_caption("BYOG")
        self.screen = pygame.display.set_mode((win_width, win_height), pygame.SRCALPHA)
        self.intro = True
        self.how_2_play = self.play = self.text_load = False


class Text(pygame.sprite.Sprite):
    def __init__(self, size, text, color, xpos, ypos, count):
        pygame.sprite.Sprite.__init__(self)
        self.font = pygame.font.SysFont("Source Code Pro", size)
        self.image = self.font.render(text, 1, color)
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(xpos, ypos)
        self.score_display = 0
        self.count = count

    def perfect(self, score_number, score):
        score_number.count += 100
        score.image = score.font.render("Score: " + str(score_number.count), 1, white)
        self.score_display += 1

    def good(self, score_number, score):
        score_number.count += 50
        score.image = score.font.render("Score: " + str(score_number.count), 1, white)
        self.score_display += 1

    def ok(self, score_number, score):
        score_number.count += 25
        score.image = score.font.render("Score: " + str(score_number.count), 1, white)
        self.score_display += 1

    def miss(self, score_number, score):
        score_number.count += 0
        score.image = score.font.render("Score: " + str(score_number.count), 1, white)
        self.score_display += 1


class Outline(pygame.sprite.Sprite):
    def __init__(self, x, y, x_pos, y_pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((x, y)).convert()
        self.image.fill(white)
        self.rect = self.image.get_rect()
        self.rect = pygame.Rect(x_pos, y_pos, x, y)


class Notes(pygame.sprite.Sprite):
    def __init__(self, x_pos, y_pos, side):
        pygame.sprite.Sprite.__init__(self)
        self.width = 97
        self.height = 55
        self.image = pygame.image.load("images/q_rectangle.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.rect = self.image.get_rect()
        self.rect = pygame.Rect(x_pos, y_pos, 90, 50)
        self.close = 0
        self.type = side

    def kills(self, screen_group):
        if self.rect.top > win_height/2 + 50:
            self.image.fill(transparent)
            self.remove(screen_group)

    def moves(self, screen_group):
        self.rect.y += 7

        if 400 > self.rect.bottom > 0:
            screen_group.add(self)
        if self.rect.top > 500:
            self.remove(screen_group)

    def update(self, screen_group):

        #Perfect
        if 438 <= self.rect.top <= 462:
            self.close = 1
        #Good
        if 463 <= self.rect.top <= 480:
            self.close = 2
        if 420 <= self.rect.top <= 437:
            self.close = 2
        #Ok
        if 481 <= self.rect.top <= 499:
            self.close = 3
        if 401 <= self.rect.top <= 419:
            self.close = 3
        #Miss
        if self.rect.top >= 500:
            self.close = 4
        if self.rect.top <= 400:
            self.close = 4


def main():
    # Initial Variable
    run = Game()
    run.screen.fill(white)
    print("You might have to wait a while for the program to boot up (Wait at least 30 seconds)")
    run.clock.tick(fps)
    pygame.display.flip()
    intro_music = pygame.mixer.Sound("Sounds/intro_song.ogg")
    game_music = pygame.mixer.Sound("Sounds/back_song.ogg")

    # Create Group
    how_to_play_text_group = pygame.sprite.Group()
    how_to_play_notes_group = pygame.sprite.Group()
    note_screen_group = pygame.sprite.Group()
    bracket_group = pygame.sprite.Group()

    # Border Objects
    boundary1 = Outline(2, 600, 100, 0)
    boundary2 = Outline(2, 600, 190, 0)
    boundary3 = Outline(2, 600, 280, 0)
    boundary4 = Outline(2, 600, 370, 0)
    boundary5 = Outline(2, 600, 460, 0)
    boundary6 = Outline(360, 2, 100, 450)
    boundary7 = Outline(360, 2, 100, 500)
    boundary8 = Outline(360, 2, 100, 600)

    #Note Objects
    n1 = Notes(q_note, -2608, "q")
    n2 = Notes(p_note, -2918, "p")
    n3 = Notes(o_note, -2981, "o")

    n4 = Notes(q_note, -3580, "q")
    n5 = Notes(o_note, -3680, "o")
    n6 = Notes(w_note, -3780, "w")
    n7 = Notes(p_note, -3880, "p")
    n8 = Notes(o_note, -3980, "o")
    n9 = Notes(p_note, -4080, "p")
    n10 = Notes(w_note, -4180, "w")
    n11 = Notes(o_note, -4280, "o")
    n12 = Notes(w_note, -4380, "w")

    n13 = Notes(q_note, -4720, "q")
    n14 = Notes(w_note, -4830, "w")
    n15 = Notes(p_note, -4940, "p")
    n16 = Notes(o_note, -5050, "o")
    n17 = Notes(p_note, -5160, "p")

    n18 = Notes(w_note, -5330, "w")

    n19 = Notes(p_note, -5430, "p")
    n20 = Notes(q_note, -5540, "q")
    n21 = Notes(p_note, -5650, "p")
    n22 = Notes(w_note, -5760, "w")
    n23 = Notes(q_note, -5870, "q")
    n24 = Notes(p_note, -5980, "p")

    n25 = Notes(o_note, -6182, "o")

    n26 = Notes(p_note, -6380, "p")
    n27 = Notes(w_note, -6490, "w")
    n28 = Notes(o_note, -6600, "o")
    n29 = Notes(q_note, -6710, "q")
    n30 = Notes(p_note, -6820, "p")

    n31 = Notes(w_note, -6990, "w")

    n32 = Notes(p_note, -7090, "p")
    n33 = Notes(o_note, -7200, "o")
    n34 = Notes(p_note, -7310, "p")
    n35 = Notes(o_note, -7420, "o")
    n36 = Notes(w_note, -7530, "w")

    n37 = Notes(q_note, -7810, "q")

    n38 = Notes(w_note, -8050, "w")
    n39 = Notes(p_note, -8160, "p")
    n40 = Notes(q_note, -8270, "q")
    n41 = Notes(w_note, -8380, "w")
    n42 = Notes(p_note, -8490, "p")

    n43 = Notes(q_note, -8660, "q")

    n44 = Notes(w_note, -8760, "w")
    n45 = Notes(o_note, -8870, "o")
    n46 = Notes(q_note, -8980, "q")
    n47 = Notes(p_note, -9090, "p")
    n48 = Notes(o_note, -9200, "o")
    n49 = Notes(w_note, -9310, "w")

    n50 = Notes(p_note, -9480, "p")

    n51 = Notes(w_note, -9678, "w")
    n52 = Notes(o_note, -9788, "o")
    n53 = Notes(q_note, -9898, "q")
    n54 = Notes(p_note, -10008, "p")
    n55 = Notes(o_note, -10118, "o")

    n56 = Notes(p_note, -10288, "p")

    n57 = Notes(q_note, -10388, "q")
    n58 = Notes(o_note, -10498, "o")
    n59 = Notes(p_note, -10608, "p")
    n60 = Notes(o_note, -10718, "o")
    n61 = Notes(w_note, -10828, "w")
    n62 = Notes(p_note, -10938, "p")

    n63 = Notes(o_note, -11420, "o")
    n64 = Notes(w_note, -11520, "w")
    n65 = Notes(q_note, -11620, "q")
    n66 = Notes(o_note, -11720, "o")
    n67 = Notes(p_note, -11820, "p")
    n68 = Notes(q_note, -11920, "q")
    n69 = Notes(w_note, -12020, "w")
    n70 = Notes(o_note, -12120, "o")
    n71 = Notes(q_note, -12220, "q")
    n72 = Notes(p_note, -12320, "p")
    n73 = Notes(q_note, -12420, "q")
    n74 = Notes(o_note, -12520, "o")
    n75 = Notes(p_note, -12620, "p")
    n76 = Notes(q_note, -12720, "q")
    n77 = Notes(w_note, -12820, "w")
    n78 = Notes(p_note, -12920, "p")
    n79 = Notes(o_note, -13020, "o")
    n80 = Notes(w_note, -13120, "w")
    n81 = Notes(q_note, -13220, "q")
    n82 = Notes(p_note, -13320, "p")
    n83 = Notes(q_note, -13420, "q")
    n84 = Notes(w_note, -13520, "w")
    n85 = Notes(o_note, -13620, "o")
    n86 = Notes(w_note, -13720, "w")
    n87 = Notes(p_note, -13820, "p")
    n88 = Notes(q_note, -13920, "q")
    n89 = Notes(w_note, -14020, "w")
    n90 = Notes(o_note, -14120, "o")
    n91 = Notes(q_note, -14220, "q")
    n92 = Notes(o_note, -14320, "o")
    n93 = Notes(p_note, -14420, "p")
    n94 = Notes(w_note, -14520, "w")
    n95 = Notes(q_note, -14620, "q")
    n96 = Notes(o_note, -14720, "o")
    n97 = Notes(w_note, -14820, "w")
    n98 = Notes(q_note, -14920, "q")
    n99 = Notes(p_note, -15020, "p")
    n100 = Notes(w_note, -15120, "w")
    n101 = Notes(o_note, -15220, "o")
    n102 = Notes(q_note, -15320, "q")
    n103 = Notes(o_note, -15420, "o")
    n104 = Notes(p_note, -15520, "p")
    n105 = Notes(w_note, -15620, "w")
    n106 = Notes(q_note, -15720, "q")
    n107 = Notes(p_note, -15820, "p")
    n108 = Notes(q_note, -15920, "q")
    n109 = Notes(p_note, -16020, "p")
    n110 = Notes(o_note, -16120, "o")
    n111 = Notes(w_note, -16220, "w")
    n112 = Notes(p_note, -16320, "p")
    n113 = Notes(q_note, -16420, "q")
    n114 = Notes(o_note, -16520, "o")
    n115 = Notes(p_note, -16620, "p")
    n116 = Notes(w_note, -16720, "w")
    n117 = Notes(p_note, -16820, "p")
    n118 = Notes(o_note, -16920, "o")
    n119 = Notes(w_note, -17020, "w")
    n120 = Notes(q_note, -17120, "q")
    n121 = Notes(p_note, -17220, "p")
    n122 = Notes(w_note, -17320, "w")

    n123 = Notes(o_note, -17800, "o")
    n124 = Notes(q_note, -18150, "q")

    n125 = Notes(p_note, -20300, "p")
    n126 = Notes(w_note, -20562, "w")
    n127 = Notes(p_note, -20742, "p")
    n128 = Notes(q_note, -20802, "q")
    n129 = Notes(o_note, -20862, "o")
    n130 = Notes(q_note, -21112, "q")
    n131 = Notes(w_note, -21322, "w")

    n132 = Notes(o_note, -21532, "o")
    n133 = Notes(q_note, -21627, "q")
    n134 = Notes(w_note, -21712, "w")
    n135 = Notes(q_note, -21797, "q")
    n136 = Notes(p_note, -21882, "p")

    n137 = Notes(q_note, -22052, "q")
    n138 = Notes(o_note, -22314, "o")
    n139 = Notes(p_note, -22494, "p")
    n140 = Notes(q_note, -22554, "q")
    n141 = Notes(w_note, -22614, "w")
    n142 = Notes(q_note, -22864, "q")

    n143 = Notes(o_note, -23084, "o")
    n144 = Notes(q_note, -23154, "q")
    n145 = Notes(w_note, -23224, "w")
    n146 = Notes(o_note, -23294, "o")
    n147 = Notes(p_note, -23364, "p")

    n148 = Notes(o_note, -23534, "o")
    n149 = Notes(q_note, -23854, "q")
    n150 = Notes(w_note, -24009, "w")
    n151 = Notes(p_note, -24299, "p")
    n152 = Notes(q_note, -24349, "q")
    n153 = Notes(o_note, -24399, "o")

    n154 = Notes(w_note, -24650, "w")
    n155 = Notes(q_note, -24700, "q")
    n156 = Notes(o_note, -24750, "o")
    n157 = Notes(p_note, -24800, "p")
    n158 = Notes(o_note, -24850, "o")

    n159 = Notes(q_note, -25020, "q")
    n160 = Notes(w_note, -25305, "w")
    n161 = Notes(p_note, -25447, "p")
    n162 = Notes(q_note, -25710, "q")
    n163 = Notes(o_note, -25750, "o")

    n164 = Notes(w_note, -25950, "w")
    n165 = Notes(q_note, -26010, "q")
    n166 = Notes(o_note, -26070, "o")
    n167 = Notes(p_note, -26140, "p")
    n168 = Notes(o_note, -26210, "o")

    n169 = Notes(w_note, -26470, "w")
    n170 = Notes(q_note, -26600, "q")
    n171 = Notes(o_note, -26870, "o")
    n172 = Notes(p_note, -26920, "p")
    n173 = Notes(w_note, -27020, "w")
    n174 = Notes(q_note, -27120, "q")

    n175 = Notes(w_note, -27320, "w")
    n176 = Notes(q_note, -27370, "q")
    n177 = Notes(o_note, -27420, "o")
    n178 = Notes(p_note, -27470, "p")
    n179 = Notes(o_note, -27520, "o")

    n180 = Notes(w_note, -27750, "w")
    n181 = Notes(o_note, -27880, "o")
    n182 = Notes(q_note, -28150, "q")
    n183 = Notes(w_note, -28250, "w")
    n184 = Notes(o_note, -28350, "o")

    n185 = Notes(p_note, -28580, "p")
    n186 = Notes(o_note, -28635, "o")
    n187 = Notes(q_note, -28690, "q")
    n188 = Notes(w_note, -28745, "w")
    n189 = Notes(p_note, -28800, "p")

    n190 = Notes(w_note, -29030, "w")
    n191 = Notes(q_note, -29160, "q")
    n192 = Notes(o_note, -29415, "o")
    n193 = Notes(p_note, -29465, "p")
    n194 = Notes(w_note, -29565, "w")
    n195 = Notes(q_note, -29665, "q")

    n196 = Notes(o_note, -29790, "o")
    n197 = Notes(p_note, -29845, "p")
    n198 = Notes(q_note, -29900, "q")
    n199 = Notes(w_note, -29955, "w")
    n200 = Notes(q_note, -30010, "q")

    n201 = Notes(p_note, -30180, "p")
    n202 = Notes(q_note, -30300, "q")
    n203 = Notes(w_note, -30560, "w")
    n204 = Notes(p_note, -30660, "p")
    n205 = Notes(q_note, -30760, "q")

    n206 = Notes(o_note, -30885, "o")
    n207 = Notes(p_note, -30935, "p")
    n208 = Notes(w_note, -30985, "w")
    n209 = Notes(q_note, -31035, "q")
    n210 = Notes(p_note, -31085, "p")

    n211 = Notes(w_note, -35650, "w")
    n212 = Notes(o_note, -35725, "o")
    n213 = Notes(q_note, -35800, "q")

    n214 = Notes(p_note, -36450, "p")
    n215 = Notes(w_note, -36525, "w")
    n216 = Notes(q_note, -36600, "q")

    n217 = Notes(p_note, -36925, "p")
    n218 = Notes(o_note, -37000, "o")
    n219 = Notes(p_note, -37075, "p")

    n220 = Notes(o_note, -37250, "o")
    n221 = Notes(q_note, -37325, "q")
    n222 = Notes(w_note, -37400, "w")

    n223 = Notes(w_note, -38050, "w")
    n224 = Notes(q_note, -38125, "q")
    n225 = Notes(p_note, -38200, "p")

    n226 = Notes(w_note, -38525, "w")
    n227 = Notes(o_note, -38600, "o")
    n228 = Notes(q_note, -38675, "q")

    n229 = Notes(q_note, -40675, "q")

    n230 = Notes(p_note, -41095, "p")
    n231 = Notes(w_note, -41305, "w")
    n232 = Notes(o_note, -41515, "o")

    n233 = Notes(w_note, -41935, "w")
    n234 = Notes(q_note, -42145, "q")
    n235 = Notes(o_note, -42355, "o")

    n236 = Notes(w_note, -42775, "w")
    n237 = Notes(p_note, -42985, "p")
    n238 = Notes(q_note, -43195, "q")
    n239 = Notes(o_note, -43405, "o")
    n240 = Notes(w_note, -43615, "w")
    n241 = Notes(p_note, -43825, "p")
    n242 = Notes(o_note, -44035, "o")

    n243 = Notes(w_note, -44455, "w")
    n244 = Notes(q_note, -44665, "q")
    n245 = Notes(p_note, -44875, "p")
    n246 = Notes(w_note, -45085, "w")
    n247 = Notes(o_note, -45295, "o")

    n248 = Notes(p_note, -45715, "p")
    n249 = Notes(o_note, -46515, "o")
    n250 = Notes(q_note, -46935, "q")
    n251 = Notes(w_note, -47145, "w")
    n252 = Notes(p_note, -47355, "p")

    n253 = Notes(q_note, -47555, "q")

    n254 = Notes(p_note, -47955, "p")
    n255 = Notes(w_note, -48155, "w")
    n256 = Notes(q_note, -48355, "q")

    n257 = Notes(p_note, -48755, "p")
    n258 = Notes(o_note, -48955, "o")
    n259 = Notes(w_note, -49155, "w")

    n260 = Notes(q_note, -49555, "q")
    n261 = Notes(p_note, -49755, "p")
    n262 = Notes(w_note, -49955, "w")
    n263 = Notes(o_note, -50155, "o")
    n264 = Notes(q_note, -50355, "q")
    n265 = Notes(w_note, -50555, "w")
    n266 = Notes(q_note, -50755, "q")

    n267 = Notes(o_note, -51155, "o")
    n268 = Notes(q_note, -51355, "q")
    n269 = Notes(o_note, -51555, "o")
    n270 = Notes(w_note, -51755, "w")
    n271 = Notes(p_note, -51955, "p")

    n272 = Notes(w_note, -52355, "w")
    n273 = Notes(o_note, -53155, "o")
    n274 = Notes(p_note, -53555, "p")
    n275 = Notes(q_note, -53755, "q")
    n276 = Notes(w_note, -53955, "w")

    #Last Note yeeeee
    n277 = Notes(o_note, -57400, "o")

    note_all_array = [n1, n2, n3, n4, n5, n6, n7, n8, n9, n10, n11, n12, n13, n14, n15, n16, n17, n18, n19, n20, n21, n22, n23, n24, n25, n26, n27, n28, n29, n30, n31, n32, n33, n34, n35, n36, n37, n38, n39, n40, n41, n42, n43, n44, n45, n46, n47, n48, n49, n50, n51, n52, n53, n54, n55, n56, n57, n58, n59, n60, n61, n62, n63, n64, n65, n66, n67, n68, n69, n70, n71, n72, n73, n74, n75, n76, n77, n78, n79, n80, n81, n82, n83, n84, n85, n86, n87, n88, n89, n90, n91, n92, n93, n94, n95, n96, n97, n98, n99, n100, n101, n102, n103, n104, n105, n106, n107, n108, n109, n110, n111, n112, n113, n114, n115, n116, n117, n118, n119, n120, n121, n122, n123, n124, n125, n126, n127, n128, n129, n130, n131, n132, n133, n134, n135, n136, n137, n138, n139, n140, n141, n142, n143, n144, n145, n146, n147, n148, n149, n150, n151, n152, n153, n154, n155, n156, n157, n158, n159, n160, n161, n162, n163, n164, n165, n166, n167, n168, n169, n170, n171, n172, n173, n174, n175, n176, n177, n178, n179, n180, n181, n182, n183, n184, n185, n186, n187, n188, n189, n190, n191, n192, n193, n194, n195, n196, n197, n198, n199, n200, n201, n202, n203, n204, n205, n206, n207, n208, n209, n210, n211, n212, n213, n214, n215, n216, n217, n218, n219, n220, n221, n222, n223, n224, n225, n226, n227, n228, n229, n230, n231, n232, n233, n234, n235, n236, n237, n238, n239, n240, n241, n242, n243, n244, n245, n246, n247, n248, n249, n250, n251, n252, n253, n254, n255, n256, n257, n258, n259, n260, n261, n262, n263, n264, n265, n266, n267, n268, n269, n270, n271, n272, n273, n274, n275, n276, n277]

    intro_back = pygame.image.load("images/intro_back.jpg")
    intro_back = pygame.transform.scale(intro_back, (win_width, win_height))
    intro_rect = intro_back.get_rect()

    play_back = pygame.image.load("images/background_game.jpg")
    play_back = pygame.transform.scale(play_back, (win_width, win_height))
    play_rect = play_back.get_rect()

    start_button = Text(75, "Start", white, win_width / 5 + 210, win_height / 2 + 175, 0)
    start = run.screen.blit(start_button.image, start_button.rect)
    how_to_play = Text(75, "How to Play", white, win_width / 5 + 125, win_height / 2 + 250, 0)
    question = run.screen.blit(how_to_play.image, how_to_play.rect)
    how_to_play_back = Text(75, "Play Game >>", black, win_width / 20, win_height - 75, 0)
    play_game = run.screen.blit(how_to_play_back.image, how_to_play_back.rect)

    intro_title = Text(150, "Osu!Mania", white, win_width / 5, win_height / 2 - 250, 0)
    how_to_play_title1 = Text(100, "How to Play", black, win_width / 2 + 30, win_height / 20, 0)
    how_to_play_title2 = Text(100, "__________", black, win_width / 2 + 30, win_height / 17, 0)
    how_to_play_script1 = Text(30, "This is a rhythm game where notes rain", black, win_width / 2 + 25, win_height / 2 - 220, 0)
    how_to_play_script2 = Text(30, "from the sky, and you time them", black, win_width / 2 + 25, win_height / 2 - 180, 0)
    how_to_play_script3 = Text(30, "accordingly with the music to its column", black, win_width / 2 + 25, win_height / 2 - 140, 0)
    how_to_play_script4 = Text(30, " in order to clear the note. You will be", black, win_width / 2 + 25, win_height / 2 - 100, 0)
    how_to_play_script5 = Text(30, "granted a score depending on your timing.", black, win_width / 2 + 25, win_height / 2 - 60, 0)
    how_to_play_script6 = Text(30, "The better the timing, the higher your score.", black, win_width / 2 + 25, win_height / 2 - 20, 0)
    how_to_play_script7 = Text(30, "It’s like playing a piano, except in a video", black, win_width / 2 + 25, win_height / 2 + 20, 0)
    how_to_play_script8 = Text(30, "game…       Good luck / Have fun!", black, win_width / 2 + 25, win_height / 2 + 60, 0)
    how_to_play_control = Text(100, "Controls: ", black, win_width / 2 + 30, win_height / 2 + 175, 0)
    how_to_play_control_button = Text(115, "Q  W  O  P", white, win_width / 2 + 30, win_height / 2 + 250, 0)

    how_to_play_note1 = Notes(p_note, 450, "p")
    how_to_play_note2 = Notes(q_note, 200, "q")
    how_to_play_note3 = Notes(o_note, 0, "o")

    score = Text(75, "Score: " + str(start_button.score_display), white, win_width / 2 + 75, win_height - 100, 0)
    score_number = Text(75, "Hi", white, win_width / 2 + 200, win_height + 100, 0)

    how_to_play_notes_group.add(how_to_play_note1, how_to_play_note2, how_to_play_note3)
    how_to_play_text_group.add(how_to_play_title1, how_to_play_title2, how_to_play_script1, how_to_play_script2, how_to_play_script3, how_to_play_script4, how_to_play_script5, how_to_play_script6, how_to_play_script7, how_to_play_script8, how_to_play_control, how_to_play_control_button)
    bracket_group.add(boundary1, boundary2, boundary3, boundary4, boundary5, boundary6, boundary7, boundary8)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

    intro_music.play(-1)
    intro_music.set_volume(0.3)

    while run.intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONUP:
                mouse = pygame.mouse.get_pos()
                if question.collidepoint(mouse):
                    run.intro = False
                    run.how_2_play = True
                elif start.collidepoint(mouse):
                    run.intro = False
                    run.play = True
                    intro_music.stop()
                    game_music.play(0)
                    game_music.set_volume(0.3)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        run.screen.blit(intro_back, intro_rect)
        run.screen.blit(start_button.image, start_button.rect)
        run.screen.blit(intro_title.image, intro_title.rect)
        run.screen.blit(how_to_play.image, how_to_play.rect)

        run.clock.tick(fps)
        pygame.display.flip()

    while run.how_2_play:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                if play_game.collidepoint(mouse):
                    run.how_2_play = False
                    run.play = True
                    intro_music.stop()
                    game_music.play(0)
                    game_music.set_volume(0.3)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        run.screen.fill(grey)
        run.screen.blit(how_to_play_back.image, how_to_play_back.rect)
        how_to_play_text_group.draw(run.screen)
        how_to_play_notes_group.draw(run.screen)
        bracket_group.draw(run.screen)

        run.clock.tick(fps)
        pygame.display.flip()

    while run.play:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                for n in note_screen_group:
                    if event.key == pygame.K_q:
                        if n.close == 1 and n.type == "q":
                            n.kills(note_screen_group)
                            score.perfect(score_number, score)
                        elif n.close == 2 and n.type == "q":
                            n.kills(note_screen_group)
                            score.good(score_number, score)
                        elif n.close == 3 and n.type == "q":
                            n.kills(note_screen_group)
                            score.ok(score_number, score)
                        elif n.close == 4 and n.type == "q":
                            n.kills(note_screen_group)
                            score.miss(score_number, score)
                    elif event.type == pygame.KEYDOWN and event.key == pygame.K_w:
                        if n.close == 1 and n.type == "w":
                            n.kills(note_screen_group)
                            score.perfect(score_number, score)
                        elif n.close == 2 and n.type == "w":
                            n.kills(note_screen_group)
                            score.good(score_number, score)
                        elif n.close == 3 and n.type == "w":
                            n.kills(note_screen_group)
                            score.ok(score_number, score)
                        elif n.close == 4 and n.type == "w":
                            n.kills(note_screen_group)
                            score.miss(score_number, score)
                    elif event.type == pygame.KEYDOWN and event.key == pygame.K_o:
                        if n.close == 1 and n.type == "o":
                            n.kills(note_screen_group)
                            score.perfect(score_number, score)
                        elif n.close == 2 and n.type == "o":
                            n.kills(note_screen_group)
                            score.good(score_number, score)
                        elif n.close == 3 and n.type == "o":
                            n.kills(note_screen_group)
                            score.ok(score_number, score)
                        elif n.close == 4 and n.type == "o":
                            n.kills(note_screen_group)
                            score.miss(score_number, score)
                    elif event.type == pygame.KEYDOWN and event.key == pygame.K_p:
                        if n.close == 1 and n.type == "p":
                            n.kills(note_screen_group)
                            score.perfect(score_number, score)
                        elif n.close == 2 and n.type == "p":
                            n.kills(note_screen_group)
                            score.good(score_number, score)
                        elif n.close == 3 and n.type == "p":
                            n.kills(note_screen_group)
                            score.ok(score_number, score)
                        elif n.close == 4 and n.type == "p":
                            n.kills(note_screen_group)
                            score.miss(score_number, score)

        for n in note_all_array:
            n.moves(note_screen_group)
            n.update(note_screen_group)

        run.screen.blit(play_back, play_rect)
        run.screen.blit(score.image, score.rect)
        note_screen_group.draw(run.screen)

        bracket_group.draw(run.screen)
        run.clock.tick(fps)
        pygame.display.flip()


if __name__ == "__main__":
    while True:
        main()
