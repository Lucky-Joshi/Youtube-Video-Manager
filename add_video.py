import time

def add_video():
    while True:
        video_name = input("Enter the name of the video t(including .mp4 extension): ")
        if video_name=="":
            print("All entries done!")
            time.sleep(5)
            break
        else:
            with open('video_list.txt', 'a') as file:
                file.write(video_name + '\n')
                print("Video entry done!")
                time.sleep(5)

