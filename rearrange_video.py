import time
def rearrange_videos():
    with open('video_list.txt', 'r') as file:
        videos = file.readlines()
    
    print("Current order of videos:")
    time.sleep(1)
    for i, video in enumerate(videos, start=1):
        print(f"{i}. {video.strip()}")
    
    from_index = int(input("Enter the index of the video to move: ")) - 1
    time.sleep(1)
    if str(from_index)=="":
        print("Please enter your choice")
    else:
        to_index = int(input("Enter the new index for the video: ")) - 1
        
        if 0 <= from_index < len(videos) and 0 <= to_index < len(videos):
            video = videos.pop(from_index)
            videos.insert(to_index, video)
            
            with open('video_list.txt', 'w') as file:
                file.writelines(videos)
            print("Rearranement successfull")
        else:
            print("Invalid choice.")
