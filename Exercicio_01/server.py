import socket, sys, traceback;
from threading import Thread;


BLOCO = 1024
PORTA = 8081


def processar_req(addr, con):
    with con:
        print(f'O cliente "{addr[0]}" está se conectando!')

        msg = ''
        while True:
            # por algum motivo o processo bloqueia qnd data fica vazio e não continua o código.
            data = con.recv(BLOCO)
            print('dado')

            if not data:
                break

            msg += data.decode()

        msg = msg.upper()
        con.sendall(msg.encode())
        print(f'Conexão com cliente "{addr[0]}" finalizada!')


def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('', PORTA))
        print(f'Escutando a porta {PORTA} para o exercicio 01')
        s.listen(100)

        while True:
            try:
                con, addr = s.accept()
                thread = Thread(target=processar_req, args=(addr, con))
                thread.start()
            except KeyboardInterrupt:
                sys.exit(1)
            except:
                traceback.print_exc()


if __name__ == '__main__':
    main()
