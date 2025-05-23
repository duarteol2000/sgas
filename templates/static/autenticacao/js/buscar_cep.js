document.addEventListener("DOMContentLoaded", function () {
    const cepInput = document.querySelector("input[name='cep']");
    const tipoLogradouroInput = document.querySelector("input[name='tipo_logradouro']");
    const logradouroInput = document.querySelector("input[name='logradouro']");
    const cidadeInput = document.querySelector("input[name='cidade']");
    const ufInput = document.querySelector("input[name='uf']");

    if (!cepInput) return;

    cepInput.addEventListener("blur", function () {
        const cep = cepInput.value.replace(/\D/g, '');
        
        if (cep.length === 8) {
            fetch(`https://viacep.com.br/ws/${cep}/json/`)
                .then(response => response.json())
                .then(data => {
                    console.log("Dados retornados da API:", data);  // <-- Aqui

                    if (!data.erro) {
                        const logradouroCompleto = data.logradouro || "";
                        const partes = logradouroCompleto.split(" ");
                        const tipo = partes.shift() || "";
                        const nomeLogradouro = partes.join(" ");

                        if (tipoLogradouroInput) tipoLogradouroInput.value = tipo;
                        if (logradouroInput) logradouroInput.value = nomeLogradouro;
                        if (cidadeInput) cidadeInput.value = data.localidade || "";
                        if (ufInput) ufInput.value = data.uf || "";

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
});
