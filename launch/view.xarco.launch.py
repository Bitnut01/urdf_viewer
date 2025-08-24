from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration, Command, PathJoinSubstitution, FindExecutable
from launch_ros.substitutions import FindPackageShare
from launch_ros.parameter_descriptions import ParameterValue
from launch_ros.actions import Node

def generate_launch_description():
    pkg = FindPackageShare('urdf_viewer')
    xacro_file = PathJoinSubstitution([pkg, 'urdf', 'test.urdf.xacro'])
    rviz_config = PathJoinSubstitution([pkg, 'rviz', 'os1zed2.rviz'])

    # (opcjonalnie) argumenty do xacro:
    use_sim_time = LaunchConfiguration('use_sim_time')

    return LaunchDescription([
        DeclareLaunchArgument('use_sim_time', default_value='false'),

        Node(
            package='joint_state_publisher',
            executable='joint_state_publisher',
            name='joint_state_publisher'
        ),

        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            parameters=[{
                # uruchamiamy xacro i przekazujemy wynik jako string URDF
                'robot_description': ParameterValue(
                    Command([
                        FindExecutable(name='xacro'),
                        ' ',
                        xacro_file
                    ]),
                    value_type=str
                )
            }]
        ),

#        Node(
#            package='rviz2',
#            executable='rviz2',
#            name='rviz2',
#            arguments=['-d', rviz_config],
#            output='screen'
#        ),
    ])
