# Reference
# https://github.com/rt-net/raspimouse_sim/blob/ros2/raspimouse_gazebo/launch/raspimouse_with_emptyworld.launch.py
import os

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import ExecuteProcess
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
from launch_ros.actions import SetParameter


def generate_launch_description():
    gazebo_world = os.path.join(
        get_package_share_directory('minimal_gazebo'), 'worlds', 'empty.sdf'
    )
    gazebo_config = os.path.join(
        get_package_share_directory('minimal_gazebo'), 'config', 'gazebo.config'
    )
    gz_sim_command = ExecuteProcess(
        cmd=[
            'gz sim -r', gazebo_world,
            '--gui-config', gazebo_config,
        ],
        shell=True,
    )

    gazebo_spawn_node = Node(
        package='ros_gz_sim',
        executable='create',
        arguments=[
            '-topic', '/robot_description',
            '-name', 'minimal_wheeled_robot',
            '-z', '0.1',
        ],
    )

    minimal_robot_description_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            [
                get_package_share_directory('minimal_robot_description'),
                '/launch/minimal_wheeled_robot.launch.py',
            ]
        ),
    )

    spawn_diff_drive_controller_node = Node(
        package='controller_manager',
        executable='spawner',
        arguments=['diff_drive_controller'],
    )

    spawn_joint_state_broadcaster_node = Node(
        package='controller_manager',
        executable='spawner',
        arguments=['joint_state_broadcaster'],
    )

    bridge_node = Node(
        package='ros_gz_bridge',
        executable='parameter_bridge',
        arguments=[
            '/clock@rosgraph_msgs/msg/Clock[gz.msgs.Clock',
        ],
    )

    return LaunchDescription([
        SetParameter(name='use_sim_time', value=True),
        gz_sim_command,
        minimal_robot_description_launch,
        spawn_diff_drive_controller_node,
        spawn_joint_state_broadcaster_node,
        gazebo_spawn_node,
        bridge_node,
    ])
