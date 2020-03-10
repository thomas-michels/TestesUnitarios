
from unittest import TestCase
from unittest.mock import Mock, patch, call
from app.api_cep import ApiCep, _get_somente_numeros

class MockApiCep(TestCase):

    @patch('api_cep.ApiCep.execute')
    def test_api_cep(self, mock_execute):

        mock_execute.assert_called_once()