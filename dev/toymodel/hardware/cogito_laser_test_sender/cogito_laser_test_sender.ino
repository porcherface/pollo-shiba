#include <Arduino.h>
String init_message = "$S01$pollo$INIT$0x0404";

String on_message = "$S01$pollo$E01_HI$0x0404";

int waitInit(int *_pins)
{
  return 0;
  /* pseudo code for waitInit
  /* 
  while (not serial read init message)
  {  
    ;
  }
  if (init ok)
    return 0; 
  return 1;    
  */
  


}
void setup() {
  // put your setup code here, to run once:
  pinMode(12, OUTPUT);
  digitalWrite(12, HIGH);
  Serial.begin(115200);
  int _pins[16];

  /* pollo ci dice cosa accendere */
  waitInit(_pins);
  
  delay(15000);
}

int terminate()
{
	/* qui invece di "12" ci sta una pinlist (ad esempio quella "_pins" che
	al momento è nello scope di init) */

	digitalWrite(12, LOW);

	/* qui ci vorrebbe una funzione di reset, 
	che torni al setup per preparare la prossima scena
}

int readTrigger()
{
	/* a function to read data from pollo and 
	return 0;

}


void loop() {
  // put your main code here, to run repeatedly:
  /* pseudo code for emitter */
  /* if readTrigger()
  		terminate()
}
