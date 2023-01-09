// scripts.js
$(document).ready(function() {
  // Send an HTTP GET request to the Python server
  $.get('http://localhost:5000/', function(response) {
    // Display the image in the page
    $('#image').html('<img src="data:image/png;base64,' + response + '"/>');
  });
});
