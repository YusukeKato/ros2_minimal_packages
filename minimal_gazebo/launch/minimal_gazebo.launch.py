from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import SetParameter


def generate_launch_description():
    gazebo_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            [
                get_package_share_directory('ros_gz_sim'),
                '/launch/gz_sim.launch.py',
            ]
        ),
        launch_arguments={'gz_args': 'empty.sdf'}.items(),
    )

    return LaunchDescription([
        SetParameter(name='use_sim_time', value=True),
        gazebo_launch,
    ])
