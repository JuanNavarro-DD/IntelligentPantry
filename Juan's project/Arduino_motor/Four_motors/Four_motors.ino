#define DIR_PIN 13
#define DIR_PIN 
#define STEP_PIN 12
#define ENABLE_PIN 4

void setup() {
  // put your setup code here, to run once:
  pinMode(DIR_PIN, OUTPUT);
  pinMode(STEP_PIN, OUTPUT);
  pinMode(ENABLE_PIN, OUTPUT);

}

void loop() {
  // put your main code here, to run repeatedly:
  digitalWrite(STEP_PIN,HIGH);
  digitalWrite(STEP_PIN, LOW);
  delay(1);

}
