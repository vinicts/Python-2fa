- Sistema de validação por email via Token -

- Plataforma de desenvolvimento:
	
	 Linux Debian 11

- Uso:
	
	 O Script escrito em python tem como finalidade servir como
	uma dupla verificação de segurança para API's, Interfaces
	gráficas ou CLI's para automações em bancos de dados.

	 Ultilizando a biblioteca smtplib, é possivel automatizar
	a função do envio de emails em massa para servir como 
	distribuição de tokens e validar se o email inserido é
	realmente válido e administrado por um humano.

- Segurança:
	
	 O Script também conta com alguns critérios básicos para
	garantir a segurança e a integridade das informações,
	como a biblioteca hashlib que é usada para gerar um hash
	do token, evitando a manipulação da string pela memória.

	 Na validação também existem algumas condições necessárias
	para que o usuário possa se autenticar, como a limitação
	de tentativas para comparar a hash do token, além tambem
	do tempo de expiração que por padrão é três minutos.

- Possíveis erros de execução:

	 Pode existir alguma incompatibilidade entre o módulo signal
	e o sistema operacional Windows, já que o módulo é voltado
	para o Unix.

	 Não foi testado nenhum outro provedor de email, então erros
	inesperados podem aparecer caso seja mudado a configuração do
	provedor Gmail.

- Palavras chave:
	
	Regex, validação, python, Linux Debian, Two Factor Authenticator.
