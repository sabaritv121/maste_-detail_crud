$(document).ready(function(){
    if($('#res') != null){
        Read();
    }

// $('#create1').on('click', function(){
//     var name = $('#name').val();
//     var nameRegex = /^[a-zA-Z]+(([',. -][a-zA-Z ])?[a-zA-Z]*)*$/;

//     if(name.trim() == "") {
//         alert("Please complete the required field");
//     } else if (!nameRegex.test(name)) {
//         alert("Name can only contain letters and spaces");
//     } else {
//         $.ajax({
//             url: 'create_project/',
//             type: 'POST',
//             data: {
//                 name: name,
//                 csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
//             },
//             success: function(){
//                 Read();
//                 $('#name').val('');
//                 alert("New Category Successfully Added");
//             }
//         });
//     }
// });
    

// function Read(){
//     $.ajax({
//         async: true,
//         url: 'read/',
//         type: 'POST',

//         data:{
//             res: 1,
//             csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
//         },
//         success: function(response){
//             $('#res').html(response);
//         }
//     });
// }



// 


// $(document).ready(function () {
//     if ($('#res').length) {
//         Read();
//     }

    $('#create1').on('click', function () {
        var category = $('#category').val();
        console.log(category);
       
        var product_name = $('#product_name').val();
        var nameRegex = /^[a-zA-Z]+(([',. -][a-zA-Z ])?[a-zA-Z]*)*$/;

        // if (category.trim() == "" || product_name.trim() == "") {
        //     alert("Please complete the required field");
        // } else 
        if (!nameRegex.test(product_name)) {
            alert("please compleate the required fields");
        } else {
            $.ajax({
                url: 'create_project',
                type: 'POST',
                data: {
                    category: category,
                    product_name: product_name,
                    csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
                },
                success: function () {
                    Read();
                    $('#category').val('');
                    $('#product_name').val('');
                    alert("New Category Successfully Added");
                }
            });
        }
    });

    // $(document).on('click', '.edit', function () {
    //     var id = $(this).attr('name');
    //     window.location = "edit/" + id;
    // });

    // $(document).on('click', '.user-edit', function () {
    //     console.log("updateddddddd");
    //     var category = $('#category').val();
    //     var project_name = $('#project_name').val();
    //     var nameRegex = /^[a-zA-Z]+(([',. -][a-zA-Z ])?[a-zA-Z]*)*$/;

    //     if (category.trim() == "" || project_name.trim() == "") {
    //         alert("Please complete the required field");
    //     } else if (!nameRegex.test(category) || !nameRegex.test(project_name)) {
    //         alert("Name can only contain letters and spaces");
    //     } else {
    //         var id = $('#member_id').val();
    //         $.ajax({
    //             url: 'update_project_subcategory/' + id,
    //             type: 'POST',
    //             data: {
    //                 category: category,
    //                 project_name: project_name,
    //                 csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
    //             },
    //             success: function () {
    //                 alert('Updated!');
    //                 window.location = '/index';
    //             }
    //         });
    //     }
    // });

    // $(document).on('click', '.toggle-active-btn', function () {
    //     var project_subcategory_id = $(this).data('projectcategory-id');
    //     var csrf_token = $(this).data('csrf-token');

    //     $.ajax({
    //         url: '/projectcategory/' + project_subcategory_id + '/toggle-active/',
    //         method: 'POST',
    //         data: {
    //             'csrfmiddlewaretoken': csrf_token
    //         },
    //         success: function (response) {
    //             if (response.status === 'success') {
    //                 $('.toggle-active-btn[data-projectcategory-id=' + project_subcategory_id + ']').text(response.is_active ? 'Disable' : 'Enable');
    //             } else {
    //                 alert(response.message);
    //             }
    //         },
    //         error: function (xhr, status, error) {
    //             console.log('Error:', error);
    //         }
    //     });
    // });

    // $(document).on('click', '.delete', function () {
    //     var id = $(this).attr('name');
    //     $.ajax({
    //         url: 'delete_project_subcategory/' + id,
    //         type: 'POST',
    //         data: {
    //             csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
    //         },
    //         success: function () {
    //             Read();
    //             alert("Deleted!");
    //         }
    //     });
    // });

   

    function Read() {
        $.ajax({
            async: true,
            url: 'read1',
            type: 'POST',



            data: {
                res: 1,
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
            },
            success: function (response) {
                $('#res').html(response);
            }
        });
    }
});



