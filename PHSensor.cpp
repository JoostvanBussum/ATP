#include <random>
#include <time.h> 
#include <iostream>

extern "C" {

    float readMockedPHValue(float min, float max) {

            srand(time(NULL));
            float random = ((float) rand()) / (float) RAND_MAX;
            float diff = max - min;
            float r = random * diff;
            return min + r;

        };
        
}
