#include <Arduino.h>
#include <String>


int parseMessage(String data)
{
    
}

void init()
{
    while(1)
    {
        String data = Serial.readString();
        

        if data.find("#S01$init$")
        {
            result = parseMessage(data);
        }
    }
}

void exec()
{

}


void finalize()
{

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