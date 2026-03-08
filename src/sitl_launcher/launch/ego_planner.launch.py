from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='ego_planner',
            executable='ego_planner_node',
            name='ego_planner_node',
            output='screen',
            parameters=[
                {'map_resolution': 0.1},
                {'map_size_x': 40.0},
                {'map_size_y': 40.0},
                {'map_size_z': 5.0},
                {'local_update_range_x': 5.5},
                {'local_update_range_y': 5.5},
                {'local_update_range_z': 4.5},
                {'obstacles_inflation': 0.15}
            ],
            remappings=[
                ('odom_world', '/mavros/local_position/odom'),
                ('grid_map/odom', '/mavros/local_position/odom'),
                ('grid_map/cloud', '/camera/points')
            ]
        ),
        Node(
            package='ego_planner',
            executable='traj_server',
            name='traj_server',
            output='screen',
            parameters=[
                {'traj_server/time_forward': 1.0}
            ],
            remappings=[
                ('position_cmd', '/planning/pos_cmd'),
                ('planning/bspline', '/planning/bspline')
            ]
        )
    ])