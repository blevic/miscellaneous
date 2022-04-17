cmake_minimum_required(VERSION 3.8.2)
project(MyProject VERSION 1.0)

add_library(
    print_hello 
    src/print_hello.c 
    src/print_hello.h
    )

add_executable(
    hello 
    src/main.c
    )

target_link_libraries(hello PRIVATE print_hello)