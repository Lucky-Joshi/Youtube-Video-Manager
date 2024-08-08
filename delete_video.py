import os,time

def delete_video():
    with open('video_list.txt', 'r') as file:
        videos = file.readlines()
    
    print("Select a video to delete:")
    time.sleep
    for i, video in enumerate(videos, start=1):
        print(f"{i}. {video.strip()}")
    
    choice = int(input("Enter your choice: ")) - 1
    time,sleep(5)
    if str(choice)=="":
        print("Please enter your choice")
    else:
        video_to_delete = videos.pop(choice).strip()
        
        if os.path.isfile(video_to_delete):
            os.remove(video_to_delete)
            print(f"Deleted {video_to_delete} successfully.")
        else:
            print("File not found.")
        
        with open('video_list.txt', 'w') as file:
            file.writelines(videos)
