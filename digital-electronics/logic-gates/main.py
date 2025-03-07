from manim import *


class Welcome(Scene):

    def construct(self):
        title = Tex(r"Logic Gates", font_size=96)
        subtitle = Tex(r"by Antonio Bernardini", font_size=48)

        subtitle.next_to(title, DOWN, buff=0.5)

        self.play(Write(title))
        self.play(Write(subtitle))
        self.wait()
        self.play(FadeOut(title), FadeOut(subtitle))


class LogicGates(Scene):

    def animateMoveTo(self, gate, coords):
        self.play(gate.animate.move_to(coords).scale(0.6))

    def drawANDSymbol(self):
        self.and_up_hor = Line(start=[0, 1, 0], end=[-1, 1, 0])
        self.and_down_hor = Line(start=[0, -1, 0], end=[-1, -1, 0])
        self.and_ver = Line(start=[-1, 1, 0], end=[-1, -1, 0])
        self.and_arc = Arc(radius=1.0, start_angle=-PI/2, angle=PI)
        self.and_text = Tex(r"AND").shift(0.125 * LEFT)
        self.and_gate = Group(self.and_up_hor, self.and_down_hor, self.and_ver, self.and_arc, self.and_text)
        self.play(
            Create(self.and_up_hor),
            Create(self.and_down_hor),
            Create(self.and_ver),
            Create(self.and_arc),
            run_time=1
        )
        self.play(Write(self.and_text))
        self.add(self.and_gate)

    def drawORSymbol(self):
        self.or_up_arc = ArcBetweenPoints(start=[-1, -1, 0], end=[1, 0, 0], angle=PI/4)
        self.or_down_arc = ArcBetweenPoints(start=[-1, 1, 0], end=[1, 0, 0], angle=-PI/4)
        self.or_left_arc = ArcBetweenPoints(start=[-1, 1, 0], end=[-1, -1, 0], angle=-PI/3)
        self.or_text = Tex(r"OR")
        self.or_gate = Group(self.or_up_arc, self.or_down_arc, self.or_left_arc, self.or_text)
        self.play(
            Create(self.or_up_arc),
            Create(self.or_down_arc),
            Create(self.or_left_arc),
            run_time=1
        )
        self.play(Write(self.or_text))
        self.add(self.or_gate)

    def drawNOTSymbol(self):
        self.not_triangle = Polygon([1 - np.sqrt(3), 1, 0], [1 - np.sqrt(3), -1, 0], [1, 0, 0], color=WHITE)
        self.not_circle = Circle(radius=0.2, color=WHITE).move_to([1.25, 0, 0])
        self.not_text = Tex(r"NOT").scale(0.8)
        self.not_gate = Group(self.not_triangle, self.not_circle, self.not_text)
        self.play(
            Create(self.not_triangle),
            Create(self.not_circle),
            run_time=1
        )
        self.play(Write(self.not_text))
        self.add(self.not_gate)

    def drawBufferSymbol(self):
        self.buffer_triangle = Polygon([1 - np.sqrt(3), 1, 0], [1 - np.sqrt(3), -1, 0], [1, 0, 0], color=WHITE)
        self.buffer_text = Tex(r"BUFFER").scale(0.5)
        self.buffer_gate = Group(self.buffer_triangle, self.buffer_text)
        self.play(
            Create(self.buffer_triangle),
            run_time=1
        )
        self.play(Write(self.buffer_text))
        self.add(self.buffer_gate)
    
    def drawNANDSymbol(self):
        self.nand_up_hor = Line(start=[0, 1, 0], end=[-1, 1, 0])
        self.nand_down_hor = Line(start=[0, -1, 0], end=[-1, -1, 0])
        self.nand_ver = Line(start=[-1, 1, 0], end=[-1, -1, 0])
        self.nand_arc = Arc(radius=1.0, start_angle=-PI/2, angle=PI)
        self.nand_cir = Circle(radius=0.2, color=WHITE).move_to([1.2, 0, 0])
        self.nand_text = Tex(r"NAND")
        self.nand_gate = Group(self.nand_up_hor, self.nand_down_hor, self.nand_ver, self.nand_arc, self.nand_cir, self.nand_text)
        self.play(
            Create(self.nand_up_hor),
            Create(self.nand_down_hor),
            Create(self.nand_ver),
            Create(self.nand_arc),
            Create(self.nand_cir),
            run_time=1
        )
        self.play(Write(self.nand_text))
        self.add(self.nand_gate)
    
    def drawNORSymbol(self):
        self.nor_up_arc = ArcBetweenPoints(start=[-1, -1, 0], end=[1, 0, 0], angle=PI/4)
        self.nor_down_arc = ArcBetweenPoints(start=[-1, 1, 0], end=[1, 0, 0], angle=-PI/4)
        self.nor_left_arc = ArcBetweenPoints(start=[-1, 1, 0], end=[-1, -1, 0], angle=-PI/3)
        self.nor_cir = Circle(radius=0.2, color=WHITE).move_to([1.2, 0, 0])
        self.nor_text = Tex(r"NOR")
        self.nor_gate = Group(self.nor_up_arc, self.nor_down_arc, self.nor_left_arc, self.nor_cir, self.nor_text)
        self.play(
            Create(self.nor_up_arc),
            Create(self.nor_down_arc),
            Create(self.nor_left_arc),
            Create(self.nor_cir),
            run_time=1
        )
        self.play(Write(self.nor_text))
        self.add(self.nor_gate)

    def drawXORSymbol(self):
        self.xor_up_arc = ArcBetweenPoints(start=[-1, -1, 0], end=[1, 0, 0], angle=PI/4)
        self.xor_down_arc = ArcBetweenPoints(start=[-1, 1, 0], end=[1, 0, 0], angle=-PI/4)
        self.xor_left_arc = ArcBetweenPoints(start=[-1, 1, 0], end=[-1, -1, 0], angle=-PI/3)
        self.xor_second_left_arc = ArcBetweenPoints(start=[-1, 1, 0], end=[-1, -1, 0], angle=-PI/3).shift(0.2 * LEFT)
        self.xor_text = Tex(r"XOR")
        self.xor_gate = Group(self.xor_up_arc, self.xor_down_arc, self.xor_left_arc, self.xor_second_left_arc, self.xor_text)
        self.play(
            Create(self.xor_up_arc),
            Create(self.xor_down_arc),
            Create(self.xor_left_arc),
            Create(self.xor_second_left_arc),
            run_time=1
        )
        self.play(Write(self.xor_text))
        self.add(self.xor_gate)
    
    def drawXNORSymbol(self):
        self.xnor_up_arc = ArcBetweenPoints(start=[-1, -1, 0], end=[1, 0, 0], angle=PI/4)
        self.xnor_down_arc = ArcBetweenPoints(start=[-1, 1, 0], end=[1, 0, 0], angle=-PI/4)
        self.xnor_left_arc = ArcBetweenPoints(start=[-1, 1, 0], end=[-1, -1, 0], angle=-PI/3)
        self.xnor_second_left_arc = ArcBetweenPoints(start=[-1, 1, 0], end=[-1, -1, 0], angle=-PI/3).shift(0.2 * LEFT)
        self.xnor_cir = Circle(radius=0.2, color=WHITE).move_to([1.2, 0, 0])
        self.xnor_text = Tex(r"XNOR").scale(0.8)
        self.xnor_gate = Group(self.xnor_up_arc, self.xnor_down_arc, self.xnor_left_arc, self.xnor_second_left_arc, self.xnor_cir, self.xnor_text)
        self.play(
            Create(self.xnor_up_arc),
            Create(self.xnor_down_arc),
            Create(self.xnor_left_arc),
            Create(self.xnor_second_left_arc),
            Create(self.xnor_cir),
            run_time=1
        )
        self.play(Write(self.xnor_text))
        self.add(self.xnor_gate)
    
    def construct(self):
        # ? Draw all logic gates.
        self.drawANDSymbol()
        self.animateMoveTo(self.and_gate, [-6, 2, 0])

        self.drawORSymbol()
        self.animateMoveTo(self.or_gate, [-3, 2, 0])

        self.drawNOTSymbol()
        self.animateMoveTo(self.not_gate, [3, 2, 0])

        self.drawBufferSymbol()
        self.animateMoveTo(self.buffer_gate, [6, 2, 0])

        self.drawNANDSymbol()
        self.animateMoveTo(self.nand_gate, [-6, -2, 0])

        self.drawNORSymbol()
        self.animateMoveTo(self.nor_gate, [-3, -2, 0])

        self.drawXORSymbol()
        self.animateMoveTo(self.xor_gate, [3, -2, 0])

        self.drawXNORSymbol()
        self.animateMoveTo(self.xnor_gate, [6, -2, 0])

        # ? Clean all logic gates.
        self.wait(2)
        self.play(
            FadeOut(self.and_gate),
            FadeOut(self.or_gate),
            FadeOut(self.not_gate),
            FadeOut(self.buffer_gate),
            FadeOut(self.nand_gate),
            FadeOut(self.nor_gate),
            FadeOut(self.xor_gate),
            FadeOut(self.xnor_gate)
        )
        self.wait()


