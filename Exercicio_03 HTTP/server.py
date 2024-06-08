import socket, sys, traceback, os;
from threading import Thread;


BLOCO = 20


def get_cabecalho(codigo: int) -> str:
    header = (
        f"HTTP/1.1 {codigo} OK\r\n"
        "content-type: text/html; charset=UTF-8\r\n\r\n"
    )
    return header


def get_file_desc(arquivo: str):
    return open(arquivo, 'rb')
    

def get_nome(requisicao: str):
    requisicao = requisicao.replace('/', '')
    if len(requisicao) == 0:
        return 'index.html'
    return f'{requisicao}.html'


def enviar_resposta(requisicao: str, connection: socket.socket) -> str:
    try:
        fd_arquivo = get_file_desc(requisicao)
        cabecalho = get_cabecalho(200).encode('UTF-8')
        
        connection.sendall(cabecalho)
        connection.sendfile(fd_arquivo)
        fd_arquivo.close()
        
    except:
        fd_arquivo = get_file_desc('./pag_erro.html')
        cabecalho = get_cabecalho(404).encode('UTF-8')
        
        connection.sendall(cabecalho)
        connection.sendfile(fd_arquivo)
        fd_arquivo.close()


def processar_req(addr, con: socket.socket):
    with con:
        print(f'O cliente "{addr[0]}" está se conectando!')
        
        metadados = ''
        while True:
            dados = con.recv(BLOCO)
            dados = dados.decode()
            metadados += dados
            
            if not dados or len(dados) < BLOCO:
                break
            
        metadados = metadados.split('\r\n')
        
        arquivo = metadados[0].split(' ')[1]
        arquivo = get_nome(arquivo)
        
        enviar_resposta(arquivo, con)
        
    print(f'fim da conexão com cliente "{addr[0]}"')


def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        porta = 8080
        c = 0
        while True:
            try:
                s.bind(('', porta))
                break
            except OSError as e:
                erro = str(e)
                if 'already in use' in erro:
                    porta += 1
            c += 1
            if c > 10:
                print(f'Já deu! As portas da 8080 até {porta} estão ocupadas!')
                break
        print(f'Escutando a porta {porta}')
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
