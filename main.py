import moviepy.editor as mp
import tkinter as tk

# Define a function to play the video when the button is clicked
def play_video():
    video = mp.VideoFileClip("Rick_Astley_Never_Gonna_Give_You_Up.ogv") # Replace this with the path to your video file
    video.preview()

# Create the main window and button
root = tk.Tk()
button = tk.Button(root, text="Jailbreak Device", command=play_video)
button.pack()

# Start the main loop
root.mainloop()
