from setuptools import find_packages, setup

package_name = 'minimal_lifecycle_node'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='YusukeKato',
    maintainer_email='yusukekato.contact@gmail.com',
    description='Minimal Lifecycle Node',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'minimal_lifecycle_node = minimal_lifecycle_node.minimal_lifecycle_node:main',
        ],
    },
)
