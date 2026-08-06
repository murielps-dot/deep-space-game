import serial
import serial.tools.list_ports
import pyautogui
import time
import sys

pyautogui.FAILSAFE = False

def achar_porta():
    portas = serial.tools.list_ports.comports()
    for p in portas:
        if 'Arduino' in p.description or 'CH340' in p.description or 'USB' in p.description:
            return p.device
    return None

porta = achar_porta()

if porta is None:
    print("Arduino não encontrado!")
    print("Portas disponíveis:")
    for p in serial.tools.list_ports.comports():
        print(f"  {p.device} — {p.description}")
    print("\nSe souber a porta, edite a linha abaixo e substitua achar_porta() por ela.")
    print("Exemplo:  porta = 'COM4'")
    input("Pressione Enter para sair...")
    sys.exit()

print(f"Arduino encontrado em: {porta}")

try:
    arduino = serial.Serial(porta, 9600, timeout=1)
except Exception as e:
    print(f"Erro ao conectar: {e}")
    input("Pressione Enter para sair...")
    sys.exit()

time.sleep(2)
print("Conectado!")
print("Abra o jogo no navegador, clique na tela e pode jogar.")
print("Pressione CTRL+C aqui para encerrar.\n")

TECLAS_VALIDAS = ['w', 's', 'a', 'd', 'f', 'q']

while True:
    try:
        linha = arduino.readline().decode('utf-8').strip()
        if not linha or linha == 'PRONTO':
            continue

        if len(linha) < 3:
            continue

        acao  = linha[0:2]   # 'P:' = pressionou, 'R:' = soltou
        tecla = linha[2:]    # letra da tecla

        if tecla not in TECLAS_VALIDAS:
            continue

        if acao == 'P:':
            pyautogui.keyDown(tecla)
            nomes = {'w':'CIMA','s':'BAIXO','a':'ESQUERDA','d':'DIREITA','f':'FOTO','q':'START'}
            print(f"▼ {nomes.get(tecla, tecla.upper())}")
        elif acao == 'R:':
            pyautogui.keyUp(tecla)

    except KeyboardInterrupt:
        print("\nEncerrando — soltando todas as teclas...")
        for t in TECLAS_VALIDAS:
            pyautogui.keyUp(t)
        arduino.close()
        print("Encerrado.")
        break
    except Exception as e:
        print(f"Erro: {e}")
        time.sleep(0.1)