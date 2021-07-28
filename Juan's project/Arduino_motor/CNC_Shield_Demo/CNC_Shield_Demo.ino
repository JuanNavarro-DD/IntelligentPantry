
// CNC Shield Stepper  Control Demo
// Superb Tech
// www.youtube.com/superbtech

const int StepX = 2;
const int DirX = 5;
const int StepY = 3;
const int DirY = 6;
const int StepZ = 4;
const int DirZ = 7;
// const int StepA = 12;
// const int DirA = 13;



void setup() {
  pinMode(StepX,OUTPUT);
  pinMode(DirX,OUTPUT);
  pinMode(StepY,OUTPUT);
  pinMode(DirY,OUTPUT);
  pinMode(StepZ,OUTPUT);
  pinMode( DirZ,OUTPUT);
  // pinMode(StepA,OUTPUT);
  // pinMode( DirA,OUTPUT);

}

void loop() {
 digitalWrite(DirX, HIGH);// set direction, HIGH for clockwise, LOW for anticlockwise
 digitalWrite(DirY, HIGH);
 digitalWrite(DirZ, HIGH);
//  digitalWrite(DirA, HIGH);

//  for(int x = 0; x<200; x++) { // loop for 200 steps
//   digitalWrite(StepA,HIGH);
//   delayMicroseconds(5000);
//   digitalWrite(StepA,LOW);
//   delayMicroseconds(2000);
//  }
 delay(1000);
 for(int x = 0; x<200; x++) { // loop for 200 steps
  digitalWrite(StepX,HIGH);
  delayMicroseconds(5000);
  digitalWrite(StepX,LOW);
  delayMicroseconds(2000);
 }
 delay(1000);
 for(int x = 0; x<200; x++) {
  digitalWrite(StepY,HIGH);
  delayMicroseconds(5000);
  digitalWrite(StepY,LOW);
  delayMicroseconds(2000);
 }
 delay(1000);
 for(int x = 0; x<200; x++) {
  digitalWrite(StepZ,HIGH);
  delayMicroseconds(5000);
  digitalWrite(StepZ,LOW); 
  delayMicroseconds(2000);
 }
delay(1000); // delay for 1 second



}
