<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Catalogo de Produtos - TechNode</title>
    <link rel="stylesheet" type="text/css" href="/static/css/style.css">
    <script src="/static/js/produtos.js" defer></script>
</head>
<body>

    <header class="topbar">
        <div class="brand"><span class="dot">&#9679;</span> TechNode</div>
        <nav class="mainnav">
            <a href="/">Inicio</a>
            <a href="/produtos">Catalogo</a>
            % if usuario_logado:
            <span class="nav-usuario">Ola, {{usuario_logado}}</span>
            <form method="POST" action="/logout" class="form-logout"><button type="submit" class="link-btn">Sair</button></form>
            % else:
            <a href="/login">Entrar</a>
            % end
        </nav>
    </header>

    <section class="section">
        <h2>Catalogo de produtos</h2>

        % if usuario_logado:
        <p><a class="btn" href="/produtos/novo">+ Novo produto</a></p>
        % end

        % if texto_flash:
        <div class="flash flash-{{tipo_flash}}">{{texto_flash}}</div>
        % end

        % if produtos:
        <table class="tabela-produtos">
            <thead>
                <tr>
                    <th>Nome</th>
                    <th>Categoria</th>
                    <th>Preco</th>
                    <th>Estoque</th>
                    % if usuario_logado:
                    <th></th>
                    % end
                </tr>
            </thead>
            <tbody>
                % for p in produtos:
                <tr>
                    <td>{{p.nome}}</td>
                    <td>{{p.categoria.value}}</td>
                    <td>{{p.preco_formatado}}</td>
                    <td>{{p.estoque}}</td>
                    % if usuario_logado:
                    <td>
                        <a href="/produtos/{{p.id}}/editar">Editar</a>
                        <form method="POST" action="/produtos/{{p.id}}/excluir" class="form-excluir">
                            <button type="submit">Excluir</button>
                        </form>
                    </td>
                    % end
                </tr>
                % end
            </tbody>
        </table>
        % else:
        <p>Nenhum produto cadastrado.</p>
        % end
    </section>

    <footer>
        &copy; 2026 TechNode - Projeto academico desenvolvido com o framework BMVC (Bottle).
    </footer>

</body>
</html>
