import os
import glob
import shutil
import time

# Gather the source destination directory and whatever other directory you want to sort your files in.
# Specify them with a variable
#~~~~~~
source = r'Src file here' # Source directory (The magic hole)
destination_video = r'file here' # video
destination_picture = r'file here' # picture
destination_sound = r'file here' #sound(music)
#Add as many categories you want!
#~~~~~~
# Filter the files with Global and add the prefixes you want like mp3,MOV etc
videos = glob.glob(os.path.join(source, '*.mp4*'), recursive=True)
pictures = glob.glob(os.path.join(source, '*.PNG*'), recursive=True)
sound = glob.glob(os.path.join(source, '*.mp3*'), recursive=True)
#~~~~~~
# Finally use the directory variable and combine its coresponding filter variable
# Loop until all files have been moved
#Add as many categories you want!
time.sleep(0.33)
for file_path in videos:
    dst_path = os.path.join(destination_video, os.path.basename(file_path))
    shutil.move(file_path, dst_path)
    print(f"Moved {file_path} -> {dst_path}")
#~~~~~~
time.sleep(0.33)
for file_path in pictures:
    dst_path = os.path.join(destination_picture, os.path.basename(file_path))
    shutil.move(file_path, dst_path)
    print(f"Moved {file_path} -> {dst_path}")
#~~~~~~
time.sleep(0.33)
for file_path in sound:
    dst_path = os.path.join(destination_sound, os.path.basename(file_path))
    shutil.move(file_path, dst_path)
    print(f"Moved {file_path} -> {dst_path}")

#Add as many categories you want!
