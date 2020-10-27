import rosbag
import numpy as np
bag = rosbag.Bag('/bags/amod20-rh3-ex-record-silvan-loew.bag')
readtopics = list(bag.get_type_and_topic_info()[1].keys())


for topic, msg, t in bag.read_messages(topics=str(readtopics[i])):
    print(t)