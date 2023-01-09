// scripts.js
$(document).ready(function() {
  // Submit the form when the button is clicked
  $('#image-form').submit(function(event) {
    // Prevent the form from being submitted
    event.preventDefault();
    
    // Get the selected image type
    var imageType = $('#image-type').val();
    
    // Send an HTTP POST request to the Python server
    $.post('http://localhost:5000/', {type: imageType}, function(response) {
      //
