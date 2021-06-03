#include <Arduino.h>

int parseMessage(String data)
{
    
}


void init()
{
    while(1)
    {
        String data = Serial.readString();
        

        if (data.substring(0,9) == "#S01$init$")
        {
            result = parseMessage(data);
        }
    }
}

void exec()
{

  if(1)
  {
    finalize();    
  }

}


void finalize()
{
  init();
}

void setup()
{
    // one time initialize (all here)
    Serial.begin(115200);
    init();
}

void loop()
{
    // do nothing
}
