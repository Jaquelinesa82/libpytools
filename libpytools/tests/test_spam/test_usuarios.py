from libpytools.spam.modelos import Usuario


def test_salvar_usuario(sessao):
    usuario = Usuario(nome='jaqueline')
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)


def test_listar_usuarios(sessao):
    usuarios = [Usuario(nome='Jaqueline'), Usuario(nome='Ana')]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()
