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

## 3. Requirements
1. Create a ROS package and organize the robot related resources in this package.
2. Design a "coffee-holding" layer for the [HomeR](https://github.com/linzhanguca/homer.git).
3. Code (a) ROS node(s) to:
   1. subscribe to the **`/cmd_vel` topic** and retrieve the linear and angular velocity from the embedded **[`Twist`](https://docs.ros2.org/foxy/api/geometry_msgs/msg/Twist.html) message**.
   2. transmit the subscribed linear and angular velocity to the Pico board as **target velocity** for the robot.
   3. receive **actual velocity** from the Pico board.
      Fill a **[`Twist`](https://docs.ros2.org/foxy/api/geometry_msgs/msg/Twist.html) message**.
      Publish the message to **`/<your robot name>/vel` topic** at **50 Hz**.
4. Document the project using this [README](README.md).
5. Demonstrate remote control and drive the robot along the designated path. 


### 3.1 Coding
- Please upload your code to this repository. 
- **(25%)** Differential driver on microcontroller:
    - Reads linear and angular velocity commands (for the robot) transfered from the serial port.
    - Outputs signals to approapriate GPIO pins to drive the motor at right speed and direction.
    - Transmits **robot's** linear and angular velocity via serial port at **100 Hz**.
- **(35%)** ROS package on computer
    - The package should contain at least one node. The node(s) should contain a publisher and a subscriber.
    - The node receives the robot's (velocity) states from the microcontroller and transmits the velocity commands to the microcontroller via serial port. 
    - The node publishes the robot's (velocity) state in a topic with **[`geometry_msgs/msg/Twist`](https://docs.ros2.org/latest/api/geometry_msgs/msg/TwistStamped.html)** message at **100 Hz**.
    - The node subscribe to the `/cmd_vel` topic and translate the message according to the microcontroller's script.
    - Move the robot around using [`teleop_twist_keyboard`](https://index.ros.org/r/teleop_twist_keyboard/) package. Find out the default linear and angular velocity commands for keys: `u`, `i`, `o`, `j`, `k`, `l`, `m`, `,`, `.`. Set appropriate duty cycle for PWM signals which drives the robot.
    
### 3.2 Documentation
- Use this `README` file or create a separate markdown file or upload a pdf file for the documentation.
- Describe the project in concise words. Unless in the Summary section, or:
    - Describe only the final solutions.
    - Don't tell stories.
- Have the documents well organized (break it down into sections). 
- Please include following contents in your documents.
    1. **(10%)** Part list (name, key specifications, functionalities and quantities).
    2. **(10%)** Mechanical layout (sketch(es) with dimensions of key parts and measurements, wiring diagrams)
    3. **(10%)** Mechanical features (describe/list weight, max velocity, max payload capacity)
    4. **(8%)** Software architecture (illustrate key components/modules and communication relationships in a graph) 
    5. **(2%)** Summary this project. You can share any thoughs or interesting findings, or discuss the future of the applications.

