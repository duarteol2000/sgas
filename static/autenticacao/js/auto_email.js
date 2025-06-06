// auto_email.js
document.addEventListener('DOMContentLoaded', function () {
    const tipoInput = document.querySelector('#id_tipo_usuario');
    const usuarioInput = document.querySelector('#id_username');
    const cidadeInput = document.querySelector('#id_cidade'); // preenchido pelo busca_cep.js
    const emailInput = document.querySelector('#id_email');

    function atualizarEmail() {
        const tipo = tipoInput.value;
        const usuario = usuarioInput.value;
        const cidade = cidadeInput.value;

        if (tipo !== 'solicitante' && usuario && cidade) {
            fetch(`localidades/obter-dominio/?cidade=${cidade}`)
                .then(response => response.json())
                .then(data => {
                    if (data.dominio) {
                        emailInput.value = `${usuario}@${data.dominio}`;
                    } else {
                        emailInput.value = '';
                    }
                });
        } else {
            emailInput.value = '';
        }
    }

    tipoInput.addEventListener('change', atualizarEmail);
    usuarioInput.addEventListener('input', atualizarEmail);
    cidadeInput.addEventListener('input', atualizarEmail);
});
