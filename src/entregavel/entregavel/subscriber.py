import rclpy
from rclpy.node import Node
from nav_msgs.msg import Odometry


class Assinante(Node):
    def __init__(self):
        super().__init__('Assinante')
        self.get_logger().info('Escutando topico')
        self._carrinho = self.create_subscription(Odometry, "/carrinho/odometry", self.carrinho, 10)
        self._alvo1 = self.create_subscription(Odometry, "/alvo1/odometry", self.alvo1, 10)
        self._alvo2 = self.create_subscription(Odometry, "/alvo2/odometry", self.alvo2, 10)
        self._alvo4 = self.create_subscription(Odometry, "/alvo4/odometry", self.alvo3, 10)
        self._alvo5 = self.create_subscription(Odometry, "/alvo5/odometry", self.alvo4, 10)
        self._alvo3 = self.create_subscription(Odometry, "/alvo3/odometry", self.alvo5, 10)
       
    def carrinho(self, objeto):
        vel_linear = objeto.twist.linear
        vel_angular = objeto.twist.angular
        position = objeto.pose

    def alvo1(self, objeto):
        vel_linear = objeto.twist.linear
        vel_angular = objeto.twist.angular
        position = objeto.pose

    def alvo2(self, objeto):
        vel_linear = objeto.twist.linear
        vel_angular = objeto.twist.angular
        position = objeto.pose
    
    def alvo3(self, objeto):
        vel_linear = objeto.twist.linear
        vel_angular = objeto.twist.angular
        position = objeto.pose
    
    def alvo4(self, objeto):
        vel_linear = objeto.twist.linear
        vel_angular = objeto.twist.angular
        position = objeto.pose
    
    def alvo5(self, objeto):
        vel_linear = objeto.twist.linear
        vel_angular = objeto.twist.angular
        position = objeto.pose


def main(args=None):
    rclpy.init(args=args)
    assinante =  Assinante()
    rclpy.spin(assinante)
    rclpy.shutdown()
    
    
    
if __name__ == '__main__':
    main()