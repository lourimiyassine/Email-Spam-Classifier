function onClickedEstimate() {
  var email = document.getElementById("email").value; // Récupérer la valeur de l'input
  var url = "http://127.0.0.1:5000/predict";

  $.post(url, { email: email })
      .done(function(response) {
          // Afficher le résultat dans l'élément avec l'id 'uiEstimated'
          document.getElementById("uiEstimated").innerHTML = "<h2>" + response + "</h2>";
      })
      .fail(function(xhr) {
          // Gérer les erreurs
          console.error(xhr); // Afficher l'objet xhr pour le débogage
          document.getElementById("uiEstimated").innerHTML = "<h2>Erreur: " + xhr.responseText + "</h2>";
      });
}