#! /usr/bin/env python

import rospy
from std_msgs.msg import Bool

def talker(Status):
	rospy.init_node('ea', anonymous=True)
	pub = rospy.Publisher("ea_control",Bool,queue_size=500)
	SignalforCylinder = Status
	rospy.loginfo(SignalforCylinder)
	pub.publish(SignalforCylinder)

print('Select 1 for Z axial 100 mm.')
print('Select 2 for x axial 0 mm')
ytt
eaway = input("EA x axial ")

while not rospy.is_shutdown():    
	if eaway == 1:  
		for i in range(1000):
			talker(True)
	if eaway == 2:  
		for i in range(1000):
			talker(False)
	exit()

