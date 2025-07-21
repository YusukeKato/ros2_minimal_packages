# Minimal Gazebo

## Install

[ros2_minimal_packages/README.md/#Install](../README.md#install)

## Start Gazebo

```sh
$ ros2 launch minimal_gazebo minimal_gazebo.launch.py
```

## Start teleop_twist_keyboard

```sh
sudo apt install ros-jazzy-teleop-twist-keyboard
ros2 run teleop_twist_keyboard teleop_twist_keyboard --ros-args -p stamped:=true
```

reference: https://rt-net.github.io/tutorials/raspimouse/simulator/install.html

## Trouble shooting

```sh
$ ros2 launch minimal_gazebo minimal_gazebo.launch.py
...
# Error
[gz sim -r-1] [Err] [SystemLoader.cc:92] Failed to load system plugin [libgz_ros2_control-system.so] : Could not find shared library.
```

Execute the following command:

```sh
export GZ_SIM_SYSTEM_PLUGIN_PATH=/opt/ros/jazzy/lib/
```

reference: https://github.com/ros-controls/gz_ros2_control/issues/390#issuecomment-2374688972

## Reference

- https://gazebosim.org/docs/latest/sdf_worlds/
- [rt-net/raspimouse_sim](https://github.com/rt-net/raspimouse_sim)
  - Copyright (c) 2016 RT Corp.
  - Copyright (c) 2016 Daisuke Sato
  - LICENSE: [MIT License](https://github.com/rt-net/raspimouse_sim/blob/ros2/LICENSE)