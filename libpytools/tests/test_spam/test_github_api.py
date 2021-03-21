from unittest.mock import Mock

from libpytools import github_api


def test_buscar_avatar():
    resp_mock = Mock()
    resp_mock.json.return_value = {
        'login': 'jaqueline', 'id': 713793,
        'avatar_url': 'https://avatars.githubusercontent.com/u/713793?v=4',
    }
    github_api.requests.get = Mock(return_value=resp_mock)
    url = github_api.buscar_avatar('Jaqueline')
    assert 'https://avatars.githubusercontent.com/u/713793?v=4' == url