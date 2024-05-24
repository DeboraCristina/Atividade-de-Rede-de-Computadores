import socket, sys, traceback;
from threading import Thread;


BLOCO = 1024;


def processar_requisicao(addr, conn):
    with conn:
        print('Conexão recebida, endereço cliente:', addr);
        while True:
            data = conn.recv(BLOCO);
            if not data: break
            print("Recebi do cliente:", data);


def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(("", 8081));
        s.listen(100);
        while True:
            try:  
                conn, addr = s.accept();
                t = Thread(target=processar_requisicao, args=(addr, conn, ));
                t.start();
            except KeyboardInterrupt:
               sys.exit(1);
            except:
               traceback.print_exc();


if __name__ == '__main__':
    main();
