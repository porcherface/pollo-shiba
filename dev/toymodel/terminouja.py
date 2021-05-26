#terminouja.py
from appJar import gui
import time
import datetime 
import serial
import threading

# Example of a semi-structured application
from ouija_coordinates import ouija_table_data_dict as data
from ouija_coordinates import wordToGCode,GCodeHome,GCodeStart
 
SHOW_TABLE_SIM = True
zerotime = time.time()

def thisTime():
    return "["+str( time.time() - zerotime)+"] "

class Terminouja():

    # Build the GUI
    def Prepare(self, app):

        now = datetime.datetime.now().strftime('%Y-%m-%d-T%H_%M_%S')
        self.logname = "log_"+now+'.txt'
        self.log = open("LOG/"+str(self.logname), "w")


        print("this session will be recorded to "+self.logname)

        self.log.write("*************************************************\n")
        self.log.write(thisTime()+"Log for session "+self.logname+"\n")
        self.log.write("*************************************************\n\n\n")



        # Form GUI
        app.setTitle("Login Form")
        app.setFont(16)
        app.setStopFunction(self.BeforeExit)
        app.addGrip(0,1)

        # Add labels & entries
        # in the correct row & column


        XSIZE = 9
        XTERMSIZE = 8
        YTERMSIZE = 9

        app.addLabel("userLab", "+ + + + T E R M I N O U I J A + + + +", row=1, column= 1, rowspan = 1,  colspan = XSIZE-2) #"row= column=2 colspan=1 rowspan=2"
        

        app.addEntry("msg",row=2, column=1,colspan=XTERMSIZE-1)
        app.addButton( "Senda", self.Submit, row=2,column=XTERMSIZE)
        app.addTextArea("t1", row=3, column=1, rowspan = YTERMSIZE, colspan=XTERMSIZE) 
        app.addLabel( "coml",   "port: (COM)",       row=1 , column=XTERMSIZE+1)        
        app.addNumericEntry("comport",            row=1 , column=XTERMSIZE+2)
        app.addEntry(   "raw Gcode Sender",       row=2 , column=XTERMSIZE+2)
        app.addLabel( "STATE",   "state: INIT",       row=2 , column=XTERMSIZE+1)
        app.addLabel( "minl",   "min Speed:",         row=3 , column=XTERMSIZE+1)
        app.addLabel( "maxl",   "max Speed",          row=4 , column=XTERMSIZE+1)
        app.addNumericEntry("min",            row=3 , column=XTERMSIZE+2)
        app.addNumericEntry("max",            row=4 , column=XTERMSIZE+2)

        app.setEntry("min", 100000)
        app.setEntry("max", 100000)

        app.addButton( "Connect",   self.Connect, row=5 , column=XTERMSIZE+1)
        app.addButton( "Send M503", self.M503,    row=5 , column=XTERMSIZE+2)
        app.addButton( "Go Home!" , self.Home,    row=6 , column=XTERMSIZE+1)
        app.addButton( "Go Start",  self.Go,      row=6 , column=XTERMSIZE+2)
        app.addButton( "STOP!",  self.Stop,       row=7 , column=XTERMSIZE+1)
        #app.addButton( "EMERGENZA",  self.Set,    row=7 , column=XTERMSIZE+2)
        app.addButton( "Check pos",  self.Check,    row=8 , column=XTERMSIZE+1)

        app.hideButton("Send M503") 
        app.hideButton("Go Home!")
        app.hideButton("Go Start")
        app.hideButton("STOP!")
        #app.hideButton("EMERGENZA")
        app.hideButton("Check pos")

        app.setEntry("comport", "10") 
        return app
        
    # Build and Start your application
    def Start(self):
        # Creates a UI
        app = gui()

        # Run the prebuild method that adds items to the UI
        app = self.Prepare(app)

        self.ser = serial.Serial()
        self.ser.port = "COM10"
        self.ser.baudrate = 115200 

        self.state = "INIT"
        self.ready = True
        # Make the app class-accesible
        self.app = app

        self.thread = threading.Thread(target = self.readSerial)
        self.thread.start()

        self.lastposition = 'XN YN'
        self.lastmsgreceived ='XN YN'
        # Start appJar
        app.go()

    def readSerial(self):
        while True:
            
            try:
                data_str = self.ser.read(self.ser.inWaiting()).decode('ascii') #read the bytes and convert from binary array to ASCII
                if data_str != "" and data_str != " ":
                    print("[?] data_str: "+data_str)
                    self.Submit("Received something!","S",False)
                    self.Submit(data_str,"O",False)
                    self.ready = True
                    
                    if data_str[0:2] != "ok":
                        self.lastmsgreceived = data_str
            except:
                pass
            #time.sleep(0.1)
            #print("1 second passed")
             
    # Callback, executes before quitting your app
    def BeforeExit(self):
        #return self.app.yesNoBox("Confirm Exit", "Are you sure you want to exit the application?")
        self.log.write(thisTime()+"INTO EXIT FUNCTION - LOG WILL CLOSE")
        self.log.close()
        
        try:
            self.ser.close()
        except: 
            pass
        
        print("tryin a stop")
        return True

    # Define method that is executed when the user clicks on the submit buttons
    # of the form
    
    def Set(self):
        
        self.log.write(thisTime()+"*** into Set routine ***"+"\n")

        msg = "G92 X100 Y127" 
        if self.ser.isOpen():
            self.ser.write( bytes(msg+'\n','ascii') )
            self.Submit("G92 X100 Y127","M", False)
        else:
            self.Submit("G92 CMD: (failed, no connection)","M",False)

    def Connect(self):
        
        self.log.write(thisTime()+"*** into Connect routine ***"+"\n")

        comport = str(int(self.app.getEntry("comport")))
        self.Submit('Opening Serial Port ' + comport,"S")
        self.ser.port = "COM"+comport
        self.state = "ONLINE"
        try:    
            self.ser.open()
            #app.setEntry("state", 3000)

        except serial.SerialException:
            self.state = "DC" 
            pass



        if self.ser.isOpen():
            self.Submit("Connection UP!","S")
            self.app.showButton("Send M503")     
            self.app.showButton("Go Start")
            self.app.showButton("Go Home!")
            self.app.showButton("STOP!")
            self.app.showButton("Check pos")

            msg = "G90" 
            
            self.ser.write( bytes(msg+'\n','ascii') )
            self.Submit("Sending init commands.","S", False)
        else: 
            self.Submit( "No Connection...","S",False)
        pass
    
    def Go(self):

        self.log.write(thisTime()+"*** into Go routine ***"+"\n")
        msg = GCodeStart() 
        if self.ser.isOpen():
            self.ser.write( bytes(msg+'\n','ascii') )
            self.Submit("Start CMD: "+msg,"M",False)
            self.lastposition = "X100 Y127"
        
        else:
            self.Submit("Start CMD: "+msg+" (failed, no connection)","M",False)

    def Stop(self):
        self.log.write(thisTime()+"*** into Stop routine ***"+"\n")

        print("[d] Pressed a stop")        
        self.state = "STOP"   
        #self.app.showButton("EMERGENZA")
    def Check(self):
        self.log.write(thisTime()+"*** into Check routine ***"+"\n")
        
    
        msg = "M114" 
        if self.ser.isOpen():
            self.ser.write( bytes(msg+'\n','ascii') )
            self.Submit("M114","M", False)
        else:
            self.Submit("M114 (failed, no connection)","M",False)

        self.parsedmsglist = self.lastmsgreceived.strip(":").split(" ")[0:2]
        self.parsedmsg =  self.parsedmsglist[0]+" "+self.parsedmsglist[1] 
        self.log.write(thisTime()+"Read from ouija:  "+str(self.parsedmsg))
        self.log.write(thisTime()+"Read from computer: "+str(self.lastposition))
        self.Submit("Read from computer: "+str(self.lastposition),"M",False)
        self.Submit("Read from ouija: "+str(self.parsedmsg),"M",False)


    def M503 (self):
        self.log.write(thisTime()+"*** into M503 routine ***"+"\n")

        msg = "M503" 
        if self.ser.isOpen():
            self.ser.write( bytes(msg+'\n','ascii') )
            self.Submit("M503 CMD.","M", False)
        else:
            self.Submit("M503 CMD: (failed, no connection)","M",False)

    def Home(self):
        self.log.write(thisTime()+"*** into Home routine ***"+"\n")
        
        msglist = GCodeHome()
        for msg in msglist:
            if self.ser.isOpen():
                self.ser.write( bytes(msg+'\n','ascii') )
                self.Submit("Start CMD: "+msg,"M",False)
            else:
                self.Submit("Start CMD: "+msg+" (failed, no connection)","M",False)
        
        self.lastposition = "X0 Y0"        

    def Submit(self, msg = "",sender="M", sendserial = True):
        self.log.write(thisTime()+"*** into Submit routine ***"+"\n")
        
        self.log.write("msg: "+str(msg)+"\n")
        self.log.write("sender: "+str(sender)+"\n")
        self.log.write("send flag: "+str(sendserial)+"\n")
        
        self.state = "CMD"
        
        if sender == "M" and msg == "Senda":
            msg = self.app.getEntry("msg")

        if msg == ' ' or msg == "":
            print("[?] found a return condtion in Submit, closing")
            self.log.write(thisTime()+"found a return condtion in Submit, closing"+"\n")
            return
      
        if sender == "M":
            pre = "Master > "

        else:
            pre = "?????: "

        if sender == "S":
            pre = " - Serial: "
        
        if sender == "O":
            pre = "OUIJA >"
            self.ready = True

        print('[*] msg to browser:'+pre+msg)    
        self.log.write(thisTime()+'msg to browser:'+pre+msg+"\n")

        successflag = True
        if sendserial is True and sender == "M":
            print('[*] sending msg to serial...') 

            speedlist = [self.app.getEntry("min"),self.app.getEntry("max")]
            msglist = wordToGCode(msg,speedlist)
            print("msglist:")
            print(msglist)

            try:
                for item in msglist:
                    
                    while self.ready is False:
                        pass    

                    if self.ready is True:
                        print("[*] current msg: "+item)
                        self.ser.write( bytes(item+'\n', 'ascii') )

                    if self.state == "STOP":
                        self.state = "READY"
                        break    
                
                print("[*] ok")
                self.log.write("[*] ok\n")
            except:
                print("[!] failed!")
                self.log.write("[!] failed!\n")
                successflag = False
            
            try: 
                self.lastposition = msglist[-2][3:-8]       
                print("last saved position is: "+self.lastposition)
            except:
                print("couldnt get last position")    
        

        print("task ended")
        self.log.write(thisTime()+"task ended\n")

        self.ready = True        
        report = " "
        if successflag is False:
            report = "(failed, no connection)"
            self.log.write(thisTime()+"error reported (might be empty): ")    
            self.log.write(report)
            self.log.write('\n')
        
        self.app.setTextArea("t1", pre+str(msg)+" "+report+"\n")
        
        return
    


# Run the application
# `python main.py`

if __name__ == '__main__':
    # Create an instance of your application
    App = Terminouja()
    # Start your app !
    App.Start()

     
    '''
    while True:
        if App.ser.inWaiting()>0: 
            
            App.Submit("Received something!","S",False)
            data_str = ser.read(ser.inWaiting()).decode('ascii') #read the bytes and convert from binary array to ASCII
            App.Submit(data_str,"O",False)
            
        time.sleep(0.01)
    '''
        