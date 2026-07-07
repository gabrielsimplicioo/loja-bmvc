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
        </nav>
    </header>

    <section class="section">
        <h2>Catalogo de produtos</h2>
        <p><a class="btn" href="/produtos/novo">+ Novo produto</a></p>

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
                    <th></th>
                </tr>
            </thead>
            <tbody>
                % for p in produtos:
                <tr>
                    <td>{{p.nome}}</td>
                    <td>{{p.categoria.value}}</td>
                    <td>{{p.preco_formatado}}</td>
                    <td>{{p.estoque}}</td>
                    <td>
                        <a href="/produtos/{{p.id}}/editar">Editar</a>
                        <form method="POST" action="/produtos/{{p.id}}/excluir" class="form-excluir">
                            <button type="submit">Excluir</button>
                        </form>
                    </td>
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