class ANDGate(Scene):
    
    def construct(self):
        # ? Draw symbol.
        up_hor = Line(start=[0, 1, 0], end=[-1, 1, 0])
        down_hor = Line(start=[0, -1, 0], end=[-1, -1, 0])
        ver = Line(start=[-1, 1, 0], end=[-1, -1, 0])
        arc = Arc(radius=1.0, start_angle=-PI/2, angle=PI)
        text = Tex(r"AND").shift(0.125 * LEFT)
        and_gate = Group(
            up_hor,
            down_hor,
            ver,
            arc,
            text
        )
        self.play(
            Create(up_hor),
            Create(down_hor),
            Create(ver),
            Create(arc),
            run_time=1
        )
        self.play(Write(text))
        self.add(and_gate)

        # ? Create inputs and output wires.
        wire_x_0 = Line(start=[-1, 0.7, 0], end=[-2, 0.7, 0])
        wire_x_1 = Line(start=[-1, -0.7, 0], end=[-2, -0.7, 0])
        wire_y = Line(start=[1, 0, 0], end=[2, 0, 0])

        self.play(
            Create(wire_x_0),
            Create(wire_x_1),
            Create(wire_y)
        )

        # ? Translate logic gate to the left.
        and_gate.add(wire_x_0, wire_x_1, wire_y)
        self.play(ApplyMethod(and_gate.shift, 3 * LEFT))

        # ? Label inputs and output.
        x_0 = {
            "0": Tex(r"0").next_to(wire_x_0.get_end(), direction=LEFT),
            "1": Tex(r"1", color=RED).next_to(wire_x_0.get_end(), direction=LEFT)
        }

        x_1 = {
            "0": Tex(r"0").next_to(wire_x_1.get_end(), direction=LEFT),
            "1": Tex(r"1", color=RED).next_to(wire_x_1.get_end(), direction=LEFT)
        }

        x_1_copy = {
            "0": x_1["0"].copy(),
            "1": x_1["1"].copy()
        }

        y = {
            "0": Tex(r"0").next_to(wire_y.get_end(), direction=RIGHT),
            "1": Tex(r"1", color=RED).next_to(wire_y.get_end(), direction=RIGHT)
        }

        text_x_0 = Tex(r"$x_0$", color=BLUE).next_to(x_0["0"], direction=LEFT)
        text_x_1 = Tex(r"$x_1$", color=BLUE).next_to(x_1["0"], direction=LEFT)
        text_y = Tex(r"$y$", color=BLUE).next_to(y["0"], direction=RIGHT)

        self.play(Write(text_x_0), Write(text_x_1), Write(text_y))
        self.play(Write(x_0["0"]), Write(x_1["0"]), Write(y["0"]))

        # ? Draw truth table.
        truth_table = Table(
            [
                ["0", "0", "0"],
                ["0", "1", "0"],
                ["1", "0", "0"],
                ["1", "1", "1"]
            ],
            col_labels=[
                Tex(r"$x_0$", color=BLUE),
                Tex(r"$x_1$", color=BLUE),
                Tex(r"$y$", color=BLUE)
            ],
            include_outer_lines=True,
            element_to_mobject=Tex,
        ).shift(4 * RIGHT)
        self.play(Create(truth_table), run_time=1)
        self.wait()

        # (x_0, x_1, y) = (0, 0, 0)
        self.play(Indicate(truth_table.get_rows()[1][:3]), run_time=1)
        self.wait()

        # (x_0, x_1, y) = (0, 1, 0)
        self.play(
            ApplyMethod(wire_x_1.set_color, RED),
            ReplacementTransform(x_1["0"], x_1["1"]),
            Indicate(truth_table.get_rows()[2][:3]),
            run_time=1,
        )
        self.wait()

        # (x_0, x_1, y) = (1, 0, 0)
        self.play(
            ApplyMethod(wire_x_0.set_color, RED),
            ApplyMethod(wire_x_1.set_color, WHITE),
            ReplacementTransform(x_0["0"], x_0["1"]),
            ReplacementTransform(x_1["1"], x_1_copy["0"]),
            Indicate(truth_table.get_rows()[3][:3]),
            run_time=1,
        )
        self.wait()

        # (x_0, x_1, y) = (1, 1, 1)
        self.play(
            ApplyMethod(wire_x_1.set_color, RED),
            ApplyMethod(wire_y.set_color, RED),
            ReplacementTransform(x_1_copy["0"], x_1_copy["1"]),
            ReplacementTransform(y["0"], y["1"]),
            Indicate(truth_table.get_rows()[4][:3]),
            run_time=1,
        )
        self.wait()

        self.play(
            Uncreate(truth_table),
            Uncreate(up_hor),
            Uncreate(down_hor),
            Uncreate(ver),
            Uncreate(arc),
            Uncreate(wire_x_0),
            Uncreate(wire_x_1),
            Uncreate(wire_y),
            Uncreate(text_x_0),
            Uncreate(text_x_1),
            Uncreate(text_y),
            Uncreate(x_0["1"]),
            Uncreate(x_1_copy["1"]),
            Uncreate(y["1"]),
            Uncreate(text),
        )
        self.wait()


