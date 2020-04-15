<script type="text/javascript">
	function call() {
	  var msg   = $('#formx').serialize();
       $.ajax({
         type: 'POST',
         url: 'formx.php', //обращаемся к обработчику
         data: msg,
        success: function(data) {  //в случае успеха выводим результаты в div "results"
            $('#formx').remove(); //скрываем форму после отправки 
			$('#results').html(data); //показываем сообщение об успехе вместо неё 

         },
         error:  function(xhr, str){ //ошибка выводит соответствующее сообщение 
	    alert('Возникла ошибка: ' + xhr.responseCode);
         }
       });
   }
</script>