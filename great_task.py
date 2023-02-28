import RPi.GPIO as GPIO
import time
import cv2
import numpy as np
q=0
q2=0
i=1
cap = cv2.VideoCapture(0)
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

    
servo=11
servo_2=13
motor=16
GPIO.setup(servo,GPIO.OUT)
GPIO.setup(servo_2,GPIO.OUT)
GPIO.setup(motor,GPIO.OUT)
GPIO.output(16, True)
def ewq():
    for i in range(0,20):
        succ,img =cap.read()

def setServ(servo,angle):
    pwm=GPIO.PWM(servo,50)
    pwm.start(0)
    dutyCycle=angle/18.+2.
#     time.sleep(1)
    pwm.ChangeDutyCycle(dutyCycle)
    time.sleep(1)
    pwm.stop()
#     time.sleep(1)

def setMot(a):
    GPIO.output(16, a==0)
setServ(servo_2,0)
setServ(servo,0)
    
while True:
    succ,img =cap.read()
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    if i==1 and succ:
        i=2
        strt=img
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        mask1 = cv2.inRange(hsv, (0,68,68), (13,255,255)) #карсный
        mask2 = cv2.inRange(hsv, (24,68,80), (33,255,255)) #желтый
        mask3 = cv2.inRange(hsv, (41,140,13), (80,255,255)) #зелёный
        mask4 = cv2.inRange(hsv, (84,41,42), (138,255,255)) #синий
        
        rs=np.sum(mask1==255)
        ys=np.sum(mask2==255)
        gs=np.sum(mask3==255)
        bs=np.sum(mask4==255)
        cv2.imshow('str',strt)
    mask1 = cv2.inRange(hsv, (0,68,68), (13,255,255)) #карсный
    mask2 = cv2.inRange(hsv, (24,68,80), (33,255,255)) #желтый
    mask3 = cv2.inRange(hsv, (41,140,13), (80,255,255)) #зелёный
    mask4 = cv2.inRange(hsv, (84,41,42), (138,255,255)) #синий
    
    r=np.sum(mask1==255)-rs
    y=np.sum(mask2==255)-ys
    g=np.sum(mask3==255)-gs
    b=np.sum(mask4==255)-bs
    if r==max(r,y,g,b) and r>10000:
        setMot(0)
        if q==0 and q2==0:
            q=1
            setServ(servo_2,110)
            setMot(1)
            time.sleep(1)
            setMot(0)
            setServ(servo_2,0)
            setMot(1)
            ewq()
        elif q!=0 and q!=1:
            q2=1
            setMot(1)
            time.sleep(1.2)
            setMot(0)
            setServ(servo,110)
            setMot(1)
            time.sleep(1)
            setMot(0)
            setServ(servo,0)
            setMot(1)
            break
    elif y==max(r,y,g,b)  and y>10000:
        setMot(0)
        if q==0 and q2==0:
            q=2
            setServ(servo_2,110)
            setMot(1)
            time.sleep(1)
            setMot(0)
            setServ(servo_2,0)
            setMot(1)
            ewq()
        elif q!=0 and q!=2:
            q2=2
            setMot(1)
            time.sleep(1.2)
            setMot(0)
            setServ(servo,110)
            setMot(1)
            time.sleep(1)
            setMot(0)
            setServ(servo,0)
            setMot(1)
            break
    elif g==max(r,y,g,b)  and g>10000:
        setMot(0)
        if q==0 and q2==0:
            q=3
            setServ(servo_2,110)
            setMot(1)
            time.sleep(1)
            setMot(0)
            setServ(servo_2,0)
            setMot(1)
            ewq()
        elif q!=0 and q!=3:
            q2=3
            setMot(1)
            time.sleep(1.2)
            setMot(0)
            setServ(servo,110)
            setMot(1)
            time.sleep(1)
            setMot(0)
            setServ(servo,0)
            setMot(1)
            break
    elif b>10000:
        setMot(0)
        if q==0 and q2==0:
            q=4
            setServ(servo_2,110)
            setMot(1)
            time.sleep(1)
            setMot(0)
            setServ(servo_2,0)
            setMot(1)
            ewq()
        elif q!=0 and q!=4:
            q2=4
            setMot(1)
            time.sleep(1.2)
            setMot(0)
            setServ(servo,110)
            setMot(1)
            time.sleep(1)
            setMot(0)
            setServ(servo,0)
            setMot(1)
            break
    else:
        setMot(1)
    cv2.imshow('xzx',img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
setMot(0)
time.sleep(3)
i=1
ewq()
print(q,q2)
while True:
    succ,img =cap.read()
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    if i==1 and succ:
        i=2
        strt=img
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        mask1 = cv2.inRange(hsv, (0,68,68), (13,255,255)) #карсный
        mask2 = cv2.inRange(hsv, (24,68,80), (33,255,255)) #желтый
        mask3 = cv2.inRange(hsv, (41,140,13), (80,255,255)) #зелёный
        mask4 = cv2.inRange(hsv, (84,41,42), (138,255,255)) #синий
        
        rs=np.sum(mask1==255)
        ys=np.sum(mask2==255)
        gs=np.sum(mask3==255)
        bs=np.sum(mask4==255)
        cv2.imshow('str',strt)
    mask1 = cv2.inRange(hsv, (0,68,68), (13,255,255)) #карсный
    mask2 = cv2.inRange(hsv, (24,68,80), (33,255,255)) #желтый
    mask3 = cv2.inRange(hsv, (41,140,13), (80,255,255)) #зелёный
    mask4 = cv2.inRange(hsv, (84,41,42), (138,255,255)) #синий
    
    r=np.sum(mask1==255)-rs
    y=np.sum(mask2==255)-ys
    g=np.sum(mask3==255)-gs
    b=np.sum(mask4==255)-bs
    
    if r==max(r,y,g,b) and r>10000:
        if q==1:
            setMot(0)
            setServ(servo_2,110)
            setMot(1)
            time.sleep(1)
            setMot(0)
            setServ(servo_2,0)
            setMot(1)
            ewq()
        elif q2==1:
            setMot(1)
            time.sleep(1.2)
            setMot(0)
            setServ(servo,110)
            setMot(1)
            time.sleep(1)
            setMot(0)
            setServ(servo,0)
            setMot(1)
            ewq()
    elif y==max(r,y,g,b)  and y>10000:
        if q==2:
            setMot(0)
            setServ(servo_2,110)
            setMot(1)
            time.sleep(1)
            setMot(0)
            setServ(servo_2,0)
            setMot(1)
            ewq()
        elif q2==2:
            setMot(1)
            time.sleep(1.2)
            setMot(0)
            setServ(servo,110)
            setMot(1)
            time.sleep(1)
            setMot(0)
            setServ(servo,0)
            setMot(1)
            ewq()
    elif g==max(r,y,g,b)  and g>10000:
        if q==3:
            setMot(0)
            setServ(servo_2,110)
            setMot(1)
            time.sleep(1)
            setMot(0)
            setServ(servo_2,0)
            setMot(1)
            ewq()
        elif q2==3:
            setMot(1)
            time.sleep(1.2)
            setMot(0)
            setServ(servo,110)
            setMot(1)
            time.sleep(1)
            setMot(0)
            setServ(servo,0)
            setMot(1)
            ewq() 
    elif b>10000:
        if q==4:
            setMot(0)
            setServ(servo_2,110)
            setMot(1)
            time.sleep(1)
            setMot(0)
            setServ(servo_2,0)
            setMot(1)
            ewq()
        elif q2==4:
            setMot(1)
            time.sleep(1.2)
            setMot(0)
            setServ(servo,110)
            setMot(1)
            time.sleep(1)
            setMot(0)
            setServ(servo,0)
            setMot(1)
            ewq()
    else:
        setMot(1)
    cv2.imshow('xzx',img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
print(1)


# setMot(0.5)
# setServ(servo,110)
# setServ(servo_2,110)
# setMot(0)
# setServ(servo,0)
# setServ(servo_2,0)

GPIO.cleanup()
