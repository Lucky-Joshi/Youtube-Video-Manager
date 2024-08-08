import os,time
from play_video import play_video
from rearrange_video import rearrange_videos
from add_video import add_video
from delete_video import delete_video

def display_menu():
    print("\t\tYoutube Video Manager")
    time.sleep(1)
    print("\t\t1. Play Video")
    time.sleep(1)
    print("\t\t2. Rearrange Videos")
    time.sleep(1)
    print("\t\t3. Add Video")
    time.sleep(1)
    print("\t\t4. Delete Video")
    time.sleep(1)
    print("\t\t5. Exit")
    time.sleep(1)

def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        os.system("CLS")
        
        if choice == '1':
            play_video()
        elif choice == '2':
            rearrange_videos()
        elif choice == '3':
            add_video()
        elif choice == '4':
            delete_video()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
