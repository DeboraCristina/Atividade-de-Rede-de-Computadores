import socket, sys, traceback;
from threading import Thread;


BLOCO = 1024*10
PORTA = 8081


def processar_req(addr, con):
    with con:
        print(f'O cliente "{addr[0]}" está se conectando!')

        metadados = con.recv(1024) # O esquema de while true não funcionou
        metadados = metadados.decode()

        if ';' not in metadados:
            con.sendall("NOT OK".encode())
            return
        
        nome_arquivo, tamanho_arquivo = metadados.split(';')
        tamanho_arquivo = int(tamanho_arquivo)
        con.sendall("OK".encode())

        with open(nome_arquivo, 'wb') as fd:
            while True:
                data = con.recv(BLOCO)

                if not data:
                    break

                fd.write(data)
    print(f'fim da conexão com cliente "{addr[0]}"')


def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('', PORTA))
        print(f'Escutando a porta {PORTA}')
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
