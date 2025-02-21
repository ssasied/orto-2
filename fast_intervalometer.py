from picamera2 import Picamera2
import os

def capture_images_fast(total_images, save_directory, resolution=(640, 480)):
  
    # check if directory exit
    if not os.path.exists(save_directory):
        os.makedirs(save_directory)

    # camera init
    picam2 = Picamera2()

    # setup in video(faster) mood
    video_config = picam2.create_video_configuration(main={"size": resolution})
    picam2.configure(video_config)
    picam2.start()

    print("Camera is on. I'm starting to quickly take photos...")

    try:
        for i in range(total_images):
            # Set file with number
            filename = os.path.join(save_directory, f"image_{i + 1:04d}.jpg")
            
            # Take a photo
            picam2.capture_file(filename)
            print(f"Photo {i + 1}/{total_images} save in {filename}")

    finally:
        picam2.stop()
        print("Process complete. Camera turned off.")


capture_images_fast(total_images=100, save_directory="/home/kuklok/Pictures", resolution=(640, 480))
