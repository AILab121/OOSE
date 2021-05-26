execute_process(COMMAND "/home/ailab/mir_robot_ws/build/mir_robot/mir_driver/catkin_generated/python_distutils_install.sh" RESULT_VARIABLE res)

if(NOT res EQUAL 0)
  message(FATAL_ERROR "execute_process(/home/ailab/mir_robot_ws/build/mir_robot/mir_driver/catkin_generated/python_distutils_install.sh) returned error code ")
endif()
