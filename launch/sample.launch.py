from pathlib import Path

from ament_index_python.packages import get_package_share_directory
import launch
import launch.actions
import launch.substitutions
import launch_ros.actions

def generate_launch_description():
    # server = launch.actions.DeclareLaunchArgument('server', default_value='127.0.0.1')
    # server = launch.substitutions.LaunchConfiguration('server')
    
    # port = launch.actions.DeclareLaunchArgument('port', default_value=3883)
    # port = 3883

    update_frequency = 100.0
    frame_id = 'world'

    # Use the VRPN server's time, or the client's ROS time.
    use_server_time = False

    broadcast_tf = True

    # Must either specify refresh frequency > 0.0, or a list of trackers to create
    refresh_tracker_frequency = 1.0
    # trackers = []
    
    return launch.LaunchDescription([
        launch.actions.DeclareLaunchArgument('server', default_value='127.0.0.1'),
        launch.actions.DeclareLaunchArgument('port', default_value='3883'),
        launch_ros.actions.Node(
            package='vrpn_client_ros',
            executable='vrpn_client_node',
            output='screen',
            emulate_tty=True,
            parameters=[
                {"server": launch.substitutions.LaunchConfiguration('server')},
                {"port": launch.substitutions.LaunchConfiguration('port')},
                {"update_frequency": update_frequency},
                {"frame_id": frame_id},
                {"use_server_time": use_server_time},
                {"broadcast_tf": broadcast_tf},
                {"refresh_tracker_frequency": refresh_tracker_frequency},
            ],
        ),
    ])