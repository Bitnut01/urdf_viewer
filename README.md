# URDF Viewer Package

A ROS2 package for visualizing URDF robot models in RViz2. This package allows you to load, view, and manipulate a robot model defined in URDF format with an interactive joint state publisher.

## Description

The URDF Viewer package provides a simple way to visualize robot models in RViz2. It includes:

- A sample robot URDF model
- A customized RViz2 configuration
- Launch files to start all necessary nodes

This tool is useful for:
- Validating URDF models
- Visualizing robot kinematics
- Testing joint movements before deploying to physical hardware

## Prerequisites

- ROS2 (tested on Humble/Iron)
- RViz2
- joint_state_publisher_gui package
- robot_state_publisher package

## Building the Package

To build the package, follow these steps:

1. Clone this repository into your ROS2 workspace's `src` directory:
   ```bash
   cd ~/your_ros2_workspace/src
   # Clone the repository here if you haven't already
   ```

2. Build the package using colcon:
   ```bash
   cd ~/your_ros2_workspace
   colcon build --packages-select urdf_viewer
   ```

3. Source the setup file:
   ```bash
   source install/setup.bash
   ```

## Launching the URDF Viewer

To launch the URDF viewer with the default robot model:

```bash
ros2 launch urdf_viewer view.launch.py
```

This will start:
- The joint_state_publisher_gui for interactive control of the robot's joints
- The robot_state_publisher to broadcast the robot state
- RViz2 with a pre-configured view for visualization

## Customizing

To use your own URDF model:
1. Place your URDF file in the `urdf` directory
2. Update the launch file to reference your model
3. Customize the RViz configuration in the `rviz` directory as needed

## License

Apache-2.0

## Maintainer

- bitnut (wmkuchar@gmail.com)
