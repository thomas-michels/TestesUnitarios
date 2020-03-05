# Criar testes para todos os métodos e classes dos seguintes arquivos:


# 1. run.py

    testar método -> consulta_api_viacep()
        
        requisitos mínimos:     
            1. criar mock do método input().
            2. criar mock do método print().
            3. realizar assert para o mock do método input(), afirmando que este mock foi chamado uma única vez e afirmando quais foram os argumentos passados no mock do input().
            4. realizar assert para o mock do método print(), afirmando que este mock foi chamado uma única vez e afirmando quais foram os argumentos passados no mock do print().
            5. ensinar ao mock do método input(), qual valor ele deverá retornar quando ele for chamado.
            6. verificar se o retorno ensinado ao mock do método input() foi passado como argumento ao mock do método print().
            7. gerar html com a cobertura de código realizada pelo teste e garantir 100% de cobertura para o código do arquivo run.py

        desafio:
            1. criar mock do método execute() da classe ApiCep()
            2. realizar assert do método execute() da classe ApiCep(), afirmando que este mock foi chamado uma única vez e afirmando quais foram os argumentos passados no mock do execute().
            3. gerar html com a cobertura de código realizada pelo teste e garantir que o teste está cobrindo somente o arquivo run.py

# 2. api_cep.py

    testar método -> _get_somente_numeros(dados)
        
        requisitos mínimos:
            1. realizar assert do retorno do método, afirmando que o retorno é somente os números contidos no parâmetro recebido (simular um parâmetro contendo letras, números e caracteres especiais).

        desafio:
            1. criar mock do método sub() do módulo re.
            2. ensinar ao mock do método sub() do módulo re, qual valor ele deverá retornar quando ele for chamado.
            3. realizar assert para mock do método sub() do módulo re, afirmando que este mock foi chamado uma única vez e afirmando quais foram os argumentos passados no mock do sub()
            4. verificar se o retorno ensinado ao mock do método sub() do módulo re foi passado para o retorno do método _get_somente_numeros(dados).

    testar classe -> ApiCep() -> mais especificamente o método execute()

        requisitos mínimos:
            1. criar mock do método _get_somente_numeros(cep).
            2. realizar assert para o mock do método _get_somente_numeros(cep), afirmando que este mock foi chamado uma única vez e afirmando quais foram os argumentos passados no mock do _get_somente_numeros(cep).

        desafio:
            1. criar mock do método get() do módulo requests.
            2. ensinar ao mock do método get() do módulo requests, qual valor ele deverá retornar quando ele for chamado.
            3. realizar assert para o mock do método get() do módulo requests, afirmando que este mock foi chamado uma única vez e afirmando quais foram os argumentos passados no mock do get()


        desafio (merece uma cota do meu mercadotech):
            1. criar mock do método json() da linha 11 do arquivo api_cep.py
            2. realizar assert para o mock do método json(), afirmando que este mock foi chamado uma única vez e afirmando quais foram os argumentos passados no mock do json()


# Observações:

    Para instalar o módulo requests do python é necessário ter instalado o pipenv.
    
        pip install pipenv
        pipenv install requests