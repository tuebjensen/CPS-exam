# #! /usr/bin/env python3
# '''
# This is a Python script that uses the nav2_simple_commander package to navigate a robot
# through a sequence of pre-defined poses in a ROS 2 environment. The BasicNavigator class
# is used to control the robot's movement, and the PoseStamped class is used to represent each goal pose.
# The setInitialPose() method is used to set the robot's initial position, and goThroughPoses() is used to navigate
# the robot through the sequence of goals.
#  The script waits for the task to complete before printing the result and shutting down the navigator.
# '''
# from geometry_msgs.msg import PoseStamped
# from nav2_simple_commander.robot_navigator import BasicNavigator, TaskResult
# import rclpy
# from rclpy.duration import Duration

# def main():
#     rclpy.init()
#     goals=[]
#     navigator = BasicNavigator()
#     initial_pose = PoseStamped()
#     initial_pose.header.frame_id = 'map'
#     initial_pose.header.stamp = navigator.get_clock().now().to_msg()
#     initial_pose.pose.position.x = -2.5
#     initial_pose.pose.position.y = 2.8
#     initial_pose.pose.orientation.z = 0.0
#     initial_pose.pose.orientation.w = 1.0
#     navigator.setInitialPose(initial_pose)

#     navigator.waitUntilNav2Active()


#     # Go to our demos first goal pose
#     goal_pose = PoseStamped()
#     goal_pose.header.frame_id = 'map'
#     goal_pose.header.stamp = navigator.get_clock().now().to_msg()
#     goal_pose.pose.position.x = -5.8
#     goal_pose.pose.position.y = -0.5
#     goal_pose.pose.orientation.w = 1.0
#     goals.append(goal_pose)

#     # goal_pose_1 = PoseStamped()
#     # goal_pose_1.header.frame_id = 'map'
#     # goal_pose_1.header.stamp = navigator.get_clock().now().to_msg()
#     # goal_pose_1.pose.position.x =-7.4
#     # goal_pose_1.pose.position.y =-1.17
#     # goal_pose_1.pose.orientation.w =0.99
#     # goals.append(goal_pose_1)


#     navigator.goThroughPoses(goals)
#     while not navigator.isTaskComplete():
#         pass


#     # Do something depending on the return code
#     result = navigator.getResult()
#     if result == TaskResult.SUCCEEDED:
#         print('Goal succeeded!')
#     elif result == TaskResult.CANCELED:
#         print('Goal was canceled!')
#     elif result == TaskResult.FAILED:
#         print('Goal failed!')
#     else:
#         print('Goal has an invalid return status!')

#     navigator.lifecycleShutdown()

#     exit(0)


# if __name__ == '__main__':
#     main()


#! /usr/bin/env python3
'''
This is a Python script that uses the nav2_simple_commander package to navigate a robot
through a sequence of pre-defined poses in a ROS 2 environment. The BasicNavigator class
is used to control the robot's movement, and the PoseStamped class is used to represent each goal pose.
The setInitialPose() method is used to set the robot's initial position, and goThroughPoses() is used to navigate
the robot through the sequence of goals.
 The script waits for the task to complete before printing the result and shutting down the navigator.
'''
from geometry_msgs.msg import PoseStamped
from nav2_simple_commander.robot_navigator import BasicNavigator, TaskResult
import rclpy
from rclpy.duration import Duration

def main():
    rclpy.init()

    goals=[]
    navigator = BasicNavigator()
    initial_pose = PoseStamped()
    initial_pose.header.frame_id = 'map'
    initial_pose.header.stamp = navigator.get_clock().now().to_msg()
    initial_pose.pose.position.x = -2.5
    initial_pose.pose.position.y = 2.8
    initial_pose.pose.orientation.z = 0.0
    initial_pose.pose.orientation.w = 1.0
    navigator.setInitialPose(initial_pose)

    navigator.waitUntilNav2Active()


    # Go to our demos first goal pose
    goal_pose = PoseStamped()
    goal_pose.header.frame_id = 'map'
    goal_pose.header.stamp = navigator.get_clock().now().to_msg()
    goal_pose.pose.position.x = -5.8
    goal_pose.pose.position.y = -0.5
    goal_pose.pose.orientation.w = 1.0


    logger = navigator.get_logger()
    navigator.goToPose(goal_pose)
    while not navigator.isTaskComplete():
        feedback = navigator.getFeedback()
        print(
            feedback.current_pose.header.stamp.sec + feedback.current_pose.header.stamp.nanosec / (10 ** 9),
            feedback.estimated_time_remaining.sec +  feedback.estimated_time_remaining.nanosec / (10 ** 9),
            feedback.distance_remaining
        )


    # Do something depending on the return code
    result = navigator.getResult()
    if result == TaskResult.SUCCEEDED:
        print('Goal succeeded!')
    elif result == TaskResult.CANCELED:
        print('Goal was canceled!')
    elif result == TaskResult.FAILED:
        print('Goal failed!')
    else:
        print('Goal has an invalid return status!')

    navigator.lifecycleShutdown()

    exit(0)

if __name__ == '__main__':
    main()