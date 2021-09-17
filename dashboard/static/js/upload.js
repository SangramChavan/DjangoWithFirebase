$(document).ready(function () {

    // $('#form').submit(function (e) {
    //     e.preventDefault();

    //     var formData = new FormData();
    //     var files = $('#id_image')[0].files[0]

    //     console.log(files);

    // });
    $('#id_image').change(function (e) {
        e.preventDefault();

        var formData = new FormData();
        var files = $('#id_image')[0].files[0];

        console.log(files);
    });
});




