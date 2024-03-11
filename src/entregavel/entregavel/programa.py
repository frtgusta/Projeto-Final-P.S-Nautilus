import rclpy
from rclpy.node import Node
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Twist


class Assinante(Node):
    def __init__(self):
        super().__init__('Assinante')
        self.get_logger().info('Escutando topico')

        self._dados = {}
        self._carrinho = self.create_subscription(Odometry, "/carrinho/odometry", self.carrinho, 10)
        self._alvo1 = self.create_subscription(Odometry, "/alvo1/odometry", self.alvo1, 10)
        self._alvo2 = self.create_subscription(Odometry, "/alvo2/odometry", self.alvo2, 10)
        self._alvo4 = self.create_subscription(Odometry, "/alvo4/odometry", self.alvo3, 10)
        self._alvo5 = self.create_subscription(Odometry, "/alvo5/odometry", self.alvo4, 10)
        self._alvo3 = self.create_subscription(Odometry, "/alvo3/odometry", self.alvo5, 10)

        self._publicador = self.create_publisher(Twist, "cmd_vel", 10)
        self.create_timer(1, self.publicar_velocidade)
       
    def carrinho(self, objeto):
        vel_linear = objeto.twist.linear
        vel_angular = objeto.twist.angular
        position = objeto.pose.position

        self._dados["carro"] = {"posição" : position, "linear" : vel_linear, "angular" : vel_angular}

    def alvo1(self, objeto):
        position = objeto.pose.position
        self._dados["Alvo1"] = position

    def alvo2(self, objeto):
        position = objeto.pose.position
        self._dados["Alvo2"] = position
    
    def alvo3(self, objeto):
        position = objeto.pose.position
        self._dados["Alvo3"] = position
    
    def alvo4(self, objeto):
        position = objeto.pose.position
        self._dados["Alvo4"] = position
    
    def alvo5(self, objeto):
        position = objeto.pose.position
        self._dados["Alvo5"] = position

    def atualizar_velocidade(self):
        carro = self._dados["carro"] # Pego a posição do carro

        for alvo in self._dados:
            for coordenada in ["x","y","z"]: #Atualiza a velocidade do carro em cada eixo
                if getattr(self._dados[alvo], coordenada) > getattr(carro["posição"], coordenada):
                    setattr(carro["linear"], coordenada, 1)
                if getattr(self._dados[alvo], coordenada) < getattr(carro["posição"], coordenada):
                    setattr(carro["linear"], coordenada, -1)
                if getattr(self._dados[alvo], coordenada) == getattr(carro["posição"], coordenada):
                    setattr(carro["linear"], coordenada, 0)
            
            if alvo != "carro": #verifica se a posição do carro é a mesma que a do alvo, se for, elimina o alvo pra no próximo loop começar pelo próximo
                if carro["posição"] == self._dados[alvo]: 
                    del self._dados[alvo]

        # Atualizando o tópico da velocidade do carro
        vel = Twist()
        vel.linear.x = carro["linear"].x
        vel.linear.y = carro["linear"].y
        vel.linear.z = carro["linear"].z

        vel.angular.x = carro["angular"].x
        vel.angular.y = carro["angular"].y
        vel.angular.z = carro["angular"].z

        self._publicador.publish(vel)


def main(args=None):
    rclpy.init(args=args)
    assinante =  Assinante()
    rclpy.spin(assinante)
    rclpy.shutdown()
    
    
    
if __name__ == '__main__':
    main()