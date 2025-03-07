import os

VIDEO_DIR = "media/videos"
PROJECT_NAME = "main/1080p60"
FILE_LIST = "videos.txt"

if __name__ == "__main__":
    project_video_dir = os.path.join(VIDEO_DIR, PROJECT_NAME)
    video_files = sorted(f for f in os.listdir(project_video_dir) if f.endswith(".mp4"))

    with open(FILE_LIST, "w") as f:
        for video in video_files:
            f.write(f"file \"{os.path.join(project_video_dir, video)}\"\n")

    print(f"The \"{FILE_LIST}\" file has been successfully generated.")
    print("Now, you can concatenate all videos with the following command:")
    print(f"ffmpeg -f concat -safe 0 -i {FILE_LIST} -c copy logic-gates.mp4")
