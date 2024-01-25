window.onload = function() {
    $.ajax({
        
        url: "{% url 'show_data' %}",

        success: function(result) {
            console.log(result);
            alert('Data Saved Successfully.');
            
        },

        error: function(result) {
            console.log(result);
            alert('Data Saved Successfully!!!!.');
        }
    });
};



$(document).ready(function () {
    var first = "{{first}}";
    console.log(first);
    $('#red',).click(function () {
        // создаем AJAX-вызов
        $.ajax({
            data: {
                'level': 'Hard',
                'project': first,
            }, // получаяем данные формы
            url: "{% url 'show_data' %}",
            // если успешно, то
            success: function (response) {
                console.log(response.problems);
                $('#problems').html(response.problems);
            },
            // если ошибка, то
            error: function (response) {
                // предупредим об ошибке
                console.log(response.responseJSON.errors)
            }
        });
        return false;
});

$('#yellow',).click(function () {
        // создаем AJAX-вызов
        $.ajax({
            data: {
                'level': 'Medium',
                'project': first,
            }, // получаяем данные формы
            url: "{% url 'show_data' %}",
            // если успешно, то
            success: function (response) {
                console.log(response);
                $('#problems').replaceWith(response);
            },
            // если ошибка, то
            error: function (response) {
                // предупредим об ошибке
                console.log(response.responseJSON.errors)
            }
        });
        return false;
});


$('#green',).click(function () {
        // создаем AJAX-вызов
        $.ajax({
            data: {
                'level': 'Easy',
                'project': first,
            }, // получаяем данные формы
            url: "{% url 'show_data' %}",
            // если успешно, то
            success: function (response) {
                console.log(response.problems);
                $('#problems').html(response.problems);
            },
            // если ошибка, то
            error: function (response) {
                // предупредим об ошибке
                console.log(response.responseJSON.errors)
            }
        });
        return false;
});
})


