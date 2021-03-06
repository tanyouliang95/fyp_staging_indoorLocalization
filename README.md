# FYP_IndoorLocalization

**DISCLAIMER**: This package is my first robotics project which involves ROS. Thus, the coding style and conventions are highly not appropriate. The end product still works quite well, but still, I keeping this as a backup!!! Pls use it on your own risk!!! =)


NTU final year project - Vision, encoder odometry and IMU sensor fusion Localization. Vision-based localization depends on VITag marker to identify location in world frame. ROS will be used as the main communication method between multiple nodes. The results for this localization system is shown as below


![alt text](/documentations/fusionResultsPath.png?)

Video link is [here](https://drive.google.com/open?id=1gD1sk_zskcC4AYHtSumUh6on5TwFIL-Y).


Yaml file `markers_config.yaml` will store all configurations and marker coordinates details. In the localization system, 4 main ROS nodes were descripted below: 


## 1) Vision
OpenCV library is used to run VITag marker detection. Access vision source code by entering `cd vision_PoseEstimation`. Run python script `main.py` to start the vision pose estimation process. 

## 2) Raspberry Pi
Raspberry Pi is used to read the signal from IMU and 
### IMU
`RTIMU` is used to access all IMU GPIO in Raspberry pi. `https://github.com/RPi-Distro/RTIMULib`
Calibration can be done in the respective RTIMU calibration script. Run `python read_IMU.py` to read raw IMU reading, Ultimately, acceleration and yaw value will be sent to server. (respect to Earth frame, reference to magnetic north)

### Encoder
2-axis incremental encoders are used to measure odometry. Run `python encoder.py` will enable Raspberry pi to read the sensor displacement reading. Hence output to reading to server


### PC Server
Run `python pc_server.py` to host a server, enable receival of Rasperry IMU and Encoder output. Script will also publish data to ROS_topic, which will be subscribe by vision and fusion node.


## 3) Sensor Fusion
Access sensor fusion code by typing `cd sensorFusion`. In within, there's multiple source codes for sensor fusion node. 

### kalman.py
Iddicated simulation file. Script will auto generate random inputs from "measurement update" and "time update", to show output results in via MATPLOTLIB.

### fusion.py
Sensor fusion script. Will accept topic from Vision input, IMU & encoder script 

## 4) rviz_indoor_localization
For visualization of localization system. `fusion.py` will publish to tf topic, which will be subscribed to visualize the robot coordinate in the world frame

Compile `rviz_indoor_localization` to visualize the localization process, then:
```
roslaunch rviz_indoor_localization display.launch
```

### markers
`rviz_markers.py` to publish coordinates of markers, and visulize real-time robot's path in 2d Environment.

# Detailed Description
For detailed description, please refer to `documentations` folder.
