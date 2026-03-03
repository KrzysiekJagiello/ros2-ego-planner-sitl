from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='ros_gz_bridge',
            executable='parameter_bridge',
            name='gz_bridge',
            arguments=[
                # Sim time
                '/clock@rosgraph_msgs/msg/Clock[gz.msgs.Clock',

                # Sensor data: RGBD camera
                '/camera/points@sensor_msgs/msg/PointCloud2[gz.msgs.PointCloudPacked',
                '/camera/camera_info@sensor_msgs/msg/CameraInfo[gz.msgs.CameraInfo',

                # Joint states
                '/world/iris_runway/model/iris_depth/joint_state@sensor_msgs/msg/JointState[gz.msgs.Model',

                # Odometry
                '/model/iris_depth/odometry@nav_msgs/msg/Odometry[gz.msgs.Odometry'

            ],
            remappings=[
                ('/world/iris_runway/model/iris_depth/joint_state', '/joint_states'),
                ('/model/iris_depth/odometry', '/odom')
            ],
            output='screen'
        )
    ])