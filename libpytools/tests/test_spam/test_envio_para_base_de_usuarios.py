from unittest.mock import Mock

import pytest

from libpytools.spam.main import EnviadorDeSpam
from libpytools.spam.modelos import Usuario


@pytest.mark.parametrize(
    'usuarios',
    [
        [
            Usuario(nome='Jaqueline', email='jaquelinesa.82@gmail.com'),
            Usuario(nome='Ana', email='ana@gmail.com')
        ],
        [
            Usuario(nome='Jaqueline', email='jaquelinesa.82@gmail.com')
        ]
    ]
 )
def test_qte_de_spam(sessao, usuarios):
    for usuario in usuarios:
        sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'jaquelinesa.82@gmail.com',
        'Curso Python Pro',
        'Confira os módulos'
    )
    assert len(usuarios) == enviador.enviar.call_count


def test_parametros_de_spam(sessao):
    usuario = Usuario(nome='Jaqueline', email='jaquelinesa.82@gmail.com')
    sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'ana@gmail.com',
        'Curso Python Pro',
        'Confira os módulos'
    )
    enviador.enviar.assert_called_once_with(
        'ana@gmail.com',
        'jaquelinesa.82@gmail.com',
        'Curso Python Pro',
        'Confira os módulos'
    )
