from libpytools.spam.enviador_de_email import Enviador
from libpytools.spam.main import EnviadorDeSpam


def test_envio_de_spam(sessao):
    enviador_de_spam = EnviadorDeSpam(sessao, Enviador())
    enviador_de_spam.enviar_emails(
        'jaquelinesa.82@gmail.com',
        'Curso Python Pro',
        'Cnfira os módulos'
    )
