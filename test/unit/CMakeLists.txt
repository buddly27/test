add_executable(testFibonacci testFibonacci.cpp)
target_link_libraries(testFibonacci
    PRIVATE
        AwesomeProject
        GTest::gtest
        GTest::gtest_main
)
gtest_discover_tests(testFibonacci)
