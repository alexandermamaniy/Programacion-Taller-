


#include <SoftwareSerial.h>
SoftwareSerial Serial1(3,2);

char _ABVAR_1_dato = ' ';

void setup()
{
  Serial1.begin( 9600 );
}

void loop()
{

  if (( ( Serial1.available() ) > ( 0 ) ))
  {
      Serial1.println("yoo");
    //_ABVAR_1_dato = Serial1.read();
    //Serial1.println( _ABVAR_1_dato );
  }
}

