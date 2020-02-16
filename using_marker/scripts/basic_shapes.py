#!/usr/bin/env python

import rospy
from visualization_msgs.msg import Marker


def switch_object(argument):                #change shapes
    switcher = {
            0: 3,
            1: 2,
            2: 0,
            3: 1,
        }
    return switcher.get(argument, "Invalid")


if __name__=="__main__":
    rospy.init_node("basic_shapes", anonymous=True)
    r = rospy.Rate(1)
    pub = rospy.Publisher("visualization_marker", Marker, queue_size=10)
    marker = Marker()
    marker.type = marker.CUBE             #first shape is cube then we change them below




    while not rospy.is_shutdown():
#        marker = Marker()
        marker.header.frame_id = "/my_frame"
        marker.header.stamp = rospy.Time.now()
        marker.ns = "basic_shapes"
        marker.id = 0
#        marker.type = marker.SPHERE
        marker.action = marker.ADD
        marker.pose.position.x = 0
        marker.pose.position.y = 0
        marker.pose.position.z = 0
        marker.pose.orientation.x = 0.0
        marker.pose.orientation.y = 0.0
        marker.pose.orientation.z = 0.0
        marker.pose.orientation.w = 0.0
        marker.scale.x = 1.0
        marker.scale.y = 1.0
        marker.scale.z = 1.0
        marker.color.r = 0.0
        marker.color.g = 1.0
        marker.color.b = 0.0
        marker.color.a = 1.0
        marker.lifetime = rospy.Duration()

        pub.publish(marker)
        rospy.loginfo(marker.type)
        print switch_object(marker.type)
        marker.type = switch_object(marker.type)
        r.sleep()
