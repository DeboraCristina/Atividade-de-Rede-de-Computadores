import socket


PORTA = 8081


def main():
    # SOCK_STREAM -> tcp
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # Solicita conexão para um ip e um porta
        s.connect( ('192.168.18.203', 8081) )
        # Envia uma msg em binário
        s.sendall( b"Ola, Mundo! Enviando uma mensagem pois estou estundando socket" )
    
    pass


if __name__ == '__main__':
    main()