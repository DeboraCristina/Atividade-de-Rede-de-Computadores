import socket, sys, traceback;
from threading import Thread;


BLOCO = 10
PORTA = 8081


def main():
    # SOCK_STREAM -> tcp
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        #s.bind(ip, porta)
        #pode especificar um ip ou escutar todos ('')
        s.bind(('', PORTA))
        
        # Define qnts clientes(requisições) ouvir
        print(f'Escutando a porta {PORTA}')
        s.listen(1)

        # Aceita conexão.
        con, addr = s.accept()

        with con:
            print(f'O cliente "{addr[0]}" está se conectando!')

            while True:
                # oq é recebendo na conexão. con vai ler um BLOCO (qnd d bytes)
                data = con.recv(BLOCO)

                if not data:
                    break

                print(f'Recebi do Cliente: "{data}"')
    
    pass


if __name__ == '__main__':
    main()
