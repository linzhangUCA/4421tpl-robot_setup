# Project 1: Robot Setup

## Intro
Our goal is to develop a robot with autonomous navigation capability. 
A variety of sensors, actuators and functionalities will be integrated on the board. 
In other words, the robot will be "complicated". We will employ [Robot Operating System (ROS)](https://docs.ros.org/) to ease the complication of managing such a system. 

## Objectives
- Practice mechinacal design, fabrication and assembly.
- Manage a robotic project using ROS.
- Try out developed ROS packages.
- Develop a customized ROS package.  

## Requirements
### 1. (10%) Create a ROS package and organize the robot related resources in this package.
- (2.5%) Save the executables (Python scripts) under `<ros workspace>/src/<this repo>/<package name>/<package name>/`
- (2.5%) Save the mechanical design files (schemetic and STL) under `<ros workspace>/src/<this repo>/<package name>/resources/`
- (2.5%) Verify you can start the node (anywhere) with the command: `ros2 run <package name> <executable name>/`
- (2.5%) Make sure author's information is correctly filled in `package.xml` and `setup.py`.
- To host ROS packages, your may need to prepare the development environment including but not limiting to:
   - Flash **Ubuntu 24.04** on Raspberry Pi 5.
     Refer to [guide](https://ubuntu.com/tutorials/how-to-install-ubuntu-desktop-on-raspberry-pi-4#2-prepare-the-sd-card)
   - Install [ROS 2 **Jazzy** Jalisco](https://docs.ros.org/en/jazzy/Installation/Ubuntu-Install-Debs.html) and [configure ROS environment](https://docs.ros.org/en/jazzy/Tutorials/Beginner-CLI-Tools/Configuring-ROS2-Environment.html).
   - Create [ROS workspace](https://docs.ros.org/en/jazzy/Tutorials/Beginner-Client-Libraries/Creating-A-Workspace/Creating-A-Workspace.html).
   - (Optional) Install [Visual Studio Code](https://code.visualstudio.com/download#) IDE **Arm64** version.
 
### 2. (15%) Design a "coffee-holding" layer for [HomeR](https://github.com/linzhanguca/homer.git).
- (5%) Design a layer which is capable of being integrated to the current [HomeR](https://github.com/linzhanguca/homer.git) robot.
- (10%) A cup holding component for a **12 oz** coffee cup must be considered in your design.
  Refer to the dimension graph below or measure a tall-size Starbucks cup.
  
   ![cup_dimensions](https://www.thepapercupcompany.com/assets/images/double-wall-coffee-dimesions21.gif)
- Anti-spill features and protection against electrical components may earn **extra points**.
  
### 3. (35%) Code (a) ROS node(s).
1. (5%) Subscribe to the **`/cmd_vel` topic** and retrieve the linear and angular velocity from the embedded **[`Twist`](https://docs.ros2.org/foxy/api/geometry_msgs/msg/Twist.html) message**.
2. (10%) Transmit the subscribed linear and angular velocity to the Pico board as **target velocity** for the robot.
3. (20%) receive **actual velocity** from the Pico board.
   Fill a **[`Twist`](https://docs.ros2.org/foxy/api/geometry_msgs/msg/Twist.html) message**.
   Publish the message to **`/homer/real_velocity` topic** at **50 Hz**.
- To publish the `/cmd_vel` topic from an external device (keyboard/gamepad), consider using [`teleop_twist_joy`](https://index.ros.org/r/teleop_twist_joy/) or [`teleop_twist_keyboard`](https://index.ros.org/r/teleop_twist_keyboard/) package.
  
### 4. Document the project using this [README](README.md).

### 5. (10%) Demonstrate remote control and drive the robot along the designated path. 

## Documentation

