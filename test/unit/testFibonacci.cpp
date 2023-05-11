#include <AwesomeProject/fibonacci.h>

#include <gtest/gtest.h>

TEST(FibonacciTest, Execute)
{
    ASSERT_EQ(AwesomeProject::fibonacci(0), 0);
    ASSERT_EQ(AwesomeProject::fibonacci(1), 1);
    ASSERT_EQ(AwesomeProject::fibonacci(12), 144);
    ASSERT_EQ(AwesomeProject::fibonacci(15), 610);
}
