#include "pch.h"

TEST(ADD, _1) {
    EXPECT_EQ(add(2, 3), 5);
}

TEST(ADD, _2) {
    EXPECT_EQ(add(-2, -3), -5);
}

TEST(ADD, _3) {
    EXPECT_EQ(add(2, -3), -1);
}

TEST(ADD, _4) {
    EXPECT_EQ(add(0, 5), 5);
}

TEST(Addition, _5) {
    EXPECT_EQ(add(1000000, 2000000), 3000000);
}
