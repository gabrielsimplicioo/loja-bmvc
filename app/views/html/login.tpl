<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Entrar - TechNode</title>
    <link rel="stylesheet" type="text/css" href="/static/css/style.css">
</head>
<body>

    <header class="topbar">
        <div class="brand"><span class="dot">&#9679;</span> TechNode</div>
        <nav class="mainnav">
            <a href="/">Inicio</a>
            <a href="/produtos">Catalogo</a>
        </nav>
    </header>

    <section class="section">
        <h2>Acesso administrativo</h2>
        <p>Entre com sua conta para cadastrar, editar ou remover produtos do catalogo.</p>

        % if erro:
        <div class="flash flash-erro">{{erro}}</div>
        % end

        <form method="POST" action="/login" class="form-produto">
            <label for="username">Usuario</label>
            <input type="text" id="username" name="username" required autofocus>

            <label for="senha">Senha</label>
            <input type="password" id="senha" name="senha" required>

            <div class="form-acoes">
                <button type="submit">Entrar</button>
            </div>
        </form>
    </section>

    <footer>
        &copy; 2026 TechNode - Projeto academico desenvolvido com o framework BMVC (Bottle).
    </footer>

</body>
</html>
