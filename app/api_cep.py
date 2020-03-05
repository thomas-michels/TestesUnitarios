import requests
import re

def _get_somente_numeros(dados : str) -> str:
    return re.sub('[^0-9]', '', dados)

class ApiCep:
    def execute(self, cep : str) -> dict:
        cep_convertido_somente_em_numeros = _get_somente_numeros(cep)
        response = requests.get(f'http://www.viacep.com.br/ws/{cep_convertido_somente_em_numeros}/json/')
        return response.json()