<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>TechNode - Loja de Tecnologia</title>
    <link rel="stylesheet" type="text/css" href="/static/css/style.css">
    <script src="/static/js/main.js"></script>
</head>
<body>

    <header class="topbar">
        <div class="brand"><span class="dot">&#9679;</span> TechNode</div>
        <nav class="mainnav">
            <a href="#produtos">Destaques</a>
            <a href="/produtos">Catalogo completo</a>
            <a href="#sobre">Sobre</a>
            <a href="#contato">Contato</a>
            % if usuario_logado:
            <span class="nav-usuario">Ola, {{usuario_logado}}</span>
            <form method="POST" action="/logout" class="form-logout"><button type="submit" class="link-btn">Sair</button></form>
            % else:
            <a href="/login">Entrar</a>
            % end
        </nav>
    </header>

    <section class="hero">
        <h1>Tecnologia com curadoria, direto para o seu setup.</h1>
        <p>
            A TechNode e uma loja especializada em componentes e perifericos de
            computador. Selecionamos produtos com boa relacao custo-beneficio
            para montadores, gamers e profissionais de TI.
        </p>
        <a class="btn" href="#produtos">Ver catalogo</a>
        <p style="margin-top: 26px; color: var(--muted); font-size: 0.85em;">
            Horario local da loja: <span id="clock">--:--:--</span>
        </p>
    </section>

    <section class="section" id="produtos">
        <h2>Categorias em destaque</h2>
        <div class="grid">
            <div class="card">
                <span class="tag">Hardware</span>
                <h3>Placas de video</h3>
                <p>Modelos para uso profissional e gaming, das entradas as top de linha.</p>
            </div>
            <div class="card">
                <span class="tag">Perifericos</span>
                <h3>Teclados mecanicos</h3>
                <p>Switches variados, layout ABNT2 e opcoes com fio ou wireless.</p>
            </div>
            <div class="card">
                <span class="tag">Armazenamento</span>
                <h3>SSDs NVMe</h3>
                <p>Alto desempenho para sistemas operacionais e jogos.</p>
            </div>
            <div class="card">
                <span class="tag">Redes</span>
                <h3>Roteadores Wi-Fi 6</h3>
                <p>Cobertura ampliada e estabilidade para home office.</p>
            </div>
        </div>
        <p style="color: var(--muted); margin-top: 18px; font-size: 0.9em;">
            Estes sao apenas destaques. Acesse o catalogo completo para ver, cadastrar,
            editar e remover produtos do estoque da TechNode.
        </p>
        <a class="btn btn-secondary" href="/produtos" style="margin-top: 10px;">Ver catalogo completo</a>
    </section>

    <section class="section" id="sobre">
        <h2>Sobre a TechNode</h2>
        <p>
            Fundada por entusiastas de tecnologia, a TechNode nasceu da necessidade
            de encontrar pecas de qualidade sem complicacao. Nosso objetivo e claro:
            oferecer um catalogo enxuto, com informacoes tecnicas honestas, para que
            o cliente monte o setup ideal sem depender de vendedores.
        </p>
    </section>

    <section class="section" id="contato">
        <h2>Fique por dentro das novidades</h2>
        <p style="color: var(--muted);">Cadastre seu e-mail e receba avisos sobre novos produtos e promocoes.</p>
        <form id="newsletter-form" style="display:flex; gap:10px; flex-wrap:wrap; margin-top:16px;">
            <input id="newsletter-email" type="email" placeholder="seu@email.com"
                   style="flex:1; min-width:220px; padding:12px; border-radius:8px; border:1px solid var(--border); background:#0f1115; color:var(--text);">
            <button class="btn" type="submit">Inscrever</button>
        </form>
    </section>

    <footer>
        &copy; 2026 TechNode - Projeto academico desenvolvido com o framework BMVC (Bottle).
    </footer>

</body>
</html>
