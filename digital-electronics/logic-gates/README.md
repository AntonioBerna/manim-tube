# Logic Gates

## Render

You can use the following command:

```
manim -pqh main.py
```

and then select the scene you want to render from the list of scenes that will be displayed in the terminal:

```
1: ANDGate
2: BufferGate
3: End
4: LogicGates
5: NANDGate
6: NORGate
7: NOTGate
8: ORGate
9: Welcome
10: XNORGate
11: XORGate
 
Choose number corresponding to desired scene/arguments.
(Use comma separated list for multiple entries)
Choice(s):
```

After rendering all the scenes, they can be joined together.
In particular, you can use the `python path.py` command to generate a file with content similar to the following:

```
file 'media/videos/main/1080p60/Welcome.mp4'
file 'media/videos/main/1080p60/LogicGates.mp4'
file 'media/videos/main/1080p60/ANDGate.mp4'
file 'media/videos/main/1080p60/ORGate.mp4'
file 'media/videos/main/1080p60/NOTGate.mp4'
file 'media/videos/main/1080p60/BufferGate.mp4'
file 'media/videos/main/1080p60/NANDGate.mp4'
file 'media/videos/main/1080p60/NORGate.mp4'
file 'media/videos/main/1080p60/XORGate.mp4'
file 'media/videos/main/1080p60/XNORGate.mp4'
file 'media/videos/main/1080p60/End.mp4'
```

> [!WARNING]
> File order is important. The first file will be displayed first, the second file will be displayed second, and so on.

This file, which by default is called `videos.txt`, must be used in combination with `ffmpeg` to concatenate all the scenes into one video.
The command to use is the following:

```
ffmpeg -f concat -safe 0 -i videos.txt -c copy logic-gates.mp4
```
