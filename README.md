# Youtube-Video-Manager
Overview
The Video Manager App is a Python-based application for managing MP4 video files. It allows users to:

Play videos from a list
Rearrange the order of videos
Add new videos
Delete existing videos
The app uses a text file to keep track of the videos and provides a simple menu-driven interface for managing them.


Project Structure
The project directory is organized as follows:
video_manager/
│
├── main.py              # Main entry point of the application
├── play_video.py        # Module to play a selected video
├── rearrange_video.py   # Module to rearrange video order
├── add_video.py         # Module to add new videos
├── delete_video.py      # Module to delete videos
└── video_list.txt       # Text file storing video filenames


Prerequisites
Python 3.x installed on your machine.
Videos should be stored in the same directory as the script or provide the full path in the video_list.txt file.


Menu Options
Once the application starts, you'll see a menu with the following options:

Play Video: Play a selected video from the list.
Rearrange Videos: Change the order of videos in the list.
Add Video: Add a new video to the list.
Delete Video: Remove a video from the list.
Exit: Exit the application.


Working
The Video Manager App operates through a menu-driven command-line interface. Each option in the menu corresponds to different functionality provided by separate Python modules. Here’s a detailed explanation of how the application works:

1. Starting the Application
When you run main.py, the application initializes and presents a menu with the following options:

Play Video
Rearrange Videos
Add Video
Delete Video
Exit
You can choose an option by entering the corresponding number.

2. Play Video
Function: play_video.py
How It Works:
Reads the list of video filenames from video_list.txt.
Displays a list of available videos with their index.
Prompts the user to select a video by entering its index.
Uses a system command to play the selected video. The command os.system(f"start {video_to_play}") is used for Windows. For macOS or Linux, this command should be adjusted to open or xdg-open, respectively.
Dependencies: Requires the video file to be present in the same directory or the path to be correctly specified.
3. Rearrange Videos
Function: rearrange_video.py
How It Works:
Reads the list of video filenames from video_list.txt.
Displays the current order of videos with their indices.
Prompts the user to specify the index of the video to move and the new index for that video.
Rearranges the video list based on the provided indices and updates video_list.txt with the new order.
Dependencies: Ensures the indices provided are valid and within range.
4. Add Video
Function: add_video.py
How It Works:
Prompts the user to enter the name of the video file to add, including the .mp4 extension.
Appends the video filename to video_list.txt.
The new video should be in the same directory or the path should be correctly specified.
Dependencies: The video file must be available in the specified location.
5. Delete Video
Function: delete_video.py
How It Works:
Reads the list of video filenames from video_list.txt.
Displays a list of available videos with their index.
Prompts the user to select a video to delete by entering its index.
Removes the selected video from video_list.txt and also deletes the actual video file from the directory.
Dependencies: The video file must be present in the directory for deletion.
6. File Management
video_list.txt: This text file maintains a list of video filenames. Each line should contain one filename with the .mp4 extension. The file is read and updated by the various modules to reflect the current state of the video library.
Example Usage
Playing a Video:

Run the application and select "Play Video".
Choose a video from the list.
The selected video will open using the default video player.
Rearranging Videos:

Select "Rearrange Videos".
Specify the index of the video you want to move and its new position.
The order of videos in video_list.txt will be updated accordingly.
Adding a New Video:

Select "Add Video".
Enter the filename of the new video.
The video will be added to the end of the list in video_list.txt.
Deleting a Video:

Select "Delete Video".
Choose a video from the list to delete.
The video file will be removed from the directory, and its entry will be deleted from video_list.txt.


