$(document).ready(function(){
  $('[data-href]').click(function(){
    window.location = $(this).data('href');
    return false;
  });

$('[data-id]').click(function(){
   $("#id_partsrequired").val($(this).data('id'));
});



