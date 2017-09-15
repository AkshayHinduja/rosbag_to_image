#Author: Akshay Hinduja
#Robot Perception Lab, RI, CMU 
#!/usr/bin/env python
import rospy
import argparse
import cv2
import os
import rosbag
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

def main():

    parser = argparse.ArgumentParser(description="Extract images from a ROS bag in PNG format.")
    parser.add_argument('-b', action='store', dest='bagfile_name', help='Enter Rosbag to extract images from.')
    parser.add_argument('-o', action='store', dest='output_dir', help='Output directory.')
    parser.add_argument('-t', action='store', dest='image_topic', help="Image topic to save.")
    parser.add_argument('-s', action='store', dest='stereo_name', help="If stereo, enter left or right")

    args = parser.parse_args()

    print "Extracting images from %s for topic %s and saving to %s" % (args.bagfile_name,
                                                          args.image_topic, args.output_dir)




    bag = rosbag.Bag(args.bagfile_name, "r")
    cvbridge_obj = CvBridge()
    n = 0
    for topic, msg, t in bag.read_messages(topics=[args.image_topic]):
        cv_img = cvbridge_obj.imgmsg_to_cv2(msg, desired_encoding="passthrough")
        if os.path.exists(args.output_dir):
            if  args.stereo_name=='left' or args.stereo_name=='right':
                if not (os.path.exists(args.output_dir + "/" + args.stereo_name)):
                        os.makedirs(args.output_dir + "/" + args.stereo_name)
                        cv2.imwrite(os.path.join(args.output_dir + "/" + args.stereo_name, "frame%04i.png" % n), cv_img)
                        print "Saving image %i" % n
                else:
                        cv2.imwrite(os.path.join(args.output_dir + "/" + args.stereo_name, "frame%04i.png" % n), cv_img)
                        print "Saving image %i" % n
            else: 
                    cv2.imwrite(os.path.join(args.output_dir,"frame%04i.png" % n), cv_img)
                    print "Saving image %i" % n
        else:
            if args.stereo_name=='left' or args.stereo_name=='right':
                os.makedirs(args.output_dir+"/" + args.stereo_name)
                cv2.imwrite(os.path.join(args.output_dir + "/" + args.stereo_name, "frame%04i.png" % n), cv_img)
                print "Saving image %i" % n
            else: 
                os.makedirs(args.output_dir)
                cv2.imwrite(os.path.join(args.output_dir , "frame%04i.png" % n), cv_img)
                print "Saving image %i" % n


        n += 1

    bag.close()

    return

if __name__ == '__main__':
    main()
