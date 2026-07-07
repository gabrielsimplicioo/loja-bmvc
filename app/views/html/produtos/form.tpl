<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{'Editar produto' if produto else 'Novo produto'}} - TechNode</title>
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
        <h2>{{'Editar produto' if produto else 'Novo produto'}}</h2>

        % if erro:
        <div class="flash flash-erro">{{erro}}</div>
        % end

        <form method="POST" action="{{'/produtos/%d' % produto.id if produto else '/produtos'}}" class="form-produto">
            <label for="nome">Nome</label>
            <input type="text" id="nome" name="nome" required value="{{produto.nome if produto else ''}}">

            <label for="categoria">Categoria</label>
            <select id="categoria" name="categoria" required>
                <option value="">Selecione...</option>
                % for c in categorias:
                <option value="{{c}}" {{'selected' if produto and produto.categoria.value == c else ''}}>{{c}}</option>
                % end
            </select>

            <label for="preco">Preco (R$)</label>
            <input type="number" id="preco" name="preco" step="0.01" min="0" required
                   value="{{produto.preco if produto else ''}}">

            <label for="estoque">Estoque</label>
            <input type="number" id="estoque" name="estoque" min="0" required
                   value="{{produto.estoque if produto else ''}}">

            <label for="descricao">Descricao</label>
            <textarea id="descricao" name="descricao" rows="3">{{produto.descricao if produto else ''}}</textarea>

            <div class="form-acoes">
                <button type="submit">{{'Salvar' if produto else 'Cadastrar'}}</button>
                <a href="/produtos">Cancelar</a>
            </div>
        </form>
    </section>

    <footer>
        &copy; 2026 TechNode - Projeto academico desenvolvido com o framework BMVC (Bottle).
    </footer>

</body>
</html>
