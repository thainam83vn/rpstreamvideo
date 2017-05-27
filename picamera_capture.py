import time
import picamera
from datetime import datetime

# Explicitly open a new file called my_image.jpg

i = 0
with picamera.PiCamera() as camera:
    camera.start_preview()
    while True:
        time.sleep(0.1)
        file_name = "" + i + ".jpg"
        my_file = open("images/" + file_name, 'wb')
        camera.capture(my_file)
        my_file.close()
# At this point my_file.flush() has been called, but the file has
# not yet been closed

