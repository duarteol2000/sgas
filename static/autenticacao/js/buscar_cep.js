document.addEventListener("DOMContentLoaded", function () {
    const cepInput = document.querySelector("input[name='cep']");
    const tipoLogradouroInput = document.querySelector("input[name='tipo_logradouro']");
    const logradouroInput = document.querySelector("input[name='logradouro']");
    const cidadeInput = document.querySelector("input[name='cidade']");
    const bairroInput = document.querySelector("input[name='bairro']");
    const ufInput = document.querySelector("input[name='uf']");

    if (!cepInput) return;

    cepInput.addEventListener("blur", function () {
        const cep = cepInput.value.replace(/\D/g, '');
        
        if (cep.length === 8) {
            fetch(`https://viacep.com.br/ws/${cep}/json/`)
                .then(response => response.json())
                .then(data => {
                    console.log("Dados retornados da API:", data);

                    if (!data.erro) {
                        const logradouroCompleto = data.logradouro || "";
                        const partes = logradouroCompleto.split(" ");
                        const tipo = partes.shift() || "";
                        const nomeLogradouro = partes.join(" ");
                        const bairro = data.bairro || "";

                        if (tipoLogradouroInput) tipoLogradouroInput.value = tipo;
                        if (logradouroInput) logradouroInput.value = nomeLogradouro;
                        if (cidadeInput) {
                            cidadeInput.value = data.localidade || "";

                            // 👇 Chama a função de preenchimento do e-mail institucional
                            atualizarEmailInstitucional();
                        }
                        if (ufInput) ufInput.value = data.uf || "";
                        if (bairroInput) {
                            bairroInput.value = bairro;
                        } else {
                            console.warn("⚠️ Campo 'bairro' não encontrado.");
                        }
                    } else {
                        alert("CEP não encontrado.");
                    }
                })
                .catch(error => {
                    console.error("Erro ao buscar CEP:", error);
                    alert("Erro ao buscar o CEP. Tente novamente.");
                });
        } else {
            alert("Por favor, insira um CEP válido com 8 números.");
        }
    });

    // 🔄 Evento manual (caso o usuário mude a cidade manualmente)
    document.querySelector('#cidade').addEventListener('change', atualizarEmailInstitucional);
});

// ✅ Função isolada para reutilizar no blur e no change
function atualizarEmailInstitucional() {
    const cidade = document.querySelector('#cidade').value;
    const tipoUsuario = document.querySelector('#tipo_usuario').value;

    if (cidade && tipoUsuario !== 'solicitante') {
        fetch(`/localidades/buscar-dominio/?cidade=${cidade}`)
            .then(response => response.json())
            .then(data => {
                if (data.dominio) {
                    const usuario = document.querySelector('#usuario').value;
                    document.querySelector('#email').value = `${usuario}@${data.dominio}`;
                }
            });
    }
}
