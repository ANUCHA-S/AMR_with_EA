#! /usr/bin/env python

import actionlib
import rospy

from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal, MoveBaseFeedback, MoveBaseResult
from geometry_msgs.msg import Pose, PoseStamped
from std_msgs.msg import Bool


def talker(Status):
#rospy.init_node('ea', anonymous=True)
	pub = rospy.Publisher("ea_control",Bool,queue_size=500)
	SignalforCylinder = Status
	rospy.loginfo(SignalforCylinder)
	pub.publish(SignalforCylinder)


rospy.init_node('send_client_goal', anonymous=True)

client = actionlib.SimpleActionClient('/move_base', MoveBaseAction)
rospy.loginfo("Waiting for move base server")
client.wait_for_server()

print('Select 0 for goto Bedroom')
print('Select 1 for goto Living Room')
print('Select 2 for goto Kitchen')
print('Select 3 for goto Home')

waypoint = input("Location: ")

while not rospy.is_shutdown():    
	if waypoint == 0:
            goal = MoveBaseGoal()
            goal.target_pose.header.frame_id = 'odom'
            goal.target_pose.header.stamp = rospy.Time.now()
            goal.target_pose.pose.position.x = 3.0
            goal.target_pose.pose.position.y = -1.0
            goal.target_pose.pose.orientation.w = 0.74
            goal.target_pose.pose.orientation.z = -0.67
            #rospy.loginfo('Sending to Bedroom succeeded!')
            client.send_goal(goal)
	    client.wait_for_result()
	    if client.get_state() == actionlib.GoalStatus.SUCCEEDED:
	    	rospy.loginfo('Sending to Bedroom succeeded!')

		for i in range(1000):
			talker(True)
	
	    exit()
	
        if waypoint == 1:   
            goal = MoveBaseGoal()
            goal.target_pose.header.frame_id = 'odom'
            goal.target_pose.header.stamp = rospy.Time.now()
            goal.target_pose.pose.position.x = 11.0
            goal.target_pose.pose.position.y = 3.5
            goal.target_pose.pose.orientation.w = 0.74
            goal.target_pose.pose.orientation.z = 0.67
            #rospy.loginfo('Sending to Living Room succeeded!')
            client.send_goal(goal)
	    client.wait_for_result()
	    if client.get_state() == actionlib.GoalStatus.SUCCEEDED:
	    	rospy.loginfo('Sending to Living Room succeeded!')
	    exit()
	
        if waypoint == 2:   
            goal = MoveBaseGoal()
            goal.target_pose.header.frame_id = 'odom'
            goal.target_pose.header.stamp = rospy.Time.now()
            goal.target_pose.pose.position.x = 15.0
            goal.target_pose.pose.position.y = -1.0
            goal.target_pose.pose.orientation.w = 0.74
            goal.target_pose.pose.orientation.z = -0.67
            #rospy.loginfo('Sending to Kitchen succeeded!')
            client.send_goal(goal)
	    client.wait_for_result()
	    if client.get_state() == actionlib.GoalStatus.SUCCEEDED:
	    	rospy.loginfo('Sending to Kitchen succeeded!')
	    exit()
	
        if waypoint == 3:   
            goal = MoveBaseGoal()
            goal.target_pose.header.frame_id = 'odom'
            goal.target_pose.header.stamp = rospy.Time.now()
            goal.target_pose.pose.position.x = 0.0
            goal.target_pose.pose.position.y = 0.0
            goal.target_pose.pose.orientation.w = 1.0
            goal.target_pose.pose.orientation.z = 0.0
            #rospy.loginfo('Sending to Home succeeded!')
            client.send_goal(goal)
	    client.wait_for_result()
	    if client.get_state() == actionlib.GoalStatus.SUCCEEDED:
	    	rospy.loginfo('Sending to Home succeeded!')

		for i in range(1000):
			talker(False)
	
	    exit()
	client.wait_for_result()	    
	exit()

