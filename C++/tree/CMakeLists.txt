cmake_minimum_required(VERSION 3.14)
project(tree)

set(CMAKE_CXX_STANDARD 14)

include_directories(.)
include_directories(cmake-build-debug)

add_executable(tree
        cmake-build-debug/cmake_install.cmake
        cmake-build-debug/CMakeCache.txt
        cmake-build-debug/Makefile
        cmake-build-debug/tree
        cmake-build-debug/tree.cbp
        CMakeLists.txt
        leetcode_106_中序后续二叉树.cpp)
