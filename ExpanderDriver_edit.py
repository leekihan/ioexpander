import smbus
import time
import sys
import RPi.GPIO as GPIO
import cmd
#GPIO.setmode(GPIO.BCM)
#GPIO.setup(16, GPIO.OUT)
#GPIO.output(16,1)

REG_9539_Input_0 = 0x00 # Input Port 0
REG_9539_Input_1 = 0x01 # Input Port 1
REG_9539_Output_0 = 0x02 # Output Port 0
REG_9539_Output_1 = 0x03 # Output Port 1
REG_9539_Polarity_0 = 0x04 # Polarity Inversion Port 0
REG_9539_Polarity_1 = 0x05 # Polarity Inversion Port 1
REG_9539_Config_0 = 0x06 # Configuration Port 0
REG_9539_Config_1 = 0x07 # Configuration Port 1
REG_6424_Config_0= 0x0c
REG_6424_Config_0_auto= 0x8c
REG_6424_Config_1= 0x0d
REG_6424_Config_1_auto= 0x8d
REG_6424_Config_2= 0x0e
REG_6424_Config_2_auto= 0x8e
REG_6424_Output_0= 0x04
REG_6424_Output_0_auto= 0x84
REG_6424_Output_1= 0x05
REG_6424_Output_1_auto= 0x85
REG_6424_Output_2= 0x06
REG_6424_Output_2_auto= 0x86
REG_6424_Input_0= 0x00
REG_6424_Input_0_auto= 0x80
REG_6424_Input_1= 0x01
REG_6424_Input_1_auto= 0x81
REG_6424_Input_2= 0x02
REG_6424_Input_2_auto= 0x82
REG_6424_polar_0= 0x08
REG_6424_polar_0_auto= 0x88
REG_6424_polar_1= 0x09
REG_6424_polar_1_auto= 0x89
REG_6424_polar_2= 0x0a
REG_6424_polar_2_auto= 0x8a
WRITE=1
READ=0

RegDict={REG_9539_Config_0:[REG_9539_Input_0 ,REG_9539_Output_0 ,REG_9539_Polarity_0],
         REG_9539_Config_1:[REG_9539_Input_1,REG_9539_Output_1 ,REG_9539_Polarity_1],
         REG_6424_Config_0:[REG_6424_Input_0,REG_6424_Output_0 ,REG_6424_polar_0],
         REG_6424_Config_0_auto :[REG_6424_Input_0_auto,REG_6424_Output_0_auto ,REG_6424_polar_0_auto],
         REG_6424_Config_1 : [REG_6424_Input_1,REG_6424_Output_1 ,REG_6424_polar_1],
         REG_6424_Config_1_auto :[REG_6424_Input_1_auto,REG_6424_Output_1_auto ,REG_6424_polar_1_auto],
         REG_6424_Config_2 : [REG_6424_Input_2,REG_6424_Output_2 ,REG_6424_polar_2],
         REG_6424_Config_2_auto :[REG_6424_Input_2_auto,REG_6424_Output_2_auto,REG_6424_polar_2_auto]
        }

bus = smbus.SMBus(1) # This is the I2C Bus

