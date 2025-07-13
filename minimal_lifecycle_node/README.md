# Minimal Lifecycle Node

## Terminal 1

```sh
$ ros2 run minimal_lifecycle_node minimal_lifecycle_node
# [minimal_lifecycle_node_a]: minimal_lifecycle_node_a: initialized.
# [minimal_lifecycle_node_b]: minimal_lifecycle_node_b: initialized.
```

## Terminal 2

```sh
$ ros2 lifecycle set minimal_lifecycle_node_a configure
# Terminal 1 > "minimal_lifecycle_node_a: on_configure() is called."

$ ros2 lifecycle set minimal_lifecycle_node_a activate
# Terminal 1 > "minimal_lifecycle_node_a: on_activate() is called."

# --- Start minimal_lifecycle_node_a publisher ---

$ ros2 lifecycle set minimal_lifecycle_node_a deactivate
# Terminal 1 > "minimal_lifecycle_node_a: on_deactivate() is called."

# --- Stop minimal_lifecycle_node_a publisher ---

$ ros2 lifecycle set minimal_lifecycle_node_b configure
# Terminal 1 > "minimal_lifecycle_node_b: on_configure() is called."

$ ros2 lifecycle set minimal_lifecycle_node_b activate
# Terminal 1 > "minimal_lifecycle_node_b: on_activate() is called."

# --- Start minimal_lifecycle_node_b publisher ---
```

## Terminal 3

```sh
$ ros2 topic echo /minimal_lifecycle_node_topic
# data: 'minimal_lifecycle_node_a: 0'
# ---
# data: 'minimal_lifecycle_node_a: 1'
# ---
# data: 'minimal_lifecycle_node_a: 2'
# ---
# ...
#
# data: 'minimal_lifecycle_node_b: 0'
# ---
# data: 'minimal_lifecycle_node_b: 1'
# ---
# data: 'minimal_lifecycle_node_b: 2'
# ---
# ...
```

## Reference

- [ros2/demos](https://github.com/ros2/demos/)
  - Copyright 2021 Open Source Robotics Foundation, Inc.
  - URL: https://github.com/ros2/demos/tree/jazzy/lifecycle_py
  - LICENSE: [Apache 2.0](https://github.com/ros2/demos/blob/jazzy/LICENSE)