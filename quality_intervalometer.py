from picamera2 import Picamera2
from time import sleep
import os

def capture_images_with_picamera2(interval_seconds, total_images, save_directory):

    if not os.path.exists(save_directory):
        os.makedirs(save_directory)

    picam2 = Picamera2()

    camera_config = picam2.create_still_configuration()
    picam2.configure(camera_config)

    picam2.start()
    print("Camera is on. I'm starting to take photos...")

    try:
        for i in range(total_images):
      
            filename = os.path.join(save_directory, f"image_{i + 1:04d}.jpg")
        
            picam2.capture_file(filename)
            print(f"Photo {i + 1}/{total_images} save in {filename}")

            sleep(interval_seconds)
    finally:
  
        picam2.stop()
        print("Process complete. Camera turned off.")

capture_images_with_picamera2(interval_seconds=5, total_images=5, save_directory="/home/kuklok/Pictures")