class Expander:
    REG_9539_Input_0 = 0x00 # Input Port 0
    REG_9539_Input_1 = 0x01 # Input Port 1
    REG_9539_Output_0 = 0x02 # Output Port 0
    REG_9539_Output_1 = 0x03 # Output Port 1
    REG_9539_Polarity_0 = 0x04 # Polarity Inversion Port 0
    REG_9539_Polarity_1 = 0x05 # Polarity Inversion Port 1
    REG_9539_Config_0 = 0x06 # Configuration Port 0
    REG_9539_Config_1 = 0x07 # Configuration Port 1
    REG_6424_Config_0= 0x0c
    REG_6424_Config_0_auto= 0x8c
    REG_6424_Config_1= 0x0d
    REG_6424_Config_1_auto= 0x8d
    REG_6424_Config_2= 0x0e
    REG_6424_Config_2_auto= 0x8e
    REG_6424_Output_0= 0x04
    REG_6424_Output_0_auto= 0x84
    REG_6424_Output_1= 0x05
    REG_6424_Output_1_auto= 0x85
    REG_6424_Output_2= 0x06
    REG_6424_Output_2_auto= 0x86
    REG_6424_Input_0= 0x00
    REG_6424_Input_0_auto= 0x80
    REG_6424_Input_1= 0x01
    REG_6424_Input_1_auto= 0x81
    REG_6424_Input_2= 0x02
    REG_6424_Input_2_auto= 0x82
    REG_6424_polar_0= 0x08
    REG_6424_polar_0_auto= 0x88
    REG_6424_polar_1= 0x09
    REG_6424_polar_1_auto= 0x89
    REG_6424_polar_2= 0x0a
    REG_6424_polar_2_auto= 0x8a
    WRITE=1
    READ=0
    

    RegDict={REG_9539_Config_0:[REG_9539_Input_0 ,REG_9539_Output_0 ,REG_9539_Polarity_0],
         REG_9539_Config_1:[REG_9539_Input_1,REG_9539_Output_1 ,REG_9539_Polarity_1],
         REG_6424_Config_0:[REG_6424_Input_0,REG_6424_Output_0 ,REG_6424_polar_0],
         REG_6424_Config_0_auto :[REG_6424_Input_0_auto,REG_6424_Output_0_auto ,REG_6424_polar_0_auto],
         REG_6424_Config_1 : [REG_6424_Input_1,REG_6424_Output_1 ,REG_6424_polar_1],
         REG_6424_Config_1_auto :[REG_6424_Input_1_auto,REG_6424_Output_1_auto ,REG_6424_polar_1_auto],
         REG_6424_Config_2 : [REG_6424_Input_2,REG_6424_Output_2 ,REG_6424_polar_2],
         REG_6424_Config_2_auto :[REG_6424_Input_2_auto,REG_6424_Output_2_auto,REG_6424_polar_2_auto]
        }
    def __init__(self,device):
        self.device=device
        self.mode=0x06
        self.ConfigReg=0xff
        self.setdict={}
        self.writeReg0=0x00
        self.writeReg1=0x00
        self.writeReg2=0x00
    
    def Sortmode(self,port):
        forbid = [8, 18, 28, 9, 19, 29]
        if self.device == 0x77:
            if port in forbid:
                print("error! ther is no such port. Please Reset your board")
            elif port >= 10:
                configmode = REG_9539_Config_1
                portnew=port-10
            else:
                configmode = REG_9539_Config_0
                portnew = port
                
        elif self.device == 0x22:
            if port in forbid:
                print("error! ther is no such port. Please Reset your board")
            elif port >= 20:
                configmode = REG_6424_Config_2
                portnew = port-20
            elif (20>port>=10):
                configmode = REG_6424_Config_1
                portnew = port-10
            else:
                configmode = REG_6424_Config_0
                portnew = port
        else:
            print("Error, please define device")
        returntuple = (configmode,portnew)
        return returntuple
        

    def setmode(self,port,mode):
        modetuple=self.Sortmode(port)
        if mode == 1:
            ConfigReg = self.ConfigReg ^ 2**(modetuple[1])
            self.ConfigReg = ConfigReg
            bus.write_byte_data(self.device,modetuple[0],self.ConfigReg)
        else:
            ConfigReg = self.ConfigReg | 2**(modetuple[1])
            self.ConfigReg = ConfigReg
            bus.write_byte_data(self.device,modetuple[0],self.ConfigReg)
                
        self.mode=modetuple[0]
        self.port = modetuple[1]
        self.setdict[str(port)]=mode
   
  
    def write(self,wport,data):
        modetuple= self.Sortmode(wport)
        if data == 1:
            if wport >= 20:
                self.writeReg2=self.writeReg2  | (data*2) ** modetuple[1]
                writeRg= self.writeReg2
            elif 20> wport >=10:
                self.writeReg1=self.writeReg1  | (data*2) ** modetuple[1]
                writeRg= self.writeReg1
            else:
                self.writeReg0=self.writeReg0  | (data*2) ** modetuple[1]
                writeRg= self.writeReg0
        elif data == 0:
            mask= (2) ** modetuple[1]
            newmask= mask ^ 0xff
            if wport >= 20:
                self.writeReg2= self.writeReg2 & newmask
                writeRg= self.writeReg2
            elif 20> wport >=10:
                self.writeReg1= self.writeReg1 & newmask
                writeRg= self.writeReg1
            else:
                self.writeReg0= self.writeReg0 & newmask
                writeRg= self.writeReg0
            
        
        try:
            if self.setdict[str(wport)]==1:
                bus.write_byte_data(self.device,RegDict[modetuple[0]][1],writeRg)
        
            else:
                print("This port is not write mode!")
        except:
            print("This port is not write mode!")

       
        
    
    def read(self,port):
        modetuple= self.Sortmode(port)
        try:
            if self.setdict[str(port)]==0:
                ReadReturn = bus.read_byte_data(self.device,RegDict[self.mode][0])
                ReadReturn = (ReadReturn>>modetuple[1]) & 1

            else:
                print("This port is not read mode!")
                ReadReturn = None
        except:
            print("This port is not read mode!")
            ReadReturn = None
        
        
        return ReadReturn
    
    def writestate(self):
        print (f"Current Write Register: {bin(bus.read_byte_data(self.device,RegDict[self.mode][1]))}")
        Wrglist=[REG_9539_Output_0 ,REG_9539_Output_1 ,REG_6424_Output_0 ,REG_6424_Output_0_auto, REG_6424_Output_1 ,REG_6424_Output_1_auto, REG_6424_Output_2,REG_6424_Output_2_auto]
        Wreg = bus.read_byte_data(self.device,RegDict[self.mode][1])
        compare = 0
        for i in range(0,8):
            compare = Wreg & 1
            print(f" {i}th port is {compare}")
            Wreg = Wreg >>1
        if self.device == 0x77:
            for i in range(0,2):
                print(f"{i}th register is {hex(bus.read_byte_data(self.device,Wrglist[i]))}")
        elif self.device == 0x22:
            for i in range(2,8):
                print(f"{i-2}th register is {hex(bus.read_byte_data(self.device,Wrglist[i]))}")
        #print(hex(self.writeReg0),hex(self.writeReg1),hex(self.writeReg2))
    
    def readstate(self):
        print(f"Current Read Register: {hex(bus.read_byte_data(self.device,RegDict[self.mode][0]))}")
        Rglist=[REG_9539_Input_0 ,REG_9539_Input_1 ,REG_6424_Input_0 ,REG_6424_Input_0_auto, REG_6424_Input_1 ,REG_6424_Input_1_auto, REG_6424_Input_2,REG_6424_Input_2_auto]
        if self.device == 0x77:
            for i in range(0,2):
                print(f"{i}th register is {hex(bus.read_byte_data(self.device,Rglist[i]))}")
        elif self.device == 0x22:
            for i in range(2,8):
                print(f"{i-2}th register is {hex(bus.read_byte_data(self.device,Rglist[i]))}")
        
    def configstate(self):
        print(f"Current config Register: {hex(bus.read_byte_data(self.device,self.mode))}")
        Configlist=[REG_9539_Config_0,REG_9539_Config_1,REG_6424_Config_0
         ,REG_6424_Config_0_auto 
         ,REG_6424_Config_1
         ,REG_6424_Config_1_auto 
         ,REG_6424_Config_2
         ,REG_6424_Config_2_auto ]
        if self.device == 0x77:
            for i in range(0,2):
                print(f"{i}th register is {hex(bus.read_byte_data(self.device,Configlist[i]))}")
        elif self.device == 0x22:
            for i in range(2,8):
                print(f"{i-2}th register is {hex(bus.read_byte_data(self.device,Configlist[i]))}")
                
    def currnetPortSet(self):
        print(self.setdict)
        
    def cleanOutReg(self):
        Clrlist=[REG_9539_Output_0 ,REG_9539_Output_1 ,REG_6424_Output_0 ,REG_6424_Output_0_auto, REG_6424_Output_1 ,REG_6424_Output_1_auto, REG_6424_Output_2,REG_6424_Output_2_auto]
        if self.device == 0x77:
            for i in range(0,2):
                bus.write_byte_data(self.device,Clrlist[i],0x00)
        elif self.device == 0x22:
            for i in range(2,8):
                bus.write_byte_data(self.device,Clrlist[i],0x00)
                
    def reset(self):
        ClrConfiglist=[REG_9539_Config_0,REG_9539_Config_1,REG_6424_Config_0
         ,REG_6424_Config_0_auto 
         ,REG_6424_Config_1
         ,REG_6424_Config_1_auto 
         ,REG_6424_Config_2
         ,REG_6424_Config_2_auto ]
        self.cleanOutReg()
        if self.device == 0x77:
            for i in range(0,2):
                bus.write_byte_data(self.device,ClrConfiglist[i],0xff)
        elif self.device == 0x22:
            for i in range(2,8):
                bus.write_byte_data(self.device,ClrConfiglist[i],0xff)
        print("Configuration Reg and output Reg reset done")
        
