$(document).ready(function(){
    if($('#result') != null){
        Read();
    }

$('#create').on('click', function(){
    var name = $('#name').val();
    var nameRegex = /^[a-zA-Z]+(([',. -][a-zA-Z ])?[a-zA-Z]*)*$/;

    if(name.trim() == "") {
        alert("Please complete the required field");
    } else if (!nameRegex.test(name)) {
        alert("Name can only contain letters and spaces");
    } else {
        $.ajax({
            url: 'create/',
            type: 'POST',
            data: {
                name: name,
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
            },
            success: function(){
                Read();
                $('#name').val('');
                alert("New Category Successfully Added");
            }
        });
    }
});
    $(document).on('click', '.edit', function(){
        $id = $(this).attr('name');
        window.location = "edit/" + $id;
    });
//$(document).on('click', '.edit', function(){
//    var id = $(this).attr('name');
//
//    // Send AJAX request to get the edit form HTML
//    $.ajax({
//        url: 'edit/' + id,
//        type: 'GET',
//        success: function(response){
//            // Replace the content of the current page with the edit form HTML
//            $('body').html(response);
//        }
//    });
//});
//


     $('#update').on('click', function(){
    var name = $('#name').val();
    var nameRegex = /^[a-zA-Z]+(([',. -][a-zA-Z ])?[a-zA-Z]*)*$/;

    if(name.trim() == "") {
        alert("Please complete the required field");
    } else if (!nameRegex.test(name)) {
        alert("Name can only contain letters and spaces");
    } else {
        var id = $('#member_id').val();
        $.ajax({
            url: 'update/' + id,
            type: 'POST',
            data: {
                name: name,
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
            },
            success: function(){
                window.location = '/index';
                alert('Updated!');
            }
        });
    }
});



    $(document).on('click', '.delete', function(){
        $id = $(this).attr('name');
        $.ajax({
            url: 'delete/' + $id,
            type: 'POST',
            data: {
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
            },
            success: function(){
                Read();
                alert("Deleted!");
            }
        });
    });

});





function Read(){
    $.ajax({
        async: true,
        url: 'read/',
        type: 'POST',

        data:{
            res: 1,
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
        },
        success: function(response){
            $('#result').html(response);
        }
    });
}


   