class ORGate(Scene):

    def construct(self):
        # ? Draw symbol.
        up_arc = ArcBetweenPoints(start=[-1, -1, 0], end=[1, 0, 0], angle=PI/4)
        down_arc = ArcBetweenPoints(start=[-1, 1, 0], end=[1, 0, 0], angle=-PI/4)
        left_arc = ArcBetweenPoints(start=[-1, 1, 0], end=[-1, -1, 0], angle=-PI/3)
        text = Tex(r"OR")
        or_gate = Group(
            up_arc,
            down_arc,
            left_arc,
            text
        )
        self.play(
            Create(up_arc),
            Create(down_arc),
            Create(left_arc),
            run_time=1
        )
        self.play(Write(text))
        self.add(or_gate)

        # ? Create inputs and output wires.
        wire_x_0 = Line(start=[-0.88, 0.7, 0], end=[-2, 0.7, 0])
        wire_x_1 = Line(start=[-0.88, -0.7, 0], end=[-2, -0.7, 0])
        wire_y = Line(start=[1, 0, 0], end=[2, 0, 0])

        self.play(
            Create(wire_x_0),
            Create(wire_x_1),
            Create(wire_y)
        )

        # ? Translate logic gate to the left.
        or_gate.add(wire_x_0, wire_x_1, wire_y)
        self.play(ApplyMethod(or_gate.shift, 3 * LEFT))

        # ? Label inputs and output.
        x_0 = {
            "0": Tex(r"0").next_to(wire_x_0.get_end(), direction=LEFT),
            "1": Tex(r"1", color=RED).next_to(wire_x_0.get_end(), direction=LEFT)
        }

        x_1 = {
            "0": Tex(r"0").next_to(wire_x_1.get_end(), direction=LEFT),
            "1": Tex(r"1", color=RED).next_to(wire_x_1.get_end(), direction=LEFT)
        }

        x_1_copy = {
            "0": x_1["0"].copy(),
            "1": x_1["1"].copy()
        }

        y = {
            "0": Tex(r"0").next_to(wire_y.get_end(), direction=RIGHT),
            "1": Tex(r"1", color=RED).next_to(wire_y.get_end(), direction=RIGHT)
        }

        text_x_0 = Tex(r"$x_0$", color=BLUE).next_to(x_0["0"], direction=LEFT)
        text_x_1 = Tex(r"$x_1$", color=BLUE).next_to(x_1["0"], direction=LEFT)
        text_y = Tex(r"$y$", color=BLUE).next_to(y["0"], direction=RIGHT)

        self.play(Write(text_x_0), Write(text_x_1), Write(text_y))
        self.play(Write(x_0["0"]), Write(x_1["0"]), Write(y["0"]))

        # ? Draw truth table.
        truth_table = Table(
            [
                ["0", "0", "0"],
                ["0", "1", "1"],
                ["1", "0", "1"],
                ["1", "1", "1"]
            ],
            col_labels=[
                Tex(r"$x_0$", color=BLUE),
                Tex(r"$x_1$", color=BLUE),
                Tex(r"$y$", color=BLUE)
            ],
            include_outer_lines=True,
            element_to_mobject=Tex,
        ).shift(4 * RIGHT)
        self.play(Create(truth_table), run_time=1)
        self.wait()

        # (x_0, x_1, y) = (0, 0, 0)
        self.play(Indicate(truth_table.get_rows()[1][:3]), run_time=1)
        self.wait()

        # (x_0, x_1, y) = (0, 1, 1)
        self.play(
            ApplyMethod(wire_x_1.set_color, RED),
            ApplyMethod(wire_y.set_color, RED),
            ReplacementTransform(x_1["0"], x_1["1"]),
            ReplacementTransform(y["0"], y["1"]),
            Indicate(truth_table.get_rows()[2][:3]),
            run_time=1,
        )
        self.wait()

        # (x_0, x_1, y) = (1, 0, 1)
        self.play(
            ApplyMethod(wire_x_0.set_color, RED),
            ApplyMethod(wire_x_1.set_color, WHITE),
            ReplacementTransform(x_0["0"], x_0["1"]),
            ReplacementTransform(x_1["1"], x_1_copy["0"]),
            Indicate(truth_table.get_rows()[3][:3]),
            run_time=1,
        )
        self.wait()

        # (x_0, x_1, y) = (1, 1, 1)
        self.play(
            ApplyMethod(wire_x_1.set_color, RED),
            ReplacementTransform(x_1_copy["0"], x_1_copy["1"]),
            Indicate(truth_table.get_rows()[4][:3]),
            run_time=1,
        )
        self.wait()

        self.play(
            Uncreate(truth_table),
            Uncreate(up_arc),
            Uncreate(down_arc),
            Uncreate(left_arc),
            Uncreate(wire_x_0),
            Uncreate(wire_x_1),
            Uncreate(wire_y),
            Uncreate(text_x_0),
            Uncreate(text_x_1),
            Uncreate(text_y),
            Uncreate(x_0["1"]),
            Uncreate(x_1_copy["1"]),
            Uncreate(y["1"]),
            Uncreate(text),
        )
        self.wait()


