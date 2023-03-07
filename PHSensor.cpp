#include <random>
#include <time.h> 
#include <iostream>

class SensorInterface {
    private:
        int min, max;

    public:
        virtual float readValue() = 0;
};

class PHSensor: public SensorInterface {
    private:
        int min = 7;
        int max = 9;

    public:

        float readValue() {
            std::random_device rd;
            std::mt19937 gen(rd());
            std::uniform_real_distribution<> dist(PHSensor::min, PHSensor::max);
            return dist(gen);
        }
};

int main() {
    PHSensor sensor;

    std::cout << sensor.readValue();

    return 0;
}