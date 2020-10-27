import rosbag
import cv2
from cv_bridge import CvBridge

inbag = rosbag.Bag('amod20-rh3-ex-record-silvan-loew.bag')
outbag= rosbag.BAG('outbag.bag', 'w')
br = CvBridge()


for topic, msg, t in inbag.read_messages(topics = '/vonduck/camera_node/image/compressed'):
    im = br.imgmsg_to_cv2(msg)
    im2 = cv2.putText(im, t, (10, 10), FONT_HERSHEY_SIMPLEX, 1, (0,0,0))
    msg2 = br.cvt_to_imgmsg(im2)
    outbag.write('/vonduck/camera_node/image/compressed', msg2)

inbag.close()
outbag.close()