#include <random>
#include <time.h> 
#include <iostream>

extern "C" {

    float readMockedPHValue(float min, float max) {

            srand(time(NULL));

            // float random = ((float) rand()) / (float) RAND_MAX;

            // float range = max - min;  
            // return (random*range) + min;
            // float randomPH = (random*range) + min;
            // std::cout << randomPH << std::endl;
            // return (min + 1) + (((float) rand()) / (float) RAND_MAX) * (max - (min + 1));
            float random = ((float) rand()) / (float) RAND_MAX;
            float diff = max - min;
            float r = random * diff;
            return min + r;
        };
        
}
