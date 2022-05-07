import os
import re
import sys
import uuid
import signal
import hashlib
import smtplib

####### Autenticação do email remetente ######

login = 'seuemailaqui@gmail.com'
senha = 'suasenha123'

###############################################


class Util:

    def timeout(signum, frame):     #Define função para tempo limite
        raise Exception()

    signal.signal(signal.SIGALRM, timeout)


class Email:

    def __init__(self, login, senha, email, token): #Recebe os dados
        
        self.login = login
        self.senha = senha
        self.email = email
        self.token = token


    def Enviar_Token(self):

        os.system('clear')
        
        print(f'- Enviando Token para {self.email}, aguarde...\n\n- Verifique a caixa de spam -')

        msg = (f'Seu token é: {self.token}')    # Conteudo do email ao email destino 
        
        remetente = self.login
        senha = self.senha         # Dados para o envio do email
        destino = self.email
        smtp = "smtp.gmail.com"

        server = smtplib.SMTP(smtp, 587)
        server.starttls()
        server.login(remetente, senha)
        server.sendmail(remetente, destino, msg.encode('utf-8'))    #Enviar token

        token = self.token
        hash256 = hashlib.sha256()
        hash256.update(token.encode('utf-8'))       # Cria um hash do token gerado
        hash_token = hash256.hexdigest()

        del token        
        del self.login
        del self.senha      # Deletando dados sensíveis da memória
        del self.token 
        
        Run = Validar(self.email, hash_token)   # Compartilha o token e o email com classe de validação
        Run.Confirma_Token()



class Validar:

    def __init__(self, email, token):
        
        self.email = email
        self.token = token


    def Confirma_Token(self):

        email = str(self.email)
        valida = str(self.token)

        tentativas = int(5) #numero de tentativas 

        os.system('clear')
        print(f'- Token enviado para {self.email} -\n')
        
        while True:

            try:
                signal.alarm(180)   # tempo de expiração do token em segundos

                print(f'- O Token expira em 3 minutos -\n')
                cod = str(input('- Insira o Token: '))
                hash256 = hashlib.sha256()
                hash256.update(cod.encode('utf-8'))       #Cria uma hash do token inserido
                hash_token = hash256.hexdigest()
        
            except Exception as e:
                os.system('clear')
                print('- Seu Token Expirou -')
                os._exit()

            else:
                if tentativas == 0:
                    os.system('clear')
                    print('- Você errou 5 vezes -')
                    os._exit(0)

                elif hash_token == valida:  # Faz a validação se os dois hash são iguais
                    os.system('clear')
                    print(f'- Token Correto -')
                    os._exit(0)

                else:
                    os.system('clear')
                    print(f'- Token incorreto -\n')     # A cada token incorreto, conta como uma tentativa
                    tentativas -= 1

            finally:
                pass


class Formulario:

    def __init__(self, login, senha):
        
        self.login = login
        self.senha = senha

    def Form(self):

        os.system('clear')
        smtp = "smtp.gmail.com"
        
        ####### Tenta se conectar ao email remetente ########

        try:
            print('- Verificando Credenciais, aguarde... -\n')
            server = smtplib.SMTP(smtp, 587)
            server.starttls()
            server.login(self.login, self.senha)
        
        except smtplib.SMTPAuthenticationError:        
            os.system('clear')
            print(f'[ Erro de autenticação no email {login} ]')
            os._exit(0)

        else:
            os.system('clear')
            server.quit()

        ######################################################

        while True:

            print('\n- Two Factor Authenticator com Python -\n')
            
            email = str(input('- Digite seu email: '))

            ######## Valida o email recebido com regex #######

            regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

            if(re.search(regex,email)):
                os.system('clear')

                #token = uuid.uuid4() # Token gerado pela Lib UUID
                token = 'admintoken' # Token padrão (Não recomendado)

                Run = Email(self.login, self.senha, email, token)
                Run.Enviar_Token()

            else:
                os.system('clear')
                print('[ Digite um email válido ]')

            ###################################################



Run = Formulario(login, senha)
Run.Form()
