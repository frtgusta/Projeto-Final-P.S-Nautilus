
import rospy
from geometry_msgs.msg import Twist

def main():
    rospy.init_node('controle_robo')
    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    rate = rospy.Rate(10)

    while not rospy.is_shutdown():
        twist = Twist()
        twist.linear.x = 0.5  
        twist.angular.z = 0.0 
        pub.publish(twist)
        rate.sleep()

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
