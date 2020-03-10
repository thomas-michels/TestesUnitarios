
from unittest import TestCase
from unittest.mock import Mock, patch, call
from run import consulta_api_viacep


class TestConsultaApiViacep(TestCase):

    @patch('run.ApiCep.execute')
    @patch('run.input')
    @patch('run.print')
    def test_consulta_api_viacep(self, mock_print, mock_input, mock_execute):
        mock_input.return_value = "89066040"
        mock_execute.return_value = 'retorno json'

        new_consulta = consulta_api_viacep()

        self.assertEqual(new_consulta, 'Cep consultado com sucesso!')

        mock_execute.assert_called_once_with("89066040")

        mock_input.assert_called_once_with('Informe o cep para consulta: ')

        mock_print.assert_called_once_with("retorno json")

# pip3 install coverage
# py -m coverage run -m unittest discover
# py -m coverage report -m
# py -m coverage html
