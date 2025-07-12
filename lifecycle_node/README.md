# Lifecycle Node

## Terminal 1

```sh
$ ros2 run lifecycle_node lifecycle_node
```

## Terminal 2

```sh
$ ros2 lifecycle set node_a configure
# Terminal 1 > "node_a: on_configure() is called."

$ ros2 lifecycle set node_a activate
# Terminal 1 > "node_a: on_activate() is called."

# --- Start node_a publisher ---

$ ros2 lifecycle set node_a deactivate
# Terminal 1 > "node_a: on_deactivate() is called."

# --- Stop node_a publisher ---

$ ros2 lifecycle set node_b configure
# Terminal 1 > "node_b: on_configure() is called."

$ ros2 lifecycle set node_b activate
# Terminal 1 > "node_b: on_activate() is called."

# --- Start node_b publisher ---
```

## Terminal 3

```sh
$ ros2 topic echo /lifecycle_node_topic
# data: 'node_a: 0'
# ---
# data: 'node_a: 1'
# ---
# data: 'node_a: 2'
# ---
# ...
#
# data: 'node_b: 0'
# ---
# data: 'node_b: 1'
# ---
# data: 'node_b: 2'
# ---
# ...
```