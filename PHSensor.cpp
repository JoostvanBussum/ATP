#include <random>
#include <time.h> 
#include <iostream>
// #include 

extern "C" {

    float readMockedPHValue(float min, float max) {

            srand(time(NULL));
            float random = ((float) rand()) / (float) RAND_MAX;
            float diff = max - min;
            float r = random * diff;
            return min + r;

            // boost::mt19937 rng;
            // boost::uniform_real<float> u(min, max);
            // boost::variate_generator<boost::mt19937&, boost::uniform_real<float> > gen(rng, u);
            // return gen();
        };
        
}
