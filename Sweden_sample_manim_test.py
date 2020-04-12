#!/usr/bin/env python
#Usage "python3 -m manim Sweden_sample_manim_test.py Test -pl"
from manimlib.imports import *

HEAD_INDEX = 0
BODY_INDEX = 0
ARMS_INDEX = 0
LEGS_INDEX = 0


class Test(Scene):
    def construct(self):
        square_c = Square(color=BLUE)
        #Area defination
        square = Square(fill_color=GOLD_B, fill_opacity=1, color=BLUE)
        square1 = Square(color=RED)
        square2= Square(color=GREEN)
        v_cities_square = VGroup(square, square1, square2)
        # Names defination
        country_name = TextMobject('Sweden', color=RED)
        country_name.scale(2)
        city_name = TextMobject('Stockhom', color=RED)
        city_name1 = TextMobject('Malmo', color=RED)
        city_name2 = TextMobject('Lund', color=RED)
        #Group cities together
        v_cities_names = VGroup(city_name, city_name1, city_name2)

        # Display People
        man = StickMan()
        man1 = StickMan()
        man2 = StickMan()
        v_people = VGroup(man, man1, man2)

        #square_c.surround(v_cities_square, v_cities_names, v_people)
        self.play(Write(square_c))

        # self.play(ShowCreation(first_line))
        # Display Country on top with UP
        country_name.to_edge(UP)
        self.play(Write(country_name))

        # Display City below the country
        city_name.next_to(country_name, LEFT + DOWN * 4)
        # Display Area below City name
        square.next_to(city_name, DOWN)
        #Display man outside city area
        self.play(ShowCreation(StickMan().next_to(square, DOWN)))
        # Display man inside the city area
        man.surround(square)
        #self.play(Write(city_name), Write(square))
        # Display City1 right side of another city
        city_name1.next_to(city_name, RIGHT * 4)
        square1.next_to(city_name1, DOWN)
        self.play(ShowCreation(StickMan().next_to(square1, DOWN)))
        man1.surround(square1)
        #self.play(Write(city_name1), Write(square1))
        # Display City2
        city_name2.next_to(city_name1, RIGHT * 4)
        square2.next_to(city_name2, DOWN)
        #man2.next_to(square2, DOWN)
        self.play(ShowCreation(StickMan().next_to(square2, DOWN)))
        man2.surround(square2)
        #Keep cities inside country
        square_c.surround(v_cities_square)
        #self.play(ShowCreation(square_c))
        #self.wait(3)
        self.play(ShowCreation(v_cities_names), ShowCreation(v_cities_square))
        #waving_man = StickMan("wave")
        #self.add(start_man)
        #self.play(Transform(start_man, plain_man))
        self.play(ShowCreation(v_people))

        #self.wait()
        # self.play(ReplacementTransform(square, square1))

class StickMan(SVGMobject):
    CONFIG = {
        "color": BLUE_E,
        "file_name_prefix": "PiCreatures",
        "stroke_width": 0.5,
        "stroke_color": WHITE,
        "fill_opacity": 1.0,
        "height": 1,
    }

    def __init__(self, mode="plain",
                 SVG_IMAGE_DIR="manimlib/files/",
                 **kwargs):
        #PiCreatures_plain.svg
        digest_config(self, kwargs)
        self.mode = mode
        #self.parts_named = True
        self.parts_named = False
        try:
            svg_file = os.path.join(
                SVG_IMAGE_DIR,
                "%s_%s.svg" % (self.file_name_prefix, mode)
            )
            SVGMobject.__init__(self, file_name=svg_file, **kwargs)
        except:
            warnings.warn("No %s design with mode %s" %
                          (self.file_name_prefix, mode))
            svg_file = os.path.join(
                SVG_IMAGE_DIR,
                "PiCreatures_plain.svg",
            )
            SVGMobject.__init__(self, mode="plain", file_name=svg_file, **kwargs)

    def name_parts(self):
        self.head = self.submobjects[HEAD_INDEX]
        self.body = self.submobjects[BODY_INDEX]
        self.arms = self.submobjects[ARMS_INDEX]
        self.legs = self.submobjects[LEGS_INDEX]
        self.parts_named = True

    def init_colors(self):
        SVGMobject.init_colors(self)
        if not self.parts_named:
            self.name_parts()
        #self.head.set_fill(self.color, opacity=1)
        #self.body.set_fill(RED, opacity=1)
        #self.arms.set_fill(YELLOW, opacity=1)
        #self.legs.set_fill(BLUE, opacity=1)
        return self