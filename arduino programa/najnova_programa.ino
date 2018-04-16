#include <Servo.h>

Servo myservo1;   // create servo object to control a servo
Servo myservo3; 
Servo myservo5;
Servo myservo2;
Servo myservo4;
Servo myservo6;

int pos1 = 0;    // variable to store the servo position
int pos3 = 0;
int pos5 = 0;
int pos2 = 0;
int pos4 = 0;
int pos6 = 0;
int boja = 0;
int pozicija = 0;
int prvflag = 0;
int flagvnatresen = 0;
int usbRead = 0;

int bluePin = 8;    //IN1 on the ULN2003 Board, BLUE end of the Blue/Yellow motor coil
int pinkPin = 7;    //IN2 on the ULN2003 Board, PINK end of the Pink/Orange motor coil
int yellowPin = 4;  //IN3 on the ULN2003 Board, YELLOW end of the Blue/Yellow motor coil
int orangePin = 2;  //IN4 on the ULN2003 Board, ORANGE end of the Pink/Orange motor coil

//Keeps track of the current step.
//We'll use a zero based index. 
int currentStep = 0;
int allstep=0;
int flag=0;
void PositionArmToGrab(){
  for (pos4 = 0; pos4<=136; pos4 += 1) {
    myservo4.write(pos4);
    delay(15);
  }
}
void GrabTheCap(){
  for (pos6 = 0; pos6<=55; pos6 += 1) {
    myservo6.write(pos6);
    delay(15);
  }
}
void RaiseTheArm(){
  for(pos4 = 136; pos4>=0; pos4 -= 1){
    myservo4.write(pos4);
    delay(15);
  }
}
void Move45(){
  for(pos1 = 0; pos1<=45; pos1 += 1){
    myservo1.write(pos1);
    delay(15);
  }
}
void Move90(){
  for(pos1 = 0; pos1<=90; pos1 += 1){
    myservo1.write(pos1);
    delay(15);
  }
}
void Move135(){
  for(pos1 = 0; pos1<=135; pos1 += 1){
    myservo1.write(pos1);
    delay(15);
  }
}
void LowerTheArm(){
  for(pos4 = 0; pos4<=136; pos4 += 1){
    myservo4.write(pos4);
    delay(15);
  }
}
void ReleaseTheCap(){
  for(pos6 = 55; pos6>=0; pos6 -= 1){
    myservo6.write(pos6);
    delay(15);
  }
}
void InitialPosition(){
    pos1 = 0;
    pos3 = 46;
    pos5 = 26;
    pos2 = 80;
    pos4 = 0;    // do 136
    pos6 = 0;
    myservo1.write(pos1);
    myservo2.write(pos2);
    myservo3.write(pos3);
    myservo4.write(pos4);
    myservo5.write(pos5);
    myservo6.write(pos6);
    delay(15);
  }

void setup() {
  Serial.begin(9600);
  pinMode(bluePin, OUTPUT);
  pinMode(pinkPin, OUTPUT);
  pinMode(yellowPin, OUTPUT);
  pinMode(orangePin,OUTPUT);

  digitalWrite(bluePin, LOW);
  digitalWrite(pinkPin, LOW);
  digitalWrite(yellowPin, LOW);
  digitalWrite(orangePin, LOW);

  myservo1.attach(10);  
  myservo3.attach(11);
  myservo5.attach(9);
  myservo2.attach(6);
  myservo4.attach(5);
  myservo6.attach(3);
  pos1 = 0;
  pos3 = 46;
  pos5 = 26;
  pos2 = 80;
  pos4 = 0;    // do 136
  pos6 = 0;
  InitialPosition();
  delay(50);
}
void loop() {
  if(prvflag==1){
    delay(1500);
    flagvnatresen=0;
    while(Serial.available() and flagvnatresen==0){
      usbRead = Serial.read();
      boja=usbRead/1000;
      pozicija=usbRead%1000;
  if(pozicija>900){
  if (boja==111){  // za zholto = 45 stepeni
    PositionArmToGrab();
  delay(1000);
  GrabTheCap();
  delay(1000);
  RaiseTheArm();
  delay(15);
  Move45();
  delay(15);
  LowerTheArm();
  delay(15);
  ReleaseTheCap();
  delay(15);
  RaiseTheArm();
  delay(15);
  InitialPosition();
  delay(2000);
  flagvnatresen=1;
  }
  if (boja==101){  // za plavo = 90 stepeni
    PositionArmToGrab();
  delay(1000);
  GrabTheCap();
  delay(1000);
  RaiseTheArm();
  delay(15);
  Move90();
  delay(15);
  LowerTheArm();
  delay(15);
  ReleaseTheCap();
  delay(15);
  RaiseTheArm();
  delay(15);
  InitialPosition();
  delay(2000);
  flagvnatresen=1;
  }

if (boja==100){  // za zeleno = 135 stepeni
    PositionArmToGrab();
  delay(1000);
  GrabTheCap();
  delay(1000);
  RaiseTheArm();
  delay(15);
  Move135();
  delay(15);
  LowerTheArm();
  delay(15);
  ReleaseTheCap();
  delay(15);
  RaiseTheArm();
  delay(15);
  InitialPosition();
  delay(2000); 
  flagvnatresen=1;
  }
  }
}
prvflag=0;
}
// STEFAN DEL
  if(prvflag==0){
    switch(currentStep){
    case 0:
      digitalWrite(bluePin, HIGH);
      digitalWrite(pinkPin, LOW);
      digitalWrite(yellowPin, LOW);
      digitalWrite(orangePin, LOW);
      break;
    case 1:
      digitalWrite(bluePin, LOW);
      digitalWrite(pinkPin, HIGH);
      digitalWrite(yellowPin, LOW);
      digitalWrite(orangePin, LOW);
      break;
    case 2:
      digitalWrite(bluePin, LOW);
      digitalWrite(pinkPin, LOW);
      digitalWrite(yellowPin, HIGH);
      digitalWrite(orangePin, LOW);
      break;
    case 3:
      digitalWrite(bluePin, LOW);
      digitalWrite(pinkPin, LOW);
      digitalWrite(yellowPin, LOW);
      digitalWrite(orangePin, HIGH);
      break;
    }
    currentStep = (++currentStep < 4) ? currentStep : 0;
    allstep= allstep+1;
  
    if(allstep>515)
    {
    allstep=0;
    prvflag=1;
    }
    delay(2.5);
  }
  
}


