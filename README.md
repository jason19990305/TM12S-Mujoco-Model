# TM12S Mujoco Model

This project primarily provides the Mujoco model for the TM Robot tm12s robotic arm. The model is built based on the resources in the ROS Github repository of TM Robot. We use ROS tools and the obj2mjcf tool to handle URDF format components and decompose the obj model into Mujoco simulation.

- `scene_grid.xml`: XML file describing the grid floor scene.
- `tm12s.xml`: XML file describing the robotic arm.
- `simulate.gif`: GIF file showing the simulation.
- `tm12s.png`: PNG image of the robotic arm.
- `tmrobot_sim.py`: Python example of robot simulation.

## Robotic Arm

The `tm12s.xml` file describes the TM Robot tm12s robotic arm. This is the main object of our simulation.

## Grid Floor Scene

The `scene_grid.xml` file describes the grid floor scene. This is used as the environment for robot simulation.

![](https://github.com/jason19990305/TM12S-Mujoco-Model/blob/main/tm12s.png)
![](https://github.com/jason19990305/TM12S-Mujoco-Model/blob/main/simulate.gif)



## Installation and Usage

### Install Mujoco

1. Please refer to the [Mujoco official documentation](https://github.com/google-deepmind/mujoco) for installation.

2. To install the Python Mujoco package, enter the following command in the terminal:

```bash
pip install mujoco-py
```

### Usage

To run `tmrobot_sim.py`, enter the following command in the terminal:
```bash
python tmrobot_sim.py
```

