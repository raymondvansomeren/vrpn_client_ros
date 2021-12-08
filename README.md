# VRPN_CLIENT_ROS

## Requirements
* VRPN 07.34 ([download](https://github.com/vrpn/vrpn/releases)/`curl -L https://github.com/vrpn/vrpn/releases/download/version_07.34/vrpn_07.34.zip > vrpn_07.34.zip` / [compile instructions](https://github.com/vrpn/vrpn/wiki/Getting-Started#compiling))
  * Unzip VRPN to the root of this project
  * Filesystem right now should look like:
    * vrpn_client_ros/
      * include/
      * src/
      * vrpn/
  * With a terminal
    * `cd vrpn` (cd into your unzipped folder)
    * `mkdir build && cd build`
    * `cmake ..`
    * `make`
    * `sudo make install`

## How to run
With the filesystem looking a bit like this:
* vrpn_client_ros/
  * include/
  * src/
  * vrpn/
    * build/
In a terminal at `vrpn_client_ros/`
* Run `colcon build`
* `. install/setup.bash`
* `ros2 launch vrpn_client_ros sample.launch.py server:=192.168.137.1` (where `192.168.137.1` the ip is the ip of the pc which is running motive (on the same network))


<!-- ## Getting VRPN

1. Download the latest release of VRPN (this is 07.34 at the moment of writing): https://github.com/vrpn/vrpn/releases
2. Follow the directions at https://github.com/vrpn/vrpn/wiki/Getting-Started#compiling -->

## Known bugs
* The client crashes when a new rigid body gets created in motive
