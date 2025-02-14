import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from std_msgs.msg import Int8


class Talker(Node):
    def __init__(self):
        super().__init__('talker')
        self.publisher1 = self.create_publisher(String, 'chatter', 10)
        self.publisher2 = self.create_publisher(Int8, 'numeric_chatter', 8)

        timer_in_seconds = 0.1
        self.timer = self.create_timer(timer_in_seconds, self.talker_callback)
        self.counter = 0
        self.counter2 = 0

    def talker_callback(self):
        msg1 = String()
        msg1.data = f'Hello World, {self.counter}'
        msg2 = Int8()
        msg2.data = self.counter2
        self.publisher1.publish(msg1)
        self.publisher2.publish(msg2)
        self.get_logger().info(f'Publishing: {msg1.data}')
        self.get_logger().info(f'Publishing: {msg2.data}')
        if self.counter2 < 127:
            self.counter2 += 1
        else:
            self.counter2 = 0
        self.counter += 1
        

        


def main(args=None):
    rclpy.init(args=args)

    talker = Talker()
    rclpy.spin(talker)



if __name__ == '__main__':
    main()


