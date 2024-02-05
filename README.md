# Project 1: Robot Setup

## Intro
Our goal is to develop a robot with autonomous navigation capability. A variety of sensors, actuators and functionalities will be integrated on the board. In other words, the robot will be "complicated". To ease the complication of managing such a system, [ROS 2 Humble](https://docs.ros.org/en/humble/) will be employed. Given a few start up materials, you'll come up with your design of the mobile robot base; assemble the physical prototype; and realize basic management using ROS.  

## Requirements
1. Build a functional mobile robot base.
2. Program a microcontroller to drive motors and monitor the robot's status.
3. Test and analyze features of the robot.
4. Install and configure ROS. Develop ROS package(s) to publish robot's state and listen to remote control commands. 

### (60%) Coding
> Please upload your code to this repository. 
- (25%) Differential driver on microcontroller:
    - Reads linear and angular velocity commands (for the robot) transfered from the serial port.
    - Outputs signals to approapriate GPIO pins to drive the motor at right speed and direction.
    - Transmits **robot's** linear and angular velocity via serial port at **100 Hz**.
- (30%) ROS package for bringing up the robot 
    - The package should contain at least one node. The node(s) should contain a publisher and a subscriber.
    - The node receives the robot's (velocity) states from the microcontroller and transmits the velocity commands to the microcontroller via serial port. 
    - The node publishes the robot's (velocity) state in a topic with **[`geometry_msgs/msg/Twist`](https://docs.ros2.org/latest/api/geometry_msgs/msg/TwistStamped.html)** message at **100 Hz**.
    - The node subscribe to the `/cmd_vel` topic and translate the message according to the microcontroller's script.
- (5%) Remote control
Verify if the robot is controllable using [`teleop_twist_keyboard`](https://index.ros.org/r/teleop_twist_keyboard/) package.
    
### (40%) Documentation
Assuming you are helping people to build a replica of your robot. Please complete the following sections to get them ready and better understand on this project. Please see commented requirements under the title of each section.
1. (5%) Part List.
2. (10%) Wiring Diagram.
3. (20%) Approaches
4. (5%) Summary

## Part List
> List all the parts of your robot. Please refer to the [table formatting guide](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/organizing-information-with-tables)

| Name | Description | Quantity |
| :--- | :---        |  :---:   |
|      |             |          |
|      |             |          |

## Wiring Diagram
> Create a wiring diagram to illustrate hardware configuration. Please refer to the [image insertion guide](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax#images)

![image name](link)

## Approaches
> Your goal is to help people understand this project. Describe your navigation methods in every stage. And all the related technical details (etc. sensors, motor speed, workflows, algorithms, etc.). You are encouraged to draw illustrative diagrams or upload assistive files.

## Summary
> Summarize the project. State the achievements of your robot. Add more supplemental materials (e.g. future designs, ideas, discussions, etc.).
