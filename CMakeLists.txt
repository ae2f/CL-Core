cmake_minimum_required(VERSION 3.10)

project(CL-Core VERSION 4.15.21)
enable_testing()

set(OpenCL_FOUND OFF)

if(NOT TARGET ${PROJECT_NAME})
    include(cmake/CL-Core.cmake)
    ae2f_CoreLibFetch(ae2f Core Rel-v6.19.12)

    ae2fCL_CheckNeeded()

    ae2f_CoreLibTent(
        ${PROJECT_NAME} INTERFACE
        include ae2fCL
        "include/ae2fCL/Loc.h"
        "include/ae2fCL/Scenario.h"
    )

    target_link_libraries(${PROJECT_NAME} INTERFACE Core)

    ae2fCL_CoreAppendInclude(${PROJECT_SOURCE_DIR}/include)
    ae2f_CoreUtilityDocTent(${PROJECT_NAME} cmake ae2fCL Core)

    if(${ae2f_TEST} AND ${ae2fCL_needed})
        find_package(OpenCL REQUIRED) 
        ae2fCL_CoreTestTent(${PROJECT_NAME} test OpenCL::OpenCL)
    endif()
endif()
