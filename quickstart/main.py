from manim import *


class Quickstart(Scene):

    def welcome(self):
        title = Tex(r"Quickstart with Manim", font_size=96)
        subtitle = Tex(r"by Antonio Bernardini", font_size=48)

        subtitle.next_to(title, DOWN, buff=0.5)

        self.play(Write(title))
        self.play(Write(subtitle))
        self.wait()
        self.play(FadeOut(title), FadeOut(subtitle))
    
    def createCircle(self):
        title = Tex(r"Create Circle", font_size=96)
        circle = Circle(color=WHITE)

        self.play(Write(title))
        self.wait()
        self.play(FadeOut(title))

        self.play(Create(circle))
        self.wait()
        self.play(FadeOut(circle))

    def squareToCircle(self):
        title = Tex(r"Square To Circle", font_size=96)
        circle = Circle(color=WHITE)
        square = Square()
        square.rotate(PI / 4)

        self.play(Write(title))
        self.wait()
        self.play(FadeOut(title))

        self.play(Create(square))
        self.play(Transform(square, circle))
        self.wait()
        self.play(FadeOut(square))
    
    def squareAndCircle(self):
        title = Tex(r"Square And Circle", font_size=96)
        circle = Circle()
        circle.set_fill(color=RED, opacity=0.5)
        square = Square()
        square.set_fill(color=BLUE, opacity=0.5)
        square.next_to(circle, RIGHT, buff=0.5)
        
        self.play(Write(title))
        self.wait()
        self.play(FadeOut(title))

        self.play(Create(circle), Create(square))
        self.wait()
        self.play(FadeOut(circle), FadeOut(square))
    
    def animatedSquareToCircle(self):
        title = Tex(r"Animated Square To Circle", font_size=96)
        circle = Circle()
        square = Square()

        self.play(Write(title))
        self.wait()
        self.play(FadeOut(title))

        self.play(Create(square))
        self.play(square.animate.rotate(PI / 4))
        self.play(Transform(square, circle))
        self.play(square.animate.set_fill(RED, opacity=0.5))
        self.wait()
        self.play(FadeOut(square))
    
    def differentRotations(self):
        # If you find that your own usage of `.animate` is causing similar unwanted behavior,
        # consider using conventional animation methods like the right square, which uses `Rotate`.
        title = Tex(r"Different Rotations", font_size=96)
        left_square = Square(color=BLUE, fill_opacity=0.7).shift(2 * LEFT)
        right_square = Square(color=GREEN, fill_opacity=0.7).shift(2 * RIGHT)

        self.play(Write(title))
        self.wait()
        self.play(FadeOut(title))

        self.play(left_square.animate.rotate(PI), Rotate(right_square, angle=PI), run_time=2)
        self.wait()
        self.play(FadeOut(left_square), FadeOut(right_square))
    
    def transform(self):
        title = Tex(r"Transform", font_size=96)
        a = Circle()
        b = Square()
        c = Triangle()
        
        self.play(Write(title))
        self.wait()
        self.play(FadeOut(title))
        
        self.play(Transform(a, b))
        self.play(Transform(a, c))
        self.wait()
        self.play(FadeOut(a))

    def replacementTransform(self):
        title = Tex(r"Replacement Transform", font_size=96)
        a = Circle()
        b = Square()
        c = Triangle()

        self.play(Write(title))
        self.wait()
        self.play(FadeOut(title))

        self.play(ReplacementTransform(a, b))
        self.play(ReplacementTransform(b, c))
        self.wait()
        self.play(FadeOut(c))
    
    def transformCycle(self):
        title = Tex(r"Transform Cycle", font_size=96)
        a = Circle()
        t1 = Square()
        t2 = Triangle()

        self.play(Write(title))
        self.wait()
        self.play(FadeOut(title))
        
        self.add(a)
        for t in [t1, t2]:
            self.play(Transform(a, t))
        self.wait()
        self.play(FadeOut(a))
    
    def end(self):
        the_end = Tex(r"The End", font_size=96)
        self.play(Write(the_end))
        self.wait()
        self.play(FadeOut(the_end))
    
    def construct(self):
        self.welcome()
        self.createCircle()
        self.squareToCircle()
        self.squareAndCircle()
        self.animatedSquareToCircle()
        self.differentRotations()
        self.transform()
        self.replacementTransform()
        self.transformCycle()
        self.end()
