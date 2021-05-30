#include <Arduino.h>
#include <U8g2lib.h>

#ifdef U8X8_HAVE_HW_SPI
#include <SPI.h>
#endif
#ifdef U8X8_HAVE_HW_I2C
#include <Wire.h>
#endif

/*
  U8g2lib Example Overview:
    Frame Buffer Examples: clearBuffer/sendBuffer. Fast, but may not work with all Arduino boards because of RAM consumption
    Page Buffer Examples: firstPage/nextPage. Less RAM usage, should work with all Arduino boards.
    U8x8 Text Only Example: No RAM usage, direct communication with display controller. No graphics, 8x8 Text only.
*/

bool triggered = false;
int logo_skull = 78;
int baseline_light = 0;
char baseline[10];
int soglia;


U8G2_SSD1306_128X64_NONAME_F_HW_I2C u8g2(U8G2_R0, /* reset=*/ U8X8_PIN_NONE);

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

void setup(void) {
  
  int _pins[16]; /* ad esempio si possono salvare qui i pin da accendere */

  u8g2.begin();
  Serial.begin(115200);
  
  u8g2.setFont(u8g2_font_8x13B_mr );
  delay(10);

  /* prima di iniziare la campionatura aspettiamo un messaggio di pollo */

  if !waitInit(_pins);
  /* pollo ci dice quali receiver vogliamo accendere


  /* una routine di calibratura */
  while (analogRead(15) == 0) {
    u8g2.clearBuffer(); // pulisci l'attuale buffer grafico
    u8g2.drawStr(0,15,"Attesa luce...");
    u8g2.sendBuffer(); // carica la nuova immagine nel buffer grafico
    delay(100);
  }

  u8g2.clearBuffer();
  u8g2.drawStr(0,15,"Calibratura...");
  u8g2.sendBuffer();
  
  for (int i = 0; i < 100; i ++) {
    baseline_light +=  analogRead(15);
  }
  
  baseline_light = baseline_light / 100;
  itoa(baseline_light, baseline, 10);

  soglia = baseline_light * 0.95;

  u8g2.clearBuffer();
  u8g2.drawStr(0,10,"* RUNNING *");
  u8g2.drawStr(0,20,"Soglia: ");
  u8g2.drawStr(50,20,baseline);
  u8g2.sendBuffer();


  /* se è andato tutto bene possiamo dire a pollo OK,
     se non è andato tutto bene diciamo a pollo KO */
}


/* messages to polloshiba on trigger*/
String trigger_msg = "#S01$R01_TRIG@";
String ok_msg = " #S01$INIT_OK@;
String ko_msg = " #S01$INIT_KO@;


int sendTrigger(){
  
  Serial.println(trigger_msg);
  return 0;
}

int terminate()
{
  /* qui invece di "12" ci sta una pinlist (ad esempio quella "_pins" che
  al momento è nello scope di init) */

  digitalWrite(12, LOW);

  /* qui ci vorrebbe una funzione di reset, 
  che torni al setup per preparare la prossima scena
}



void loop(void) {
  if (!triggered) {
    /*u8g2.clearBuffer(); // clear the internal memory
    u8g2.drawStr(0,15,"Lettura V:");
    char voltaggio[10];
    itoa(analogRead(15), voltaggio, 10);
    u8g2.drawStr(0, 30, voltaggio);
    u8g2.drawStr(0, 45, "Baseline luce:");
    u8g2.drawStr(0, 60, baseline);
    u8g2.sendBuffer(); // transfer internal memory to the display
*/
    if (analogRead(15) < soglia) {
      triggered = true;
      sendTrigger();
      terminate();
    }
    //delay(1);
  }
  else {

    /* qui possiamo mettere le operazioni post trigger */

    u8g2.clearBuffer();
    u8g2.setFont(u8g2_font_cursor_tf );
    u8g2.drawGlyph(10,15,0x78);
    u8g2.drawGlyph(100,40,0x78);
    u8g2.drawGlyph(64,38,0x78);
    u8g2.drawGlyph(80,8,0x78);

    u8g2.setFont(u8g2_font_8x13B_mr );
    u8g2.drawStr(0,40,"TRIGGERED!");
    
    u8g2.sendBuffer();
    delay(3000);

    u8g2.clearBuffer();
    u8g2.drawStr(0,20,"Running");
    u8g2.sendBuffer();
    triggered = false;
  }
}
