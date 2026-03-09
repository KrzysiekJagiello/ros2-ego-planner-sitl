from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='ego_planner',
            executable='ego_planner_node',
            name='ego_planner_node',
            output='screen',
            # prefix=['gdb -ex run --args'],
            parameters=[{
                'fsm/flight_type': 1,
                'manager/drone_id': 0,
                'manager/max_vel': 2.0,
                'manager/max_acc': 6.0,
                'manager/max_jerk': 4.0,
                'manager/planning_horizon': 7.5,
                'manager/control_points_distance': 0.4,
                'manager/use_distinctive_trajs': True,
                'manager/feasibility_tolerance': 0.05,
                
                'grid_map/resolution': 0.1,
                'grid_map/map_size_x': 40.0,
                'grid_map/map_size_y': 40.0,
                'grid_map/map_size_z': 5.0,
                'grid_map/local_update_range_x': 5.5,
                'grid_map/local_update_range_y': 5.5,
                'grid_map/local_update_range_z': 4.5,
                'grid_map/obstacles_inflation': 0.15,
                

                'grid_map/cx': 321.046,
                'grid_map/cy': 243.449,
                'grid_map/fx': 387.229,
                'grid_map/fy': 387.229,
                
                'optimization/max_vel': 2.0,
                'optimization/max_acc': 6.0,
                'optimization/lambda_smooth': 1.0,
                'optimization/lambda_collision': 0.5,
                'optimization/lambda_fitness': 1.0,
                'optimization/dist0': 0.5,
            }],
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