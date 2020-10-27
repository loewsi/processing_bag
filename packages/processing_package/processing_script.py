import rosbag
import cv2
from cv_bridge import CvBridge

inbag = rosbag.Bag('/bags/amod20-rh3-ex-record-silvan-loew.bag')
outbag= rosbag.Bag('/bags/outbag.bag', 'w')
br = CvBridge()


for topic, msg, t in inbag.read_messages(topics = '/vonduck/camera_node/image/compressed'):
    time = t.to_sec()
    time_string = str(time)
    im = br.compressed_imgmsg_to_cv2(msg)
    im2 = cv2.putText(im, time_string, (10, 450), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,0), 3)
    msg2 = br.cv2_to_compressed_imgmsg(im2)
    outbag.write('/vonduck/camera_node/image/compressed', msg2, t)

inbag.close()
outbag.close()
print("Bag is created, have fun!")