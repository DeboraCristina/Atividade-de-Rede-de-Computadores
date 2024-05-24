import socket


PORTA = 8081


def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect( ('192.168.18.97', PORTA) )
        
        mensagem = "Ola, Mundo! Enviando uma mensagem pois estou estundando socket"
        s.sendall( mensagem.encode() )
        print(f'{mensagem = }')

        resposta = s.recv(1024).decode()
        print(f'{resposta = }')
    
    pass


if __name__ == '__main__':
    main()