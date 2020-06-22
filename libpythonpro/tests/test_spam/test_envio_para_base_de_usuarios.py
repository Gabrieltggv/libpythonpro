from libpythonpro.spam.enviador_de_email import Enviador
from libpythonpro.spam.main import EnviadorDeSpam


def test_envio_de_spam(sessao):
    envioador_de_spam = EnviadorDeSpam(sessao, Enviador)
    envioador_de_spam.enviar_emails(
        'gabrieltggv29@gmail',
        'Curso Python Pro',
        'Confira os módulos fantásticos'
    )
