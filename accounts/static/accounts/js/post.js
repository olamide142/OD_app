function deleteNote(post_id){
    $(document).ready(function(){
        $(post_id).fadeOut("2000");
        //    csrfToken since am sending a post request
        var csrftoken = getCookie('csrftoken');

         $.ajax({
            type: 'POST',
            data: {'note_id':post_id, 'csrfmiddlewaretoken':csrftoken},
            url: '/ajax/deleteNote/',
            dataType: 'json',
            success: function (data) {
                alert("Success");
            }
         });
    });
}

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}