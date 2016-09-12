#if defined(ARDUINO) 
SYSTEM_MODE(SEMI_AUTOMATIC); 
#endif

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  int pin=D0;
  int pin1=D1;
  int pin2=D2;
  int pin3=D3;
  pinMode(D0, INPUT_PULLUP);
  pinMode(D1, INPUT_PULLUP);
  pinMode(D2, INPUT_PULLUP);
  pinMode(D3, INPUT_PULLUP);
}

void loop() {
  // put your main code here, to run repeatedly:
  if (digitalRead(D0)==LOW) {
    Serial.println("R");
  }
  // green, middle
  if (digitalRead(D1)==LOW) {
    Serial.println("G");      
    
  }
  // blue, right
  if (digitalRead(D2)==LOW) {
    Serial.println("B");      
  }
  // undo only clears the array, cannot delete a letter that has already been entered
  if (digitalRead(D3)==LOW) {
    Serial.println("U");
  }   
  delay(300);


//    
//  int i = 0;
//
//  while(i < 3) {
//    // red, left
//    if (digitalRead(D0)==LOW) {
////      Serial.print(i);
//      Serial.println("R");
////      key_code[i] = 0;
//      i++;
//    }
//    // green, middle
//    if (digitalRead(D1)==LOW) {
////      Serial.print(i);
//      Serial.println("G");
////      key_code[i] = 1;
//      
//      i++;
//    }
//    // blue, right
//    if (digitalRead(D2)==LOW) {
////      Serial.print(i);
//      Serial.println("B");
////      key_code[i] = 2;  
//      
//      i++;    
//    }
//    // undo only clears the array, cannot delete a letter that has already been entered
//    if (digitalRead(D3)==LOW) {
////      Serial.print(i);  
//      Serial.println("UNDO");
//      i = -1; 
//  
//      i++;
//    }   
//    delay(300);
//  }
//  Serial.println("hi");
//  delay(300);


}



