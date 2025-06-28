$(document).ready(function() {
    $('.sidebar a').click(function(event) {
      event.preventDefault(); // evita que o link seja carregado normalmente
  
      var arquivo = $(this).data('arquivo'); // obtém o arquivo a carregar
      $('#conteudo').load(arquivo); // carrega o arquivo no elemento de conteúdo
    });
});

