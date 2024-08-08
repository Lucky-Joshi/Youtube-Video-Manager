import os,time

def play_video():
    with open('video_list.txt', 'r') as file:
        videos = file.readlines()
        
    print("Select a video to play:")
    for i, video in enumerate(videos, start=1):
        print(f"{i}. {video.strip()}")
    
    choice = int(input("Enter your choice: ")) - 1
    time.sleep(1)

    if str(choice)=="":
        print("Please enter your choice")
    else:
        video_to_play = videos[choice].strip()
        time.sleep(1)

        if os.path.isfile(video_to_play):
            os.system(f"start {video_to_play}")  # Use 'start' for Windows, 'open' for macOS, 'xdg-open' for Linux
        else:
            print("File not found.")
