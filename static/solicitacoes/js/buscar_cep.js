function buscarCep() {
    const cepInput = document.querySelector("input[name='cep']");

    if (!cepInput) {
        alert("Campo de CEP não encontrado.");
        return;
    }

    const cep = cepInput.value.replace(/\D/g, '');  // remove traços e letras

    if (cep.length !== 8) {
        alert("CEP inválido. Deve conter 8 dígitos.");
        return;
    }

    fetch(`https://viacep.com.br/ws/${cep}/json/`)
        .then(response => response.json())
        .then(data => {
            if (data.erro) {
                alert("CEP não encontrado.");
                return;
            }

            document.querySelector("input[name='logradouro']").value = data.logradouro || '';
            document.querySelector("input[name='bairro']").value = data.bairro || '';
            document.querySelector("input[name='cidade']").value = data.localidade || '';
            document.querySelector("input[name='estado']").value = data.uf || '';
        })
        .catch(error => {
            console.error("Erro ao buscar CEP:", error);
            alert("Erro ao buscar o CEP. Tente novamente.");
        });
}