class NOTGate(Scene):

    def construct(self):
        # ? Draw symbol.
        triangle = Polygon([1 - np.sqrt(3), 1, 0], [1 - np.sqrt(3), -1, 0], [1, 0, 0], color=WHITE)
        circle = Circle(radius=0.2, color=WHITE).move_to([1.25, 0, 0])
        text = Tex(r"NOT").scale(0.8)
        not_gate = Group(
            triangle,
            circle,
            text
        )
        self.play(
            Create(triangle),
            Create(circle),
            run_time=1
        )
        self.play(Write(text))
        self.add(not_gate)

        # ? Create inputs and output wires.
        wire_x = Line(start=[1 - np.sqrt(3), 0, 0], end=[-2, 0, 0])
        wire_y = Line(start=[1.47, 0, 0], end=[2.07, 0, 0], color=RED)

        self.play(
            Create(wire_x),
            Create(wire_y)
        )

        # ? Translate logic gate to the left.
        not_gate.add(wire_x, wire_y)
        self.play(ApplyMethod(not_gate.shift, 3 * LEFT))

        # ? Label inputs and output.
        x = {
            "0": Tex(r"0").next_to(wire_x.get_end(), direction=LEFT),
            "1": Tex(r"1", color=RED).next_to(wire_x.get_end(), direction=LEFT)
        }

        y = {
            "0": Tex(r"0").next_to(wire_y.get_end(), direction=RIGHT),
            "1": Tex(r"1", color=RED).next_to(wire_y.get_end(), direction=RIGHT)
        }

        text_x = Tex(r"$x$", color=BLUE).next_to(x["0"], direction=LEFT)
        text_y = Tex(r"$y$", color=BLUE).next_to(y["1"], direction=RIGHT)

        self.play(Write(text_x), Write(text_y))
        self.play(Write(x["0"]), Write(y["1"]))

        # ? Draw truth table.
        truth_table = Table(
            [
                ["0", "1"],
                ["1", "0"],
            ],
            col_labels=[
                Tex(r"$x$", color=BLUE),
                Tex(r"$y$", color=BLUE)
            ],
            include_outer_lines=True,
            element_to_mobject=Tex,
        ).shift(4 * RIGHT)
        self.play(Create(truth_table), run_time=1)
        self.wait()

        # (x, y) = (0, 1)
        self.play(Indicate(truth_table.get_rows()[1][:2]), run_time=1)
        self.wait()

        # (x, y) = (1, 0)
        self.play(
            ApplyMethod(wire_x.set_color, RED),
            ApplyMethod(wire_y.set_color, WHITE),
            ReplacementTransform(x["0"], x["1"]),
            ReplacementTransform(y["1"], y["0"]),
            Indicate(truth_table.get_rows()[2][:2]),
            run_time=1,
        )
        self.wait()

        self.play(
            Uncreate(truth_table),
            Uncreate(triangle),
            Uncreate(circle),
            Uncreate(wire_x),
            Uncreate(wire_y),
            Uncreate(text_x),
            Uncreate(text_y),
            Uncreate(x["1"]),
            Uncreate(y["0"]),
            Uncreate(text),
        )
        self.wait()


class BufferGate(Scene):

    def construct(self):
        # ? Draw symbol.
        triangle = Polygon([1 - np.sqrt(3), 1, 0], [1 - np.sqrt(3), -1, 0], [1, 0, 0], color=WHITE)
        text = Tex(r"BUFFER").scale(0.5)
        buffer_gate = Group(
            triangle,
            text
        )
        self.play(
            Create(triangle),
            run_time=1
        )
        self.play(Write(text))
        self.add(buffer_gate)

        # ? Create inputs and output wires.
        wire_x = Line(start=[1 - np.sqrt(3), 0, 0], end=[-2, 0, 0])
        wire_y = Line(start=[1, 0, 0], end=[2, 0, 0])

        self.play(
            Create(wire_x),
            Create(wire_y)
        )

        # ? Translate logic gate to the left.
        buffer_gate.add(wire_x, wire_y)
        self.play(ApplyMethod(buffer_gate.shift, 3 * LEFT))

        # ? Label inputs and output.
        x = {
            "0": Tex(r"0").next_to(wire_x.get_end(), direction=LEFT),
            "1": Tex(r"1", color=RED).next_to(wire_x.get_end(), direction=LEFT)
        }

        y = {
            "0": Tex(r"0").next_to(wire_y.get_end(), direction=RIGHT),
            "1": Tex(r"1", color=RED).next_to(wire_y.get_end(), direction=RIGHT)
        }

        text_x = Tex(r"$x$", color=BLUE).next_to(x["0"], direction=LEFT)
        text_y = Tex(r"$y$", color=BLUE).next_to(y["1"], direction=RIGHT)

        self.play(Write(text_x), Write(text_y))
        self.play(Write(x["0"]), Write(y["0"]))

        # ? Draw truth table.
        truth_table = Table(
            [
                ["0", "0"],
                ["1", "1"],
            ],
            col_labels=[
                Tex(r"$x$", color=BLUE),
                Tex(r"$y$", color=BLUE)
            ],
            include_outer_lines=True,
            element_to_mobject=Tex,
        ).shift(4 * RIGHT)
        self.play(Create(truth_table), run_time=1)
        self.wait()

        # (x, y) = (0, 0)
        self.play(Indicate(truth_table.get_rows()[1][:2]), run_time=1)
        self.wait()

        # (x, y) = (1, 1)
        self.play(
            ApplyMethod(wire_x.set_color, RED),
            ApplyMethod(wire_y.set_color, RED),
            ReplacementTransform(x["0"], x["1"]),
            ReplacementTransform(y["0"], y["1"]),
            Indicate(truth_table.get_rows()[2][:2]),
            run_time=1,
        )
        self.wait()

        self.play(
            Uncreate(truth_table),
            Uncreate(triangle),
            Uncreate(wire_x),
            Uncreate(wire_y),
            Uncreate(text_x),
            Uncreate(text_y),
            Uncreate(x["1"]),
            Uncreate(y["1"]),
            Uncreate(text),
        )
        self.wait()


