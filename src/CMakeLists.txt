add_library(AwesomeProject
    AwesomeProject/fibonacci.cpp
)

target_include_directories(AwesomeProject
    PUBLIC
        $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}>
        $<INSTALL_INTERFACE:${CMAKE_INSTALL_INCLUDEDIR}>
)

install(TARGETS AwesomeProject EXPORT ${PROJECT_NAME})
install(
    DIRECTORY
        AwesomeProject
    DESTINATION
        ${CMAKE_INSTALL_INCLUDEDIR}
    FILES_MATCHING PATTERN "*.h"
)

install(EXPORT ${PROJECT_NAME}
    FILE AwesomeProjectTargets.cmake
    NAMESPACE AwesomeProject::
    DESTINATION share/cmake/AwesomeProject
)
