import pytest

from libpythonpro.spam.enviador_de_email import Enviador


def test_criar_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None


@pytest.mark.parametrize(
    'remetente',
    ['foo@bar.com.br', 'gabrieltggv29@gmail.com']
)
def test_remetente(remetente):
    enviador = Enviador()

    resultado = enviador.enviar(
        remetente,
        'suporte@vilatec.com.br',
        'Curso Python Pro',
        'Primeiro teste da turma Luiz Vital.'
    )
    assert remetente in resultado
