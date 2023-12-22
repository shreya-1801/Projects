#include <Servo.h>
Servo s1;
 
const int redPin = 7;       // Red LED
const int yellowPin = 4;    // Yellow LED
const int greenPin = 2;     // Green LED
const int buzzerPin = 13;    // Buzzer
const int carSensorPin = 8; // IR sensor
const int gatePin = 12;  // Gate motor control pin
 
// Traffic light timings
const int greenDuration = 5000;
const int yellowDuration = 2000;
const int redDuration = 5000;
 
// Constants for traffic light colors
const int RED = 0;
const int YELLOW = 1;
const int GREEN = 2;
 
 
void setup() {
 pinMode(redPin, OUTPUT);
 pinMode(yellowPin, OUTPUT);
 pinMode(greenPin, OUTPUT);
 pinMode(buzzerPin, OUTPUT);
 s1.attach(gatePin);
 pinMode(carSensorPin, INPUT);
 
 // Initially, set the traffic light to red
 setTrafficLight(RED);
 
 // Initialize gate as open
 openGate();
}
 
void loop() {
 // Read the car sensor value
 int carValue = digitalRead(carSensorPin);
 openGate();
 
 if (carValue == LOW) {
   // Car detected
   closeGate();
   setTrafficLight(RED);
   soundBuzzer();
 } else {
   // Car not detected
   setTrafficLight(GREEN);
   delay(greenDuration);
   setTrafficLight(YELLOW);
   delay(yellowDuration);
   setTrafficLight(RED);
   delay(redDuration);
 }
}
 
void setTrafficLight(int color) {
 digitalWrite(redPin, color == RED ? HIGH : LOW);
 digitalWrite(yellowPin, color == YELLOW ? HIGH : LOW);
 digitalWrite(greenPin, color == GREEN ? HIGH : LOW);
}
 
void soundBuzzer() {
 digitalWrite(buzzerPin, HIGH);
 delay(1000);
 digitalWrite(buzzerPin, LOW);
}
 
void openGate() {
 s1.write(180);
}
 
void closeGate() {
 s1.write(90); }