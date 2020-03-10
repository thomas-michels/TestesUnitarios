
from unittest import TestCase
from unittest.mock import Mock, patch, call
from app.api_cep import ApiCep, _get_somente_numeros

class TestApiCep(TestCase):

    @patch('app.api_cep.requests.get')
    @patch('app.api_cep._get_somente_numeros')
    def test_api_cep(self, mock_get_numeros, mock_get):
        consulta = ApiCep()
        retorno_api = Mock()
        retorno_api.json.return_value = 'Retorno Api'
        mock_get_numeros.return_value = '89066040'
        mock_get.return_value = retorno_api

        resultado = consulta.execute('89066040')

        self.assertEqual(resultado, 'Retorno Api')
        mock_get_numeros.assert_called_once_with('89066040')
        mock_get.assert_called_with('http://www.viacep.com.br/ws/89066040/json/')
        retorno_api.assert_called_once_with()

    @patch('app.api_cep.re.sub')
    def test_get_somente_numeros(self, mock_re_sub):
        mock_re_sub.return_value = '89066040'

        resultado = _get_somente_numeros('890*66-,=040')

        self.assertEqual(resultado, '89066040')
        mock_re_sub.assert_called_once('[^0-9]', '', '890*66-,=040')