#include <Servo.h>


struct Mov
{
    char key;     // key asociado al Led
    int time;        // numero de pin asociado al Led
};

Mov movimientos[] = {
                'W', 1000,                
                'A', 1300,
                'W', 1000,
                'X', 1000,};
int tamMov = sizeof(movimientos)/sizeof(Mov);
int fin;

char dato = ' ';
Servo servo_pin_8;
Servo servo_pin_9;
Servo servo_pin_7;

void setup()
{
  Serial.begin( 9600 );
  servo_pin_8.attach( 8 );
  servo_pin_9.attach( 9 );
  servo_pin_7.attach( 7 );
}  

int aux=0;
void loop()
{
    if ( Serial.available()  >  0  ){     
      dato = Serial.read();
      

      if ( dato == 'W' ){          
       front();
      }
      else if ( dato  == 'S'){
        back();
      }
      else if ( dato  == 'D'){
        right();
      }
      else if ( dato == 'A'){
        left();
      }
      else if ( dato == 'X'){
        stopA();
      }
      else if ( dato  == 'T'){      
        closeP();
        
      }
      else if ( dato  == 'R'){
        openP();
      } 
      else if(dato == 'M'){
        monitoreo();
      }
      
    }
      

    
}
void front(){
      servo_pin_8.attach( 8 );
      servo_pin_9.attach( 9 );
      //servo_pin_8.write( 112 );
      //servo_pin_9.write( 60 );
      servo_pin_8.write( 122 );
      servo_pin_9.write( 50 );

}

void stopA(){
    servo_pin_8.write( 90 );
    servo_pin_9.write( 90 );
    servo_pin_8.detach();
    servo_pin_9.detach();
}

void back(){
      servo_pin_8.attach( 8 );
      servo_pin_9.attach( 9 );
      //servo_pin_8.write( 60 );
      //servo_pin_9.write( 112 );
      servo_pin_8.write( 30 );
      servo_pin_9.write( 142 );

}
void right(){
        servo_pin_8.attach( 8 );
      servo_pin_9.attach( 9 );
      servo_pin_8.write( 112 );
      servo_pin_9.write( 112 );

}
void left(){
      servo_pin_8.attach( 8 );
      servo_pin_9.attach( 9 );
      servo_pin_8.write( 60 );
      servo_pin_9.write( 60 );

}
void closeP(){
  servo_pin_7.attach( 7 );
  servo_pin_7.write( 175 );
}    
void openP(){
  servo_pin_7.attach( 7 );
  servo_pin_7.write( 50 );
}
    
void monitoreo(){
    delay(1000);
    for(int i=0; i<tamMov; i++){
      fin = millis()+movimientos[i].time;
      if ( movimientos[i].key == 'W' ){          
       front();
      }
      else if ( movimientos[i].key  == 'S'){
        back();
      }
      else if ( movimientos[i].key  == 'D'){
        right();
      }
      else if ( movimientos[i].key == 'A'){
        left();
      }
      else if ( movimientos[i].key == 'X'){
        stopA();
      }
      else if ( movimientos[i].key  == 'T'){
        closeP();
      }
      else if ( movimientos[i].key  == 'R'){
        openP();
      }      
      while( millis()<fin ){                       
      }
      Serial.println( (String)movimientos[i].key+"_"+(String)movimientos[i].time );
    }
    Serial.println( "termino_T" );
}
