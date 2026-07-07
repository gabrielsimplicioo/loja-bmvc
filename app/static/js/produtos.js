// interacoes das paginas de produtos (CRUD)

document.addEventListener('DOMContentLoaded', function () {
    document.querySelectorAll('.form-excluir').forEach(function (form) {
        form.addEventListener('submit', function (event) {
            if (!confirm('Remover este produto do catalogo?')) {
                event.preventDefault();
            }
        });
    });
});
