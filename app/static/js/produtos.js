// interacoes da pagina de produtos: confirmacao de exclusao e catalogo em tempo real

document.addEventListener('DOMContentLoaded', function () {
    document.addEventListener('submit', function (event) {
        if (event.target.matches('.form-excluir') && !confirm('Remover este produto do catalogo?')) {
            event.preventDefault();
        }
    });

    if (document.getElementById('catalogo')) {
        iniciarWebsocketEstoque();
    }
});

function iniciarWebsocketEstoque() {
    const socket = new WebSocket(`ws://${window.location.hostname}:8081`);

    socket.addEventListener('message', function (event) {
        const dados = JSON.parse(event.data);
        switch (dados.evento) {
            case 'criado':
                adicionarLinha(dados.produto);
                break;
            case 'atualizado':
                atualizarLinha(dados.produto);
                break;
            case 'excluido':
                removerLinha(dados.produto);
                break;
        }
    });

    socket.addEventListener('close', function () {
        setTimeout(iniciarWebsocketEstoque, 3000);
    });
}

function adicionarLinha(produto) {
    const corpo = document.getElementById('tabela-produtos-corpo');
    if (!corpo || corpo.querySelector(`tr[data-id="${produto.id}"]`)) return;

    const tabela = document.querySelector('.tabela-produtos');
    corpo.appendChild(criarLinhaProduto(produto, tabela.dataset.admin === 'true'));
    showToast(`Novo produto no catalogo: ${produto.nome}`);
}

function atualizarLinha(produto) {
    const linha = document.querySelector(`tr[data-id="${produto.id}"]`);
    if (!linha) return;

    linha.querySelector('.col-nome').textContent = produto.nome;
    linha.querySelector('.col-categoria').textContent = produto.categoria;
    linha.querySelector('.col-preco').textContent = produto.preco_formatado;
    linha.querySelector('.col-estoque').textContent = produto.estoque;
    showToast(`Estoque atualizado: ${produto.nome}`);
}

function removerLinha(produto) {
    const linha = document.querySelector(`tr[data-id="${produto.id}"]`);
    if (linha) linha.remove();
    showToast(`Produto removido: ${produto.nome}`);
}

function criarLinhaProduto(produto, admin) {
    const linha = document.createElement('tr');
    linha.dataset.id = produto.id;
    linha.appendChild(criarCelula(produto.nome, 'col-nome'));
    linha.appendChild(criarCelula(produto.categoria, 'col-categoria'));
    linha.appendChild(criarCelula(produto.preco_formatado, 'col-preco'));
    linha.appendChild(criarCelula(produto.estoque, 'col-estoque'));

    if (admin) {
        linha.appendChild(criarCelulaAcoes(produto));
    }
    return linha;
}

function criarCelula(texto, classe) {
    const celula = document.createElement('td');
    celula.className = classe;
    celula.textContent = texto;
    return celula;
}

function criarCelulaAcoes(produto) {
    const celula = document.createElement('td');

    const linkEditar = document.createElement('a');
    linkEditar.href = `/produtos/${produto.id}/editar`;
    linkEditar.textContent = 'Editar';

    const form = document.createElement('form');
    form.method = 'POST';
    form.action = `/produtos/${produto.id}/excluir`;
    form.className = 'form-excluir';

    const botaoExcluir = document.createElement('button');
    botaoExcluir.type = 'submit';
    botaoExcluir.textContent = 'Excluir';
    form.appendChild(botaoExcluir);

    celula.appendChild(linkEditar);
    celula.appendChild(document.createTextNode(' '));
    celula.appendChild(form);
    return celula;
}