class NANDGate(Scene):

    def construct(self):
        # ? Draw symbol.
        and_up_hor = Line(start=[0, 1, 0], end=[-1, 1, 0]).shift(2 * LEFT)
        and_down_hor = Line(start=[0, -1, 0], end=[-1, -1, 0]).shift(2 * LEFT)
        and_ver = Line(start=[-1, 1, 0], end=[-1, -1, 0]).shift(2 * LEFT)
        and_arc = Arc(radius=1.0, start_angle=-PI/2, angle=PI).shift(2 * LEFT)
        and_text = Tex(r"AND").shift(0.125 * LEFT).shift(2 * LEFT)

        not_triangle = Polygon([1 - np.sqrt(3), 1, 0], [1 - np.sqrt(3), -1, 0], [1, 0, 0], color=WHITE).shift(2 * RIGHT)
        not_circle = Circle(radius=0.2, color=WHITE).move_to([1.25, 0, 0]).shift(2 * RIGHT)
        not_text = Tex(r"NOT").scale(0.8).shift(2 * RIGHT)
        plus_sign = Tex(r"+")

        nand_text = Tex(r"NAND")
        nand_gate = Group(
            and_up_hor,
            and_down_hor,
            and_ver,
            and_arc,
            not_circle,
            nand_text
        )

        self.play(
            Create(and_up_hor),
            Create(and_down_hor),
            Create(and_ver),
            Create(and_arc),
            Create(not_triangle),
            Create(not_circle),
            FadeIn(plus_sign),
            run_time=1
        )
        self.play(
            Write(and_text), 
            Write(not_text)
        )
        self.play(
            Unwrite(and_text), 
            Unwrite(not_text)
        )        
        self.play(
            Uncreate(not_triangle, run_time=0.2),
            ApplyMethod(and_up_hor.shift, 2 * RIGHT),
            ApplyMethod(and_down_hor.shift, 2 * RIGHT),
            ApplyMethod(and_ver.shift, 2 * RIGHT),
            ApplyMethod(and_arc.shift, 2 * RIGHT),
            ApplyMethod(not_circle.shift, 2.05 * LEFT),
            FadeOut(plus_sign, run_time=0.2),
        )
        self.play(FadeIn(nand_text))
        self.wait()

        # ? Create inputs and output wires.
        wire_x_0 = Line(start=[-1, 0.7, 0], end=[-2, 0.7, 0])
        wire_x_1 = Line(start=[-1, -0.7, 0], end=[-2, -0.7, 0])
        wire_y = Line(start=[1.4, 0, 0], end=[2, 0, 0], color=RED)

        self.play(
            Create(wire_x_0),
            Create(wire_x_1),
            Create(wire_y)
        )

        # ? Translate logic gate to the left.
        nand_gate.add(wire_x_0, wire_x_1, wire_y)
        self.play(ApplyMethod(nand_gate.shift, 3 * LEFT))

        # ? Label inputs and output.
        x_0 = {
            "0": Tex(r"0").next_to(wire_x_0.get_end(), direction=LEFT),
            "1": Tex(r"1", color=RED).next_to(wire_x_0.get_end(), direction=LEFT)
        }

        x_1 = {
            "0": Tex(r"0").next_to(wire_x_1.get_end(), direction=LEFT),
            "1": Tex(r"1", color=RED).next_to(wire_x_1.get_end(), direction=LEFT)
        }

        x_1_copy = {
            "0": x_1["0"].copy(),
            "1": x_1["1"].copy()
        }

        y = {
            "0": Tex(r"0").next_to(wire_y.get_end(), direction=RIGHT),
            "1": Tex(r"1", color=RED).next_to(wire_y.get_end(), direction=RIGHT)
        }

        text_x_0 = Tex(r"$x_0$", color=BLUE).next_to(x_0["0"], direction=LEFT)
        text_x_1 = Tex(r"$x_1$", color=BLUE).next_to(x_1["0"], direction=LEFT)
        text_y = Tex(r"$y$", color=BLUE).next_to(y["0"], direction=RIGHT)

        self.play(Write(text_x_0), Write(text_x_1), Write(text_y))
        self.play(Write(x_0["0"]), Write(x_1["0"]), Write(y["1"]))

        # ? Draw truth table.
        truth_table = Table(
            [
                ["0", "0", "1"],
                ["0", "1", "1"],
                ["1", "0", "1"],
                ["1", "1", "0"]
            ],
            col_labels=[
                Tex(r"$x_0$", color=BLUE),
                Tex(r"$x_1$", color=BLUE),
                Tex(r"$y$", color=BLUE)
            ],
            include_outer_lines=True,
            element_to_mobject=Tex,
        ).shift(4 * RIGHT)
        self.play(Create(truth_table), run_time=1)
        self.wait()

        # (x_0, x_1, y) = (0, 0, 1)
        self.play(Indicate(truth_table.get_rows()[1][:3]), run_time=1)
        self.wait()

        # (x_0, x_1, y) = (0, 1, 1)
        self.play(
            ApplyMethod(wire_x_1.set_color, RED),
            ReplacementTransform(x_1["0"], x_1["1"]),
            Indicate(truth_table.get_rows()[2][:3]),
            run_time=1,
        )
        self.wait()

        # (x_0, x_1, y) = (1, 0, 1)
        self.play(
            ApplyMethod(wire_x_0.set_color, RED),
            ApplyMethod(wire_x_1.set_color, WHITE),
            ReplacementTransform(x_0["0"], x_0["1"]),
            ReplacementTransform(x_1["1"], x_1_copy["0"]),
            Indicate(truth_table.get_rows()[3][:3]),
            run_time=1,
        )
        self.wait()

        # (x_0, x_1, y) = (1, 1, 0)
        self.play(
            ApplyMethod(wire_x_1.set_color, RED),
            ApplyMethod(wire_y.set_color, WHITE),
            ReplacementTransform(x_1_copy["0"], x_1_copy["1"]),
            ReplacementTransform(y["1"], y["0"]),
            Indicate(truth_table.get_rows()[4][:3]),
            run_time=1,
        )
        self.wait()

        self.play(
            Uncreate(truth_table),
            Uncreate(and_up_hor),
            Uncreate(and_down_hor),
            Uncreate(and_ver),
            Uncreate(and_arc),
            Uncreate(wire_x_0),
            Uncreate(wire_x_1),
            Uncreate(wire_y),
            Uncreate(text_x_0),
            Uncreate(text_x_1),
            Uncreate(text_y),
            Uncreate(x_0["1"]),
            Uncreate(x_1_copy["1"]),
            Uncreate(y["0"]),
            Uncreate(not_circle),
            Uncreate(nand_text),
        )
        self.wait()


