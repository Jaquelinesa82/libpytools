import pytest

from libpytools.spam.enviador_de_email import Enviador
from libpytools.spam.main import EnviadorDeSpam
from libpytools.spam.modelos import Usuario


class EnviadorMock(Enviador):
    def __init__(self):
        super().__init__()
        self.qtd_email_enviados = 0
        self.parametros_de_envio = None

    def enviar(self, remetente, destinatario, assunto, corpo):
        self.parametros_de_envio = (remetente, destinatario, assunto, corpo)
        self.qtd_email_enviados += 1


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
def test_qtd_de_spam(sessao, usuarios):
    for usuario in usuarios:
        sessao.salvar(usuario)
    enviador = EnviadorMock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'jaquelinesa.82@gmail.com',
        'Curso Python Pro',
        'Confira os módulos'
    )
    assert len(usuarios) == enviador.qtd_email_enviados


def test_parametros_de_spam(sessao):
    usuario = Usuario(nome='Jaqueline', email='jaquelinesa.82@gmail.com')
    sessao.salvar(usuario)
    enviador = EnviadorMock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'ana@gmail.com',
        'Curso Python Pro',
        'Confira os módulos'
    )
    assert enviador.parametros_de_envio == (
        'ana@gmail.com',
        'jaquelinesa.82@gmail.com',
        'Curso Python Pro',
        'Confira os módulos'
    )
