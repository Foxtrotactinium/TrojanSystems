    $(document).ready(function(){
      $('table tr').click(function(){
        window.location = $(this).data('href');
        print(request)
        return false;
      });
    });