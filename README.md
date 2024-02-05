# Project 1: Robot Setup

## Background
Our goal is to develop a robot with autonomous navigation capability. A variety of sensors, actuators and functionalities will be integrated on the board. In other words, the robot will be "complicated". To ease the complication of managing such a system, [ROS 2 Humble](https://docs.ros.org/en/humble/) will be employed. Given a few start up materials, you'll come up with your design of the mobile robot base; assemble the physical prototype; and realize basic management using ROS.  

## Requirements:
1. Build the robot's mobile base.
2. Program a microcontroller to drive motors and monitor the robot's status.
3. Test and analyze features of the robot.
4. Install and configure ROS. Develop ROS package(s) to publish robot's state and listen to remote control commands. 

### (60%) Coding:
- Please upload your code to this repository. A Python script running on the computer and another python script running on the Pico board are expected. 
- As there are more more than 1 solutions, the only criterion is to navigate use the designated sensor as the main source.  
- (20%) Stage 1 - Encoder Navigation:
    - **Start the robot on or behind the "Stage 1 Start Line"**.
    - You may need to plan a good trajectory first.
    - Calculate encoder counts based on planned trajectory.
    - (5%) **Stop at the "Stage 2 Start Area" in the end**.
    - Refer to [Assignment 5](https://classroom.github.com/a/vAs41PAP).

- (20%) Stage 2 - Lidar Navigation:
    - You may want to use walls to do wall following.
    - (5%) **Stop at the "Stage 3 Start Area" in the end**.
    -  **Hint: you can hard code time to stop this stage**
    - Refer to [Assignment 6](https://classroom.github.com/a/0LxkqZrp).

- (20%) Stage 3 - Camera Navigation:
    - You may find an ArUco marker useful as a target.
    - You are allowed to move the marker to guide the robot approaching the final destination.
    - (5%) **Stop within 1 meter to the goal**.
    - Refer to [Robotic Vision's slides](https://linzhanguca.github.io/_docs/robotics_1-2023/1114/vision.pdf).
 
    
#### Helpful Resources:
- [Need send data from computer to micro-controller?](https://github.com/linzhangUCA/3421tpl-preliminary_navigation/blob/e9c1038da02bca8127d7bb059af717bda7670a1a/example_computer_talker_listener.py)
- [Need send data from micro-controller to computer?](https://github.com/linzhangUCA/3421tpl-preliminary_navigation/blob/9f3da94dea0d3793ad8117b58b8f6c77060568cf/example_pico_listener_talker.py)
- [Need remotely access RPi?](https://www.realvnc.com/en/connect/download/viewer/)

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
