#include <Servo.h>
Servo myservo;
#include <SoftwareSerial.h>
SoftwareSerial ss(3,4);
#define echoPin 6 // attach pin D2 Arduino to pin Echo of HC-SR04
#define trigPin 7//attach pin D3 Arduino to pin Trig of HC-SR04
#define echoPin1 8 // attach pin D2 Arduino to pin Echo of HC-SR04
#define trigPin1 9//attach pin D3 Arduino to pin Trig of HC-SR04

// defines variables
long duration; // variable for the duration of sound wave travel
int distance; // variable for the distance measurement
long duration1; // variable for the duration of sound wave travel
int distance1; // variable for the distance measurement
int pos;
void SendMessage( String data)
{
ss.println("AT+CMGF=1");
delay(1000);
ss.println("AT+CMGS=\"+918978142641\"\r");
delay(1000);
ss.println(data);
delay(100);
ss.println((char)26);
delay(1000);
}
void setup() {
Serial.begin(9600);
myservo.attach(10);
ss.begin(9600);
pinMode(trigPin, OUTPUT); // Sets the trigPin as an OUTPUT
pinMode(echoPin, INPUT); // Sets the echoPin as an INPUT
pinMode(trigPin1, OUTPUT); // Sets the trigPin as an OUTPUT
pinMode(echoPin1, INPUT); // Sets the echoPin as an INPUT

}

void loop() {
digitalWrite(trigPin, LOW);
delayMicroseconds(2);
// Sets the trigPin HIGH (ACTIVE) for 10 microseconds
digitalWrite(trigPin, HIGH);
delayMicroseconds(10);
digitalWrite(trigPin, LOW);
// Reads the echoPin, returns the sound wave travel time in microseconds
duration = pulseIn(echoPin, HIGH);
// Calculating the distance
distance = duration * 0.034 / 2; // Speed of sound wave divided by 2 (go and back)
// Displays the distance on the Serial Monitor
Serial.print("Distance: ");
Serial.print(distance);
Serial.println(" cm");
delay(1000);
if(distance<10) {
Serial.println("human detect");
delay(1000);
myservo.write(90); // tell servo to go to position in variable 'pos'
delay(15); // waits 15ms for the servo to reach the positio
//digitalWrite(buzzer,HIGH);
//delay(1000);
}
else{
myservo.write(0); // tell servo to go to position in variable 'pos'
delay(15); // waits 15ms for the servo to reach the positio
//digitalWrite(buzzer,LOW);
//delay(1000);
}
digitalWrite(trigPin1, LOW);
delayMicroseconds(2);
// Sets the trigPin HIGH (ACTIVE) for 10 microseconds
digitalWrite(trigPin1, HIGH);
delayMicroseconds(10);
digitalWrite(trigPin1, LOW);
// Reads the echoPin, returns the sound wave travel time in microseconds
duration1 = pulseIn(echoPin1, HIGH);
// Calculating the distance
distance1 = duration1 * 0.034 / 2; // Speed of sound wave divided by 2 (go and back)
// Displays the distance on the Serial Monitor
Serial.print("Distance1: ");
Serial.print(distance1);
Serial.println(" cm");
delay(1000);
if(distance1<40) {
Serial.println("dustbin full");
delay(1000);
SendMessage("dustbin full");
delay(2000);
}
else{
Serial.println("no full");
delay(1000);
}

}
