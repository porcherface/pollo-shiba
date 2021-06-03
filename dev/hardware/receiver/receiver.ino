#include <Arduino.h>

int P1 = 30;
int P2 = 32;

int parseMessage(String data)
{
    int has_error = 0;
    String msg = "#S01$init$";
    if(digitalRead(P1))
      msg += "[OK]";
    else
    {
      msg += "[KO]";
      has_error = 1;
    }

    if(digitalRead(P2))
      msg += "[OK]";
    else
    {
      msg += "[KO]";
      has_error = 1;
    }
}

int triggered()
{
    if (!digitalRead(P1))
    {
      return 1;
    }
    if (!digitalRead(P2))
    {
      return 1;
    }
    return 0;
}






void initialize()
{
    while(1)
    {
        String data = Serial.readString();
        int result;

        if( data.substring(0,9)== ("#S01$init$"))
        {
            result = parseMessage(data);
            if (!result)
              exec();       
        }
    }
}

void exec()
{

  while(1)
  {
    if (triggered())
    {
      break;
    }
  }
  finalize();
}

void finalize()
{

  Serial.println("#S01$FINALIZED@");
  initialize();
}

void setup()
{
    // one time initialize (all here)
    pinMode(P1, INPUT);
    pinMode(P2, INPUT);
    
    Serial.begin(115200);
    initialize();
}

void loop()
{
    // do nothing
}
