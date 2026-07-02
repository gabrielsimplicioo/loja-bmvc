// interacoes da pagina inicial

document.addEventListener('DOMContentLoaded', function () {
    startClock();
    setupNewsletterForm();
});

function startClock() {
    const clockEl = document.getElementById('clock');
    if (!clockEl) return;

    function tick() {
        const now = new Date();
        clockEl.textContent = now.toLocaleTimeString('pt-BR');
    }

    tick();
    setInterval(tick, 1000);
}

function setupNewsletterForm() {
    const form = document.getElementById('newsletter-form');
    if (!form) return;

    form.addEventListener('submit', function (event) {
        event.preventDefault();
        const emailInput = document.getElementById('newsletter-email');
        const email = emailInput.value.trim();

        if (!email) {
            showToast('Informe um e-mail valido.');
            return;
        }

        showToast(`Inscricao confirmada para ${email}!`);
        form.reset();
    });
}

function showToast(message) {
    let toast = document.getElementById('toast');
    if (!toast) {
        toast = document.createElement('div');
        toast.id = 'toast';
        toast.className = 'toast';
        document.body.appendChild(toast);
    }

    toast.textContent = message;
    toast.classList.add('show');

    clearTimeout(showToast._timer);
    showToast._timer = setTimeout(() => {
        toast.classList.remove('show');
    }, 2500);
}
