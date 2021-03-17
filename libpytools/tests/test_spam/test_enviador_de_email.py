import pytest

from libpytools.spam.enviador_de_email import Enviador, EmailInvalido


def test_criar_enviador_de_email():
    enviador=Enviador()
    assert enviador is not None


@pytest.mark.parametrize('remetente', ['jaquelinesa.82@gmail.com', 'foo@bar.com.br'])
def test_remetente(remetente):
    enviador = Enviador()
    resultado = enviador.enviar(
        remetente,
        'ana@python.pro.br',
        'Curso Python Pro',
        'Primeira turma 2021'
    )
    assert remetente in resultado


@pytest.mark.parametrize('remetente', ['', 'jaqueline'])
def test_remetente_invalido(remetente):
    enviador = Enviador()
    with pytest.raises(EmailInvalido):
        enviador.enviar(
            remetente,
            'jaqueline@python.pro.br',
            'Curso Python Pro',
            'Primeira turma 2021'
        )



