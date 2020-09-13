
//https://arduinogetstarted.com/tutorials/arduino-light-sensor
int limit = 2;
int PowerPin = 10;  // using digital pin as second 5v power


void setup() {
  // initialize serial communication at 9600 bits per second:
  Serial.begin(9600);
  digitalWrite(PowerPin, HIGH); 
}

void loop() {
  // reads the input on analog pin A0 (value between 0 and 1023)
  int lightSensor1 = analogRead(A0);
  int lightSensor2 = analogRead(A5);  // 3v

  Serial.print(lightSensor1);
  Serial.print(";");
  Serial.println(lightSensor2);

  delay(500);
}
