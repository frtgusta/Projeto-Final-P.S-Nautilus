# Copyright 2022 Open Source Robotics Foundation, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.actions import IncludeLaunchDescription
from launch.conditions import IfCondition
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution

from launch_ros.actions import Node


def generate_launch_description():
    # Configure ROS nodes for launch

    # Setup project paths
    pkg_project_bringup = get_package_share_directory('harpia_proj_final')
    pkg_project_gazebo = get_package_share_directory('harpia_proj_final')
    pkg_project_description = get_package_share_directory('harpia_proj_final')
    pkg_ros_gz_sim = get_package_share_directory('ros_gz_sim')
    
    # Load the SDF file from "description" package
    sdf_file  =  os.path.join(pkg_project_description, 'models', 'carrinho.sdf')
    with open(sdf_file, 'r') as infp:
        robot_desc = infp.read()
    
    # For publishing and controlling the robot pose, we need joint states of the robot
    # Configure the robot model by adjusting the joint angles using the GUI slider
    #joint_state_publisher_gui = Node(
    #    package='joint_state_publisher_gui',
    #    executable='joint_state_publisher_gui',
    #    name='joint_state_publisher_gui',
    #    arguments=[sdf_file],
    #    output=['screen']
    #)

    # Setup to launch the simulator and Gazebo world
    gz_sim = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(pkg_ros_gz_sim, 'launch', 'gz_sim.launch.py')),
        launch_arguments={'gz_args': PathJoinSubstitution([
            pkg_project_gazebo,
            'worlds',
            'proj_final_world.sdf'
        ])}.items(),
    )

    # Takes the description and joint angles as inputs and publishes the 3D poses of the robot links
    robot_state_publisher = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        name='robot_state_publisher',
        output='both',
        parameters=[
            {'use_sim_time': True},
            {'robot_description': robot_desc},
        ]
    )

    # Bridge ROS topics and Gazebo messages for establishing communication
    gz_topic = ''
    
    bridge = Node(
        package='ros_gz_bridge',
        executable='parameter_bridge',
        parameters=[{
            'config_file': os.path.join(pkg_project_bringup, 'params', 'bridges.yaml'),
            'qos_overrides./tf_static.publisher.durability': 'transient_local',
            
        }],
        # arguments=[
        #    '/model/carrinho/cmd_vel@geometry_msgs/msg/Twist@gz.msgs.Twist',
        # ],
        output='screen'
    )

    return LaunchDescription([
        gz_sim,
        bridge,
#        joint_state_publisher_gui,
        robot_state_publisher
    ])