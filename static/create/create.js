$(document).ready(function(){
    if($('#table') != null){
        Read();
    }

    $('#create2').on('click', function () {
        var subcategory = $('#subcategory').val();
        // console.log(category);
       
        var product = $('#product').val();
        var price = $('#price').val();
        var nameRegex = /^[a-zA-Z]+(([',. -][a-zA-Z ])?[a-zA-Z]*)*$/;

        // if (category.trim() == "" || product_name.trim() == "") {
        //     alert("Please complete the required field");
        // } else 
        if (!nameRegex.test(product)) {
        //     alert("please compleate the required fields");
        }
         else {
            $.ajax({
                url: 'create_product',
                type: 'POST',
                data: {
                    subcategory: subcategory,
                    product: product,
                    price:price,

                    csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
                },
                success: function () {
                    Read();
                    $('#subcategory').val('');
                    $('#product').val('');
                    $('#price').val('');
                    alert("New Product Successfully Added");
                }
            });
        }
    });    

    function Read() {
        $.ajax({
            async: true,
            url: 'view',
            type: 'POST',



            data: {
                res: 1,
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
            },
            success: function (response) {
                $('#table').html(response);
            }
        });
    }
});