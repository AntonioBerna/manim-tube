# manim-tube

## Usage

The `-ql` specifies low render quality (854x480 15FPS).
This does not look very good, but is very useful for rapid prototyping and testing. 

The other options that specify render quality are `-qm`, `-qh`, `-qp` and `-qk` for medium (1280x720 30FPS), high (1920x1080 60FPS), 2k (2560x1440 60FPS) and 4k quality (3840x2160 60FPS), respectively.

The `-p` flag plays the animation once it is rendered.

### Examples

Tipically commands are like this:

```
manim -pqh main.py
```

If you want to render a specific scene, you can specify it

```
manim -pqh main.py SceneName
```

If you want to render multiple scenes, you can specify them separated

```
manim -pqh main.py SceneName1 SceneName2
```
