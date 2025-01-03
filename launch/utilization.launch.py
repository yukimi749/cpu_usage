import launch
import launch.actions
import launch.substitutions
import launch_ros.actions


def generate_launch_description():

    cpu_utilization = launch_ros.actions.Node(
        package='cpu_usage',
        executable='cpu_utilization',
        )
    listener = launch_ros.actions.Node(
        package='cpu_usage',
        executable='listener',
        output='screen'
        )

    return launch.LaunchDescription([cpu_utilization, listener])