class NORGate(Scene):

    def construct(self):
        # ? Draw symbol.
        or_up_arc = ArcBetweenPoints(start=[-1, -1, 0], end=[1, 0, 0], angle=PI/4).shift(2 * LEFT)
        or_down_arc = ArcBetweenPoints(start=[-1, 1, 0], end=[1, 0, 0], angle=-PI/4).shift(2 * LEFT)
        or_left_arc = ArcBetweenPoints(start=[-1, 1, 0], end=[-1, -1, 0], angle=-PI/3).shift(2 * LEFT)
        or_text = Tex(r"OR").shift(2 * LEFT)

        not_triangle = Polygon([1 - np.sqrt(3), 1, 0], [1 - np.sqrt(3), -1, 0], [1, 0, 0], color=WHITE).shift(2 * RIGHT)
        not_circle = Circle(radius=0.2, color=WHITE).move_to([1.25, 0, 0]).shift(2 * RIGHT)
        not_text = Tex(r"NOT").scale(0.8).shift(2 * RIGHT)
        plus_sign = Tex(r"+")

        nor_text = Tex(r"NOR")
        nor_gate = Group(
            or_up_arc,
            or_down_arc,
            or_left_arc,
            not_circle,
            nor_text
        )

        self.play(
            Create(or_up_arc),
            Create(or_down_arc),
            Create(or_left_arc),
            Create(not_triangle),
            Create(not_circle),
            FadeIn(plus_sign),
            run_time=1
        )
        self.play(
            Write(or_text),
            Write(not_text)
        )
        self.play(
            Unwrite(or_text),
            Unwrite(not_text)
        )        
        self.play(
            Uncreate(not_triangle, run_time=0.2),
            ApplyMethod(or_up_arc.shift, 2 * RIGHT),
            ApplyMethod(or_down_arc.shift, 2 * RIGHT),
            ApplyMethod(or_left_arc.shift, 2 * RIGHT),
            ApplyMethod(not_circle.shift, 2.05 * LEFT),
            FadeOut(plus_sign, run_time=0.2),
        )
        self.play(FadeIn(nor_text))
        self.wait()

        # ? Create inputs and output wires.
        wire_x_0 = Line(start=[-0.88, 0.7, 0], end=[-2, 0.7, 0])
        wire_x_1 = Line(start=[-0.88, -0.7, 0], end=[-2, -0.7, 0])
        wire_y = Line(start=[1.4, 0, 0], end=[2, 0, 0], color=RED)

        self.play(
            Create(wire_x_0),
            Create(wire_x_1),
            Create(wire_y)
        )

        # ? Translate logic gate to the left.
        nor_gate.add(wire_x_0, wire_x_1, wire_y)
        self.play(ApplyMethod(nor_gate.shift, 3 * LEFT))

        # ? Label inputs and output.
        x_0 = {
            "0": Tex(r"0").next_to(wire_x_0.get_end(), direction=LEFT),
            "1": Tex(r"1", color=RED).next_to(wire_x_0.get_end(), direction=LEFT)
        }

        x_1 = {
            "0": Tex(r"0").next_to(wire_x_1.get_end(), direction=LEFT),
            "1": Tex(r"1", color=RED).next_to(wire_x_1.get_end(), direction=LEFT)
        }

        x_1_copy = {
            "0": x_1["0"].copy(),
            "1": x_1["1"].copy()
        }

        y = {
            "0": Tex(r"0").next_to(wire_y.get_end(), direction=RIGHT),
            "1": Tex(r"1", color=RED).next_to(wire_y.get_end(), direction=RIGHT)
        }

        text_x_0 = Tex(r"$x_0$", color=BLUE).next_to(x_0["0"], direction=LEFT)
        text_x_1 = Tex(r"$x_1$", color=BLUE).next_to(x_1["0"], direction=LEFT)
        text_y = Tex(r"$y$", color=BLUE).next_to(y["0"], direction=RIGHT)

        self.play(Write(text_x_0), Write(text_x_1), Write(text_y))
        self.play(Write(x_0["0"]), Write(x_1["0"]), Write(y["1"]))

        # ? Draw truth table.
        truth_table = Table(
            [
                ["0", "0", "1"],
                ["0", "1", "0"],
                ["1", "0", "0"],
                ["1", "1", "0"]
            ],
            col_labels=[
                Tex(r"$x_0$", color=BLUE),
                Tex(r"$x_1$", color=BLUE),
                Tex(r"$y$", color=BLUE)
            ],
            include_outer_lines=True,
            element_to_mobject=Tex,
        ).shift(4 * RIGHT)
        self.play(Create(truth_table), run_time=1)
        self.wait()

        # (x_0, x_1, y) = (0, 0, 1)
        self.play(Indicate(truth_table.get_rows()[1][:3]), run_time=1)
        self.wait()

        # (x_0, x_1, y) = (0, 1, 0)
        self.play(
            ApplyMethod(wire_x_1.set_color, RED),
            ApplyMethod(wire_y.set_color, WHITE),
            ReplacementTransform(x_1["0"], x_1["1"]),
            ReplacementTransform(y["1"], y["0"]),
            Indicate(truth_table.get_rows()[2][:3]),
            run_time=1,
        )
        self.wait()

        # (x_0, x_1, y) = (1, 0, 0)
        self.play(
            ApplyMethod(wire_x_0.set_color, RED),
            ApplyMethod(wire_x_1.set_color, WHITE),
            ReplacementTransform(x_0["0"], x_0["1"]),
            ReplacementTransform(x_1["1"], x_1_copy["0"]),
            Indicate(truth_table.get_rows()[3][:3]),
            run_time=1,
        )
        self.wait()

        # (x_0, x_1, y) = (1, 1, 0)
        self.play(
            ApplyMethod(wire_x_1.set_color, RED),
            ReplacementTransform(x_1_copy["0"], x_1_copy["1"]),
            Indicate(truth_table.get_rows()[4][:3]),
            run_time=1,
        )
        self.wait()

        self.play(
            Uncreate(truth_table),
            Uncreate(or_up_arc),
            Uncreate(or_down_arc),
            Uncreate(or_left_arc),
            Uncreate(wire_x_0),
            Uncreate(wire_x_1),
            Uncreate(wire_y),
            Uncreate(text_x_0),
            Uncreate(text_x_1),
            Uncreate(text_y),
            Uncreate(x_0["1"]),
            Uncreate(x_1_copy["1"]),
            Uncreate(not_circle),
            Uncreate(nor_text),
            Uncreate(y["0"]),
        )
        self.wait()


