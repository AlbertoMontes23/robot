#!/usr/bin/env python3
import rospy
import time
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint
cmd_publis=rospy.Publisher('/arm_controller/command',JointTrajectory, queue_size=10)
rospy.init_node('arm_move')
point=JointTrajectoryPoint()
cmd=JointTrajectory()
cmd.joint_names=["arm_base_joint","shoulder_joint", "bottom_wrist_joint", "elbow_joint", "top_wrist_joint"]
point.positions=[-0.1,0.210116830848170721, 0.022747275919015486, 0.0024182584123728645, 0.00012406874824844039]
point.time_from_start=rospy.Duration(10)
cmd.points=[point]

while not rospy.is_shutdown():
	cmd_publis.publish(cmd)



