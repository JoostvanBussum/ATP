#include <iostream>

extern "C" {

    float adjustPHValue(float currentPH, float goalPH) {
            if(currentPH > goalPH){
                return -0.05;
            }

            return 0.05;
        };
        
}