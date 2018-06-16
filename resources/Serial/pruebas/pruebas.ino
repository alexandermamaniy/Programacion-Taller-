#include <Servo.h>

char _ABVAR_1_dato = ' ' ;
Servo servo_pin_8;
Servo servo_pin_9;
Servo servo_pin_7;

void setup()
{
  //Serial1.begin( 9600 );
  Serial.begin( 9600 );
  servo_pin_8.attach( 8 );
  servo_pin_9.attach( 9 );
  servo_pin_7.attach( 7 );
}

void loop()
{
  if (( ( Serial.available() ) > ( 0 ) ))
  {
    _ABVAR_1_dato = Serial.read();
    Serial.println( _ABVAR_1_dato );
    if (( ( _ABVAR_1_dato ) == ('A') )){
      servo_pin_8.attach( 8 );
      servo_pin_9.attach( 9 );
      servo_pin_8.write( 60 );
      servo_pin_9.write( 60 );
      delay(3350);
      servo_pin_8.write( 90 );
      servo_pin_9.write( 90 );
      servo_pin_8.detach();
      servo_pin_9.detach();
      Serial.println( "termino todo de impromorjhghjghyg" ); 
    }
    
  
  if (( ( _ABVAR_1_dato ) == ('D') )){
      servo_pin_8.attach( 8 );
      servo_pin_9.attach( 9 );
      servo_pin_8.write( 111.8 );
      servo_pin_9.write( 111.8 );
      delay(3350);
      servo_pin_8.write( 90 );
      servo_pin_9.write( 90 );
      servo_pin_8.detach();
      servo_pin_9.detach();
      Serial.println( "termino todo de impromorhgfetrtov" );
    }
    
  }    
  
}


