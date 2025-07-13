import rclpy

from rclpy.lifecycle import Node
from rclpy.lifecycle import State
from rclpy.lifecycle import TransitionCallbackReturn
from std_msgs.msg import String


class MinimalLifecycleNode(Node):
    def __init__(self, node_name):
        super().__init__(node_name)
        self.node_name: str = node_name
        self.topic_name: str = 'minimal_lifecycle_node_topic'
        self.cnt: int = 0
        self.pub = None
        self.timer = None
        self.get_logger().info(self.node_name + ': initialized.')

    def pub_str(self):
        str_msg = String()
        str_msg.data = self.node_name + ': ' + str(self.cnt)
        self.pub.publish(str_msg)
        self.cnt += 1

    def on_configure(self, state: State) -> TransitionCallbackReturn:
        self.get_logger().info(self.node_name + ': on_configure() is called.')
        self.pub = self.create_publisher(String, self.topic_name, 10)
        self.timer = self.create_timer(1.0, self.pub_str)
        self.timer.cancel()  # stop timer
        return TransitionCallbackReturn.SUCCESS

    def on_activate(self, state: State) -> TransitionCallbackReturn:
        self.get_logger().info(self.node_name + ': on_activate() is called.')
        self.timer.reset()  # restart timer
        return TransitionCallbackReturn.SUCCESS

    def on_deactivate(self, state: State) -> TransitionCallbackReturn:
        self.get_logger().info(self.node_name + ': on_deactivate() is called.')
        self.timer.cancel()  # stop timer
        return TransitionCallbackReturn.SUCCESS

    def on_cleanup(self, state: State) -> TransitionCallbackReturn:
        self.get_logger().info(self.node_name + ': on_cleanup() is called.')
        self.destroy_publisher(self.pub)
        self.destroy_timer(self.timer)
        return TransitionCallbackReturn.SUCCESS

    def on_shutdown(self, state: State) -> TransitionCallbackReturn:
        self.get_logger().info(self.node_name + ': on_shutdown() is called.')
        self.destroy_publisher(self.pub)
        self.destroy_timer(self.timer)
        return TransitionCallbackReturn.SUCCESS


def main():
    rclpy.init()
    executor = rclpy.executors.SingleThreadedExecutor()
    minimal_lifecycle_node_a = MinimalLifecycleNode('minimal_lifecycle_node_a')
    minimal_lifecycle_node_b = MinimalLifecycleNode('minimal_lifecycle_node_b')
    executor.add_node(minimal_lifecycle_node_a)
    executor.add_node(minimal_lifecycle_node_b)
    try:
        executor.spin()
    except (KeyboardInterrupt, rclpy.executors.ExternalShutdownException):
        minimal_lifecycle_node_a.destroy_node()
        minimal_lifecycle_node_b.destroy_node()


if __name__ == '__main__':
    main()
