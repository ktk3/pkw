function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

$(document).ready(function() {
    $("button.ajax-save").hide();
    $("button.ajax-cancel").hide();
    $("input.karty-edit").hide();
    $("input.wyborcy-edit").hide();

    $("button.ajax-edit").click(function() {
        var okr_id = $(this).parent().parent().attr('id');
        $("#" + okr_id).find("button.ajax-save").show();
        $("#" + okr_id).find("button.ajax-cancel").show();
        $(this).hide();
        $("#" + okr_id).find("input.wyborcy-edit").show();        
        $("#" + okr_id).find("input.karty-edit").show();
        $("#" + okr_id).find("span").hide();
        var czas;
        $.post('/ajax/update', {'okr_id': okr_id, 'csrfmiddlewaretoken': getCookie('csrftoken')}, function(data) {
            $("#" + okr_id).find("input.wyborcy-edit").val(data.wyborcy);
            $("#" + okr_id).find("input.karty-edit").val(data.karty);
            czas = data.czas;
            $("#" + okr_id + "-czas").val(czas);
        });

    });
    $("button.ajax-cancel").click(function() {
        var okr_id = $(this).parent().parent().attr('id');
        $("#" + okr_id).find("button.ajax-save").hide();
        $("#" + okr_id).find("button.ajax-edit").show();
        $(this).hide();
        $("#" + okr_id).find("input.wyborcy-edit").hide();        
        $("#" + okr_id).find("input.karty-edit").hide();
        $("#" + okr_id).find("span").show();
    });

    $("button.ajax-save").click(function() {
        var okr_id = $(this).parent().parent().attr('id');
        var czas = $("#" + okr_id + "-czas").val();
        var wyborcy = $("#" + okr_id).find("input.wyborcy-edit").val();
        var karty = $("#" + okr_id).find("input.karty-edit").val();
        $.post('/ajax/save', {
                'okr_id': okr_id, 
                'karty' : karty,
                'czas' : czas,
                'wyborcy' : wyborcy,
                'csrfmiddlewaretoken': getCookie('csrftoken')}, 
                function(data) {
            // $('#current-price').text(data);
            // if (parseInt(price) < parseInt(data)) {
            //     alert('Podbita cena mniejsza niż obecna.');
            // }
            $("#" + okr_id).find("span.karty-view").text(data.karty);
            $("#" + okr_id).find("span.wyborcy-view").text(data.wyborcy);
            if (data.error){
                alert(data.error);
            }
            console.log(JSON.stringify(data));
        });  
        $("#" + okr_id).find("button.ajax-cancel").hide();
        $("#" + okr_id).find("button.ajax-edit").show();
        $(this).hide();
        $("#" + okr_id).find("input.wyborcy-edit").hide();        
        $("#" + okr_id).find("input.karty-edit").hide();
        $("#" + okr_id).find("span").show();
        
    });

    $('#bid').click(function() {
        var price = $('#price').val();
        $.post('/ajax/bid/', {'price': price, 'csrfmiddlewaretoken': getCookie('csrftoken')}, function(data) {
            $('#current-price').text(data);
            if (parseInt(price) < parseInt(data)) {
                alert('Podbita cena mniejsza niż obecna.');
            }
        });
    });
});

