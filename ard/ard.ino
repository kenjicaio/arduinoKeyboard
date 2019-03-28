unsigned long timer[] = {0, 0};
boolean pressed[] = {false, false};
boolean r = false;

void setup() {
  Serial.begin(9600);
  pinMode(7, INPUT_PULLUP);
  pinMode(8, INPUT_PULLUP);
  Serial.write('c');
}

void loop() {
  if (millis() - timer[0] > 10) {
    r = !digitalRead(7);
    if (r != pressed[0]) {
      pressed[0] = r;
      if (r) {
        Serial.write('a');
      } else {
        Serial.write('A');
      }
    }
    timer[0] = millis();
  }
  if (millis() - timer[1] > 10) {
    r = !digitalRead(8);
    if (r != pressed[1]) {
      pressed[1] = r;
      if (r) {
        Serial.write('b');
      } else {
        Serial.write('B');
      }
    }
    timer[1] = millis();
  }
}

