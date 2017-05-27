import time
import picamera
from shutil import copyfile
from datetime import datetime

# Explicitly open a new file called my_image.jpg

i = 0
with picamera.PiCamera() as camera:
    camera.start_preview()
    while True:
        time.sleep(0.1)
        file_name = "images/" + str(i) + ".jpg"
        my_file = open("images/current.jpg", 'wb')
        camera.capture(my_file)
        my_file.close()
        copyfile("images/current.jpg", file_name)
        i = i + 1
# At this point my_file.flush() has been called, but the file has
# not yet been closed

