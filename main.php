<html>
  <head>
    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>git 
    <script>
      function predictImage() {
        var image = $('#image').get(0).files[0];
        var formData = new FormData();
        formData.append('image', image);

        $.ajax({
          url: '/predict',
          type: 'POST',
          data: formData,
          processData: false,
          contentType: false,
          success: function(response) {
            $('#prediction').text(response.prediction);
          }
        });
      }
      
    </script>
  </head>
  <body>
    <input type="file" id="image">
    <button onclick="predictImage()">Predict</button>
    <br>
    <span id="prediction"></span>
  </body>
</html>
