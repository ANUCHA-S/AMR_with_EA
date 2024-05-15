#! /usr/bin/env python


import rospy
from std_msgs.msg import Bool



SignalforCylinder = False
def callback(data):
	global SignalforCylinder
	rospy.loginfo(data.data)
	SignalforCylinder = data.data
	rospy.signal_shutdown("End")

def listener():
	rospy.init_node('ea_sub', anonymous=True)
	rospy.Subscriber('ea_control',Bool,callback,queue_size=500)
	rospy.spin()
	print (SignalforCylinder)

if __name__ == '__main__':
	listener()
