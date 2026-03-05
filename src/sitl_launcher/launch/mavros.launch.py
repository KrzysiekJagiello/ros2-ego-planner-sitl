import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    pkg_share = get_package_share_directory('sitl_launcher')

    mavros_node = Node(
        package='mavros',
        executable='mavros_node',
        namespace='mavros',
        output='screen',
        parameters=[
            os.path.join(pkg_share, 'config', 'apm_pluginlists.yaml'),
            os.path.join(pkg_share, 'config', 'apm_config.yaml'),
            {
                'fcu_url': 'udp://127.0.0.1:14551@',
                'gcs_url': '',
                'tgt_system': 1,
                'tgt_component': 1,
                'fcu_protocol': 'v2.0'
            }
        ]
    )

    return LaunchDescription([
        mavros_node
    ])