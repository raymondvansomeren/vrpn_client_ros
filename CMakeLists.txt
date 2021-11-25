cmake_minimum_required(VERSION 3.5)
project(vrpn_client_ros)

find_package(ament_cmake REQUIRED)

list(APPEND CMAKE_MODULE_PATH "${CMAKE_SOURCE_DIR}/vrpn/cmake")
find_package(VRPN REQUIRED)

find_package(rclcpp REQUIRED)
find_package(std_msgs REQUIRED)
find_package(geometry_msgs REQUIRED)
find_package(tf2_ros REQUIRED)
# find_package(tf2 REQUIRED)

set(CMAKE_CXX_STANDARD 17)
add_compile_options(-Wall -Wextra -Wpedantic)

include_directories(include)

add_library(vrpn_client_ros
            src/vrpn_client_ros.cpp
)
ament_target_dependencies(vrpn_client_ros rclcpp std_msgs geometry_msgs tf2_ros VRPN)

add_executable(vrpn_tracker_node src/vrpn_tracker_node.cpp)
target_link_libraries(vrpn_tracker_node vrpn_client_ros)
ament_target_dependencies(vrpn_tracker_node rclcpp std_msgs geometry_msgs tf2 VRPN)

add_executable(vrpn_client_node src/vrpn_client_node.cpp)
target_link_libraries(vrpn_client_node vrpn_client_ros)
ament_target_dependencies(vrpn_client_node rclcpp std_msgs geometry_msgs tf2_ros VRPN)

install(DIRECTORY
    launch
    DESTINATION share/${PROJECT_NAME}/
)

install(TARGETS
    vrpn_client_ros
    ARCHIVE DESTINATION lib
    LIBRARY DESTINATION lib
    RUNTIME DESTINATION bin
)

install(TARGETS
    vrpn_tracker_node
    vrpn_client_node
    DESTINATION lib/${PROJECT_NAME}
)

ament_package()