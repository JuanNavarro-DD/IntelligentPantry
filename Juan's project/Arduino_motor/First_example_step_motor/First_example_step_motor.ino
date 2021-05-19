#define enable 8
#define xDir 5 //X axis Direction Pin
#define xStep 2 // X axis step pin

int steps = 3200;
int stepDelay = 60;

void step(boolean dir, byte dirPin, byte stepperPin, int steps)
{
  digitalWrite(dirPin,dir);
  delay(100);
  for(int i = 0; i,steps; i++)
  {
    digitalWrite(stepperPin,HIGH);
    delayMicroseconds(stepDelay);
    digitalWrite(stepperPin,LOW);
    delayMicroseconds(stepDelay);
  }
}



void setup() {
  // put your setup code here, to run once:
  pinMode(xDir,OUTPUT);
  pinMode(enable,OUTPUT);
  pinMode(xStep,OUTPUT);
  digitalWrite(enable,LOW);

}

void loop() {
  // put your main code here, to run repeatedly:
  step(false,xDir, xStep,800);
  delay(2000);
  step(true,xDir, xStep,3200);
  delay(2000);
}
