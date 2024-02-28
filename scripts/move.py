import rclpy
from rclpy.node import Node

from geometry_msgs.msg import Twist


class MinimalPublisher(Node):

    def _init_(self):
        super()._init_('minimal_publisher')
        self.publisher_ = self.create_publisher(Twist, '/diff_drive/cmd_vel', 10)
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)

    def timer_callback(self):
        msg = Twist()
        msg.linear.x=10
        msg.linear.y=0
        msg.linear.z=0
        msg.angular.x=0
        msg.angular.y=0
        msg.angular.z=2
        self.publisher_.publish(msg)
 



def main(args=None):
    rclpy.init(args=args)

    minimal_publisher = MinimalPublisher()

    rclpy.spin(minimal_publisher)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_publisher.destroy_node()
    rclpy.shutdown()


if _name_ == '_main_':
    main()