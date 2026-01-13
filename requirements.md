# Project Instructions

## Background
Recall the final project of Robotics I.
Were you struggling with managing the components on the lab rover (despite how naive it was)?
Have you ever imagined upgrading the rover with extended computers, sensors and actuators?

The [Robot Operating System (ROS)](https://docs.ros.org/en/jazzy/index.html) is here to help.
With its inherent modularity, which effectively turns software development into a "building block" architecture similar to assembling Legos. 
Rather than writing a single, monolithic script that is hard to maintain and debug, ROS allows you to break your robot’s complex functions into independent, isolated "nodes" that communicate through a universal messaging system. 

In this project, your team will start building the mobile base of the coffee delivery robot.
You will practice managing the robot using a ROS package and several ROS compatible modules.


## Requirements
- Upload your ROS package to this repository.
- Complete documentation in [README](README.md) to inspire interested people.

### 1. Portrait
- Take a **clear** picture of your robot.
- **Label** the key components of the robot in the picture.
- **Display** the labeled portrait in [README](README.md).

> [!IMPORTANT]
> The portrait has to match the robot used for the demonstration.

> [!TIP]
> Find a good viewing angle.
> BearCar has a good [example](https://ucaengineeringphysics.github.io/bearcar_docs/images/bearcar_annotate.png).

### 2. (10%) Mechanical Design.
Please upload all the mechanical drawings into the [drawings/mechanical](drawings/mechanical) directory to illustrate the following.
- All 3D printed and customized parts' dimensions.
- The driving wheel's dimensions.
- Layout (spatial relationship) of the base, Raspberry Pi 5, driving wheels and the caster wheel.

> [!NOTE]
> - Engineering drawings' [format](https://www.mcgill.ca/engineeringdesign/step-step-design-process/basics-graphics-communication/drawing-format-and-elements) is prefered.
> - **Bonus** will be given to innovated mechanical designs in a scale of 0% to 5% of the project's total.

### 2. (20%) Electrical Design.
Please upload all the electrical drawings into the [drawings/electrical](drawings/electrical) directory to illustrate the following.
- Power distribution/management for all the electrical components.
  - Please specify input and/or output voltage of each component.
  - Please specify the power connectors/wires' names.
- Signal flows among Raspberry Pi 5, Pico, and the motor drivers.
  - Please specify hardware interfaces used for these signals.
  - Please specify direction of each signal.

> [!NOTE]
> - The electric flows output to motors are considered as power consumptions, thus can be ignored in the signal wiring diagram.  
> - **Bonus** will be given to innovated electrical designs in a scale of 0% to 5% of the project's total.

### 3. (35%) ROS Package Organization.
1. (5%) Subscribe to the **`/cmd_vel` topic** and retrieve the linear and angular velocity from the embedded **[`Twist`](https://docs.ros2.org/foxy/api/geometry_msgs/msg/Twist.html) message**.
2. (15%) Transmit the subscribed linear and angular velocity to the Pico board as **target velocity** for the robot.
3. (15%) receive **actual velocity** from the Pico board.
   Fill a **[`Twist`](https://docs.ros2.org/foxy/api/geometry_msgs/msg/Twist.html) message**.
   Publish the message to **`/homer/real_velocity` topic** at **50 Hz**.
- You are responsible for setting up the communication between the Pico board and the Raspberry Pi 5.
- To publish the `/cmd_vel` topic from an external device (keyboard/gamepad), consider using [`teleop_twist_joy`](https://index.ros.org/r/teleop_twist_joy/) or [`teleop_twist_keyboard`](https://index.ros.org/r/teleop_twist_keyboard/) package.
  
### 4. (30%) Coding
1. (5%) Illustrate a Schematic of mechanical design with specific dimensions and locations of key components.
2. (10%) Illustrate a Wiring diagram for the relationships among the batteries, motors, motor driver, Pico board, power management board and Raspberry Pi.
   Please mark/denote the signal wires and power wires.
3. (5%) Illustrate a graph of ROS Nodes with all participating/active nodes and topics.
4. (15%) Estimate the robot's **pose**.
   - Given the following conditions.
      1. Using the same temporal and spatial setups as described in [Assignment 3](https://classroom.github.com/a/R9LNWs9-)
      2. Let the robot initiated at the state: $$(X_0 = 0, Y_0 = 0, \theta_0 = 0, v_0 = 0.5, \omega_0 = \pi/3)$$
      3. Keep the linear and angular velocity the same and let them last for 1.2 seconds.
      4. Use the same frequency as the `/homer/real_velocity` topic use to estimate the robot's pose.
   - Please estimate the robot's final pose with the key procedures/equations.
     
### 5. (5%) Demonstration. 
Remotely control your robot to travel along the path as required in the [final project](https://classroom.github.com/a/6rpdyl8z) in Robotics 1.
Using either the keyboard on a laptop or a gamepad to drive your robot.

### 6. AI Policies
Please acknowledge AI's contributions according to the policies in the [syllabus](https://linzhanguca.github.io/_docs/robotics2-2025/syllabus.pdf).


### An Example of Estimating Robot's State