class XORGate(Scene):

    def construct(self):
        # ? Draw symbol.
        up_arc = ArcBetweenPoints(start=[-1, -1, 0], end=[1, 0, 0], angle=PI/4)
        down_arc = ArcBetweenPoints(start=[-1, 1, 0], end=[1, 0, 0], angle=-PI/4)
        left_arc = ArcBetweenPoints(start=[-1, 1, 0], end=[-1, -1, 0], angle=-PI/3)
        second_left_arc = ArcBetweenPoints(start=[-1, 1, 0], end=[-1, -1, 0], angle=-PI/3).shift(0.2 * LEFT)
        text = Tex(r"XOR")
        xor_gate = Group(
            up_arc,
            down_arc,
            left_arc,
            second_left_arc,
            text
        )
        self.play(
            Create(up_arc),
            Create(down_arc),
            Create(left_arc),
            Create(second_left_arc),
            run_time=1
        )
        self.play(Write(text))
        self.add(xor_gate)

        # ? Create inputs and output wires.
        wire_x_0 = Line(start=[-1.08, 0.7, 0], end=[-2, 0.7, 0])
        wire_x_1 = Line(start=[-1.08, -0.7, 0], end=[-2, -0.7, 0])
        wire_y = Line(start=[1, 0, 0], end=[2, 0, 0])

        self.play(
            Create(wire_x_0),
            Create(wire_x_1),
            Create(wire_y)
        )

        # ? Translate logic gate to the left.
        xor_gate.add(wire_x_0, wire_x_1, wire_y)
        self.play(ApplyMethod(xor_gate.shift, 3 * LEFT))

        # ? Label inputs and output.
        x_0 = {
            "0": Tex(r"0").next_to(wire_x_0.get_end(), direction=LEFT),
            "1": Tex(r"1", color=RED).next_to(wire_x_0.get_end(), direction=LEFT)
        }

        x_1 = {
            "0": Tex(r"0").next_to(wire_x_1.get_end(), direction=LEFT),
            "1": Tex(r"1", color=RED).next_to(wire_x_1.get_end(), direction=LEFT)
        }

        x_1_copy = {
            "0": x_1["0"].copy(),
            "1": x_1["1"].copy()
        }

        y = {
            "0": Tex(r"0").next_to(wire_y.get_end(), direction=RIGHT),
            "1": Tex(r"1", color=RED).next_to(wire_y.get_end(), direction=RIGHT)
        }

        y_copy = {
            "0": y["0"].copy(),
            "1": y["1"].copy()
        }

        text_x_0 = Tex(r"$x_0$", color=BLUE).next_to(x_0["0"], direction=LEFT)
        text_x_1 = Tex(r"$x_1$", color=BLUE).next_to(x_1["0"], direction=LEFT)
        text_y = Tex(r"$y$", color=BLUE).next_to(y["0"], direction=RIGHT)

        self.play(Write(text_x_0), Write(text_x_1), Write(text_y))
        self.play(Write(x_0["0"]), Write(x_1["0"]), Write(y["0"]))

        # ? Draw truth table.
        truth_table = Table(
            [
                ["0", "0", "0"],
                ["0", "1", "1"],
                ["1", "0", "1"],
                ["1", "1", "0"]
            ],
            col_labels=[
                Tex(r"$x_0$", color=BLUE),
                Tex(r"$x_1$", color=BLUE),
                Tex(r"$y$", color=BLUE)
            ],
            include_outer_lines=True,
            element_to_mobject=Tex,
        ).shift(4 * RIGHT)
        self.play(Create(truth_table), run_time=1)
        self.wait()

        # (x_0, x_1, y) = (0, 0, 0)
        self.play(Indicate(truth_table.get_rows()[1][:3]), run_time=1)
        self.wait()

        # (x_0, x_1, y) = (0, 1, 1)
        self.play(
            ApplyMethod(wire_x_1.set_color, RED),
            ApplyMethod(wire_y.set_color, RED),
            ReplacementTransform(x_1["0"], x_1["1"]),
            ReplacementTransform(y["0"], y["1"]),
            Indicate(truth_table.get_rows()[2][:3]),
            run_time=1,
        )
        self.wait()

        # (x_0, x_1, y) = (1, 0, 1)
        self.play(
            ApplyMethod(wire_x_0.set_color, RED),
            ApplyMethod(wire_x_1.set_color, WHITE),
            ReplacementTransform(x_0["0"], x_0["1"]),
            ReplacementTransform(x_1["1"], x_1_copy["0"]),
            Indicate(truth_table.get_rows()[3][:3]),
            run_time=1,
        )
        self.wait()

        # (x_0, x_1, y) = (1, 1, 0)
        self.play(
            ApplyMethod(wire_x_1.set_color, RED),
            ApplyMethod(wire_y.set_color, WHITE),
            ReplacementTransform(x_1_copy["0"], x_1_copy["1"]),
            ReplacementTransform(y["1"], y_copy["0"]),
            Indicate(truth_table.get_rows()[4][:3]),
            run_time=1,
        )
        self.wait()

        self.play(
            Uncreate(truth_table),
            Uncreate(up_arc),
            Uncreate(down_arc),
            Uncreate(second_left_arc),
            Uncreate(left_arc),
            Uncreate(wire_x_0),
            Uncreate(wire_x_1),
            Uncreate(wire_y),
            Uncreate(text_x_0),
            Uncreate(text_x_1),
            Uncreate(text_y),
            Uncreate(x_0["1"]),
            Uncreate(x_1_copy["1"]),
            Uncreate(text),
            Uncreate(y_copy["0"]),
        )
        self.wait()


