// um ouvinte de evento é para o DomContentLoaded, que é acionado quando o Html é carregado
document.addEventListener("DOMContentLoaded", function() {
    // busca os elementos coma a classe alert que é a classe das mensagens de alertas exibidas na tela
    var alertMessages = document.querySelectorAll(".alert");

    // o forEach vai iterar sobre todos os elementos do array que é a classe alert
    alertMessages.forEach(function(alertMessage) {
        // função que vai remover a messagem de alerta após 5 segundos
        setTimeout(function() {
            alertMessage.remove();
        }, 5000); // 5000 milissegundos = 5 segundos
    });
});