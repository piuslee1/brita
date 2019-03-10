/*
Measure the optical density of a liquid sample over 3 days in 30 minute intervals.
Writes the data onto an SD card for future use. Stops collecting once enough data is collected.
*/
#include <SD.h> //Load SD library
#include <SPI.h> //Load Serial library


float sensor, v; //create two float variables
int n = 144; // number of data points
int count = 0; 
int chipSelect = 4; //hook up chipSelect to pin 4 on board
long duration;
File mySensorData; //make a file to put the data in

void setup() {
    Serial.begin(9600); //bits of data per second, faster baud rate for live plotting
    pinMode(10,OUTPUT); //Reserve pin 10 as an output
    SD.begin(chipSelect); //Initialize SD card with chipSelect connected to pin 4
}

void loop(){
  mySensorData= SD.open("TurbData.txt", FILE_WRITE); //open new file to write to it
  if (mySensorData) { //if the data file opens correctly-->
  sensor = analogRead(A0); //read from sensor 
  delay(100); //delays x/1000 sec   
  v = sensor * 5 / 1023;
  Serial.println(v);   
  mySensorData.println(v); //Write v to SD file
  mySensorData.close(); //Close the file
  count = count + 1;
  if (count > 143){
    while (1){}
    }
}
}
    
    
