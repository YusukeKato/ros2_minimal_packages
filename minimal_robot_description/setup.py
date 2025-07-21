from glob import glob
import os

from setuptools import find_packages, setup

package_name = 'minimal_robot_description'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'config'),
            glob(os.path.join('config', '*.rviz'))),
        (os.path.join('share', 'minimal_gazebo', 'config'),
            glob(os.path.join('config', '*.yaml'))),
        (os.path.join('share', package_name, 'urdf'),
            glob(os.path.join('urdf', '*.xacro'))),
        (os.path.join('share', package_name, 'launch'),
            glob(os.path.join('launch', '*.launch.py'))),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='YusukeKato',
    maintainer_email='yusukekato.contact@gmail.com',
    description='Minimal Robot Description',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        ],
    },
)
