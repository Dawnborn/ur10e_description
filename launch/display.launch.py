from launch import LaunchDescription
from launch_ros.actions import Node
from launch.substitutions import Command, PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare
from launch_ros.parameter_descriptions import ParameterValue

def generate_launch_description():
    urdf_path = PathJoinSubstitution([
        FindPackageShare("ur10e_description"),
        "urdf",
        "robot.urdf"
    ])

    rviz_config_path = PathJoinSubstitution([
        FindPackageShare("ur10e_description"),
        "config",
        "ur10e_config.rviz"
    ])

    return LaunchDescription([
        # Robot State Publisher Node
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            output='screen',
            parameters=[{
                'robot_description': ParameterValue(
                    Command(['cat ', urdf_path]),
                    value_type=str
                )
            }]
        ),
        # RViz Node
        Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2',
            output='screen',
            arguments=['-d', rviz_config_path]
        ),
    ])