class XNORGate(Scene):
    
    def construct(self):
        # ? Draw symbol.
        xor_up_arc = ArcBetweenPoints(start=[-1, -1, 0], end=[1, 0, 0], angle=PI/4).shift(2 * LEFT)
        xor_down_arc = ArcBetweenPoints(start=[-1, 1, 0], end=[1, 0, 0], angle=-PI/4).shift(2 * LEFT)
        xor_left_arc = ArcBetweenPoints(start=[-1, 1, 0], end=[-1, -1, 0], angle=-PI/3).shift(2 * LEFT)
        xor_second_left_arc = ArcBetweenPoints(start=[-1, 1, 0], end=[-1, -1, 0], angle=-PI/3).shift(2.2 * LEFT)
        xor_text = Tex(r"XOR").shift(2 * LEFT)

        not_triangle = Polygon([1 - np.sqrt(3), 1, 0], [1 - np.sqrt(3), -1, 0], [1, 0, 0], color=WHITE).shift(2 * RIGHT)
        not_circle = Circle(radius=0.2, color=WHITE).move_to([1.25, 0, 0]).shift(2 * RIGHT)
        not_text = Tex(r"NOT").scale(0.8).shift(2 * RIGHT)
        plus_sign = Tex(r"+")

        xnor_text = Tex(r"XNOR").scale(0.8)
        xnor_gate = Group(
            xor_up_arc,
            xor_down_arc,
            xor_left_arc,
            xor_second_left_arc,
            not_circle,
            xnor_text
        )

        self.play(
            Create(xor_up_arc),
            Create(xor_down_arc),
            Create(xor_left_arc),
            Create(xor_second_left_arc),
            Create(not_triangle),
            Create(not_circle),
            FadeIn(plus_sign),
            run_time=1
        )
        self.play(
            Write(xor_text),
            Write(not_text)
        )
        self.play(
            Unwrite(xor_text),
            Unwrite(not_text)
        )        
        self.play(
            Uncreate(not_triangle, run_time=0.2),
            ApplyMethod(xor_up_arc.shift, 2 * RIGHT),
            ApplyMethod(xor_down_arc.shift, 2 * RIGHT),
            ApplyMethod(xor_left_arc.shift, 2 * RIGHT),
            ApplyMethod(xor_second_left_arc.shift, 2 * RIGHT),
            ApplyMethod(not_circle.shift, 2.05 * LEFT),
            FadeOut(plus_sign, run_time=0.2),
        )
        self.play(FadeIn(xnor_text))
        self.wait()

        # ? Create inputs and output wires.
        wire_x_0 = Line(start=[-1.08, 0.7, 0], end=[-2, 0.7, 0])
        wire_x_1 = Line(start=[-1.08, -0.7, 0], end=[-2, -0.7, 0])
        wire_y = Line(start=[1.4, 0, 0], end=[2, 0, 0], color=RED)

        self.play(
            Create(wire_x_0),
            Create(wire_x_1),
            Create(wire_y)
        )

        # ? Translate logic gate to the left.
        xnor_gate.add(wire_x_0, wire_x_1, wire_y)
        self.play(ApplyMethod(xnor_gate.shift, 3 * LEFT))

        # ? Label inputs and output.
        x_0 = {
            "0": Tex(r"0").next_to(wire_x_0.get_end(), direction=LEFT),
            "1": Tex(r"1", color=RED).next_to(wire_x_0.get_end(), direction=LEFT)
        }

        x_1 = {
            "0": Tex(r"0").next_to(wire_x_1.get_end(), direction=LEFT),
            "1": Tex(r"1", color=RED).next_to(wire_x_1.get_end(), direction=LEFT)
        }

        x_1_copy = {
            "0": x_1["0"].copy(),
            "1": x_1["1"].copy()
        }

        y = {
            "0": Tex(r"0").next_to(wire_y.get_end(), direction=RIGHT),
            "1": Tex(r"1", color=RED).next_to(wire_y.get_end(), direction=RIGHT)
        }

        y_copy = {
            "0": y["0"].copy(),
            "1": y["1"].copy()
        }

        text_x_0 = Tex(r"$x_0$", color=BLUE).next_to(x_0["0"], direction=LEFT)
        text_x_1 = Tex(r"$x_1$", color=BLUE).next_to(x_1["0"], direction=LEFT)
        text_y = Tex(r"$y$", color=BLUE).next_to(y["0"], direction=RIGHT)

        self.play(Write(text_x_0), Write(text_x_1), Write(text_y))
        self.play(Write(x_0["0"]), Write(x_1["0"]), Write(y["1"]))

        # ? Draw truth table.
        truth_table = Table(
            [
                ["0", "0", "1"],
                ["0", "1", "0"],
                ["1", "0", "0"],
                ["1", "1", "1"]
            ],
            col_labels=[
                Tex(r"$x_0$", color=BLUE),
                Tex(r"$x_1$", color=BLUE),
                Tex(r"$y$", color=BLUE)
            ],
            include_outer_lines=True,
            element_to_mobject=Tex,
        ).shift(4 * RIGHT)
        self.play(Create(truth_table), run_time=1)
        self.wait()

        # (x_0, x_1, y) = (0, 0, 1)
        self.play(Indicate(truth_table.get_rows()[1][:3]), run_time=1)
        self.wait()

        # (x_0, x_1, y) = (0, 1, 0)
        self.play(
            ApplyMethod(wire_x_1.set_color, RED),
            ApplyMethod(wire_y.set_color, WHITE),
            ReplacementTransform(x_1["0"], x_1["1"]),
            ReplacementTransform(y["1"], y["0"]),
            Indicate(truth_table.get_rows()[2][:3]),
            run_time=1,
        )
        self.wait()

        # (x_0, x_1, y) = (1, 0, 0)
        self.play(
            ApplyMethod(wire_x_0.set_color, RED),
            ApplyMethod(wire_x_1.set_color, WHITE),
            ReplacementTransform(x_0["0"], x_0["1"]),
            ReplacementTransform(x_1["1"], x_1_copy["0"]),
            Indicate(truth_table.get_rows()[3][:3]),
            run_time=1,
        )
        self.wait()

        # (x_0, x_1, y) = (1, 1, 1)
        self.play(
            ApplyMethod(wire_x_1.set_color, RED),
            ApplyMethod(wire_y.set_color, RED),
            ReplacementTransform(x_1_copy["0"], x_1_copy["1"]),
            ReplacementTransform(y["0"], y_copy["1"]),
            Indicate(truth_table.get_rows()[4][:3]),
            run_time=1,
        )
        self.wait()

        self.play(
            Uncreate(truth_table),
            Uncreate(xor_up_arc),
            Uncreate(xor_down_arc),
            Uncreate(xor_left_arc),
            Uncreate(xor_second_left_arc),
            Uncreate(wire_x_0),
            Uncreate(wire_x_1),
            Uncreate(wire_y),
            Uncreate(text_x_0),
            Uncreate(text_x_1),
            Uncreate(text_y),
            Uncreate(x_0["1"]),
            Uncreate(x_1_copy["1"]),
            Uncreate(xnor_text),
            Uncreate(y_copy["1"]),
            Uncreate(not_circle),
        )
        self.wait()


class End(Scene):

    def construct(self):
        text = Tex(r"Thank you for watching!", font_size=96)
        self.play(Write(text))
        self.wait()
        self.play(Unwrite(text))
        self.wait()
