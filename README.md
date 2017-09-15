# Rosbag to Image Extractor README

Extract images from a ROS bag in PNG format.

Usage: python rosbag_to_image.py -b <BAGFILE NAME> -o <OUTPUT DIRECTORY> -t <TOPIC> -s <LEFT/RIGHT> 

optional arguments:

  -h, --help       show this help message and exit
  -b BAGFILE_NAME  Enter Rosbag to extract images from. 
  -o OUTPUT_DIR    Output directory.
  -t IMAGE_TOPIC   Image topic to save.
  -s STEREO_NAME   If stereo, enter left or right, creates diectory accordingly



