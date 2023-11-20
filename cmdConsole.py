
from ExpanderDriver import Expander 
import cmd

class my(cmd.Cmd):

    intro = "This is GPIO EXPANDER Controller made by Durden. 0.reset (recommend) 1.set (set device) 2. p (port mode)  3. Write or Read \n\nsample command\n\nreset\nset 0\np 5 1\nwrite 5 1\n\n-> Device is set to tca9535, P05 port is write mode, and 1 is wrote. Maybe LED is turned on. Try it! \n\n If u have any question about this program, please use help command or find Durden"
    
    prompt = '(GPIO) '
    file= None


    def do_set(self,arg):
        """set 0 -> setting 9535(under)     set 1 -> setting 6424(up)"""
        if int(arg) == 0:
            self.DevCmd= Expander(0x77)
            print("9535 is set")
        elif int(arg) == 1:
            self.DevCmd=  Expander(0x22)
            print("6424 is set")
        else:
            print("There is no device")



    def do_p(self,arg):
        """p portname WriteEnable   e.g) p 5 1  -> P05 Write mod"""
        setport=int(arg.split()[0])
        setmode=int(arg.split()[1])
        
        
        try:
            self.DevCmd.setmode(setport,setmode)
            print(f"{setport}th port is set. Write Enable is {setmode}")
        
        except:
            print("Error! Try again")
        
    def do_write(self,arg):
        """write portname data, data must be 0 or 1  e.g) write 23 1"""
        setport=int(arg.split()[0])
        setdata=int(arg.split()[1])

        self.DevCmd.write(setport,setdata)
        print("Done")
        
        
    def do_read(self,arg):
        """read portname  e.g) read 23 """
        print(self.DevCmd.read(int(arg)))
        
    def do_wstate(self,arg):
        """Write Register"""
        self.DevCmd.writestate()
    
    def do_rstate(self,arg):
        """Read Register"""
        self.DevCmd.readstate()

    def do_cstate(self,arg):
        """Configuration Register"""
        self.DevCmd.configstate()
        
        
    def do_clean(self,arg):
        """Clean output Register, you must set the port before running"""
        self.DevCmd.cleanOutReg()
        print("Clean done")
        
    def do_pstate(self,arg):
        """Current portstate. key is port, value is WriteEnable.  e.g) {"3":1} -> P03 is write mode"""
        self.DevCmd.currnetPortSet()
        
    def do_reset(self,arg):
        Expander(0x77).reset()
        Expander(0x22).reset()
       





    def do_quit(self, *arg):
        """quit """
        print("byebye")
        return True



my().cmdloop()    
######################################################################################################################################################