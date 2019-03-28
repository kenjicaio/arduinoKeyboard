from time import sleep
import keyboard
import serial
import serial.tools.list_ports as listUSB

quit = False # Condição para fechar o programa
mPorts = False # Para verficar se há múltiplos dispositivos conectáveis
ports = list(listUSB.comports()) # Lista de portas seriais em formato serial.tools
names = [] # Lista de nomes em formato string
tries = [] # Seleção de potenciais portas para conectar
ct = 0 # Contador 
ard = 0

for p in ports:
    names.append(str(p))
    
if len(ports) == 1:
    print("Apenas um dispositivo encontrado, tentando conectar")
    ard = serial.Serial(names[0][0:4])
    r = ard.read()
    r = r.decode('ascii')
    if r is 'c':
        print("Conectado")
    else:
        print("Erro ao conectar")
        exit()
else:
    print("Múltiplos dispositivos encontrados")
    mPorts = True
    for n in names:
        if n.find("CH340") is not -1:
            tries.append(n[0:4])

if mPorts:
    if len(tries) == 1:
        print("Apenas um dispositivo apto, tentando conectar")
        ard = serial.Serial(tries[0])
        r = ard.read()
        r = r.decode('ascii')
        if r is 'c':
            print("Conectado")
        else:
            print("Erro ao conectar")
            exit()
    else:
        print("Testando conexão com dispositivos")
        for t in tries:
            ard = serial.Serial(t)
            r = ard.read()
            r = r.decode('ascii')
            if r is 'c':
                print("Conectado")
                break
            else:
                print("Erro ao conectar, tentando outro dispositivo")
                ard = 0;        
            
if ard == 0:
    print("Não foi possível conectar, saindo do programa")
    exit();

while quit is False:
    if ard.inWaiting() == 0:
        r = 0
    else:
        try:
            r = ard.read()
            r = r.decode('ascii')
            if r >= 'A' and r <= 'z':
                if r.isupper():
                    keyboard.release(r.lower())
                else:
                    keyboard.press(r)
        except serial.serialutil.SerialException:
            print ("Dispositivo desconectado, fechando programa")
            quit = True

if quit is not True:
    print('Erro inesperado, fechando programa')
    ard.close()