// interacoes da pagina de login

document.addEventListener('DOMContentLoaded', function () {
    const campoSenha = document.getElementById('senha');
    const botaoAlternar = document.getElementById('alternar-senha');
    if (!campoSenha || !botaoAlternar) return;

    botaoAlternar.addEventListener('click', function () {
        const senhaVisivel = campoSenha.type === 'text';
        campoSenha.type = senhaVisivel ? 'password' : 'text';
        botaoAlternar.textContent = senhaVisivel ? 'Mostrar' : 'Ocultar';
    });
});
