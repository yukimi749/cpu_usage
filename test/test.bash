#!/bin/bash
#SPDX-FileCopyrightText: 2024 Yukimi Miyahara
#SPDX-License-Identifier: BSD-3-Clause

dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws
colcon build
source $dir/.bashrc

timeout 10 ros2 launch cpu_usage utilization.launch.py > /tmp/cpu_usage.log 

cat /tmp/cpu_usage.log | grep -E '(100|[1-9][0-9]?)'


