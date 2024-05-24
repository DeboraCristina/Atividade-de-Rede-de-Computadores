import socket, os


PORTA = 8081


def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect( ('192.168.18.203', PORTA) )

        try:
            # enviar o nome do arquivo
            nome_arquivo = './imagem_idiota.png'
            tamanho_arquivo = os.path.getsize(nome_arquivo)
            mensagem = f'{nome_arquivo};{tamanho_arquivo}'
            mensagem = (mensagem.encode())
            s.sendall(mensagem)

            # resposta do servidor
            resposta = s.recv(1024).decode()
            if resposta.upper() != 'OK':
                raise Exception('Erro ao enviar metadados')

            with open(nome_arquivo, 'rb') as fd:
                s.sendfile(fd)
                # Ao usar sendfile(), você melhora a eficiência da transferência de arquivos, 
                # especialmente para arquivos grandes, pois essa função é projetada para 
                # minimizar a sobrecarga do sistema operacional.
        
        except Exception as e:
            print(f'ERRO: {e}')


if __name__ == '__main__':
    main()
