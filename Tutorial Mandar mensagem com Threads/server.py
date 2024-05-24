import socket, sys, traceback;
from threading import Thread;


BLOCO = 10
PORTA = 8081


def processar_req(addr, con):
    with con:
        print(f'O cliente "{addr[0]}" está se conectando!')

        while True:
            data = con.recv(BLOCO)

            if not data:
                break

            print(f'Recebi do Cliente: "{data}"')


def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('', PORTA))
        print(f'Escutando a porta {PORTA}')
        s.listen(100)

        while True:
            try:
                con, addr = s.accept()
                #thread = Thread(func para processar a requisição, (endereço, conexão))
                thread = Thread(target=processar_req, args=(addr, con))
                thread.start()

                # Não deve se colocar mais nada nesse while true. 
                # O obj dessa função é acelerar a conexão cliente-servidor.
                # Qualquer outro processamento deixará esse processo mt lento
                # O ideal é atender o máximo de clientes possível
            except KeyboardInterrupt:
                sys.exit(1)
            except:
                traceback.print_exc()


if __name__ == '__main__':
    main()
