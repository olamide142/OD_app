

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


$(document).ready(function(){
  $("button").click(function(){

//    check if the button clicked was a delete button
    var note_id = this.id;
    if (note_id.search('delete_') != -1){
//        Remove the substring 'delete_' to get the ID of post
        note_id = note_id.replace('delete_','');
    //    csrfToken since am sending a post request
        var csrftoken = getCookie('csrftoken');

        $.ajax({
                type: 'POST',
                data: {'note_id':note_id, 'csrfmiddlewaretoken':csrftoken},
                url: '/ajax/deleteNote/',
                dataType: 'json',
                success: function (data) {
                    console.log("Success");
        //        Make the post <div> FadeOut
                  $("#"+note_id).fadeOut(2000);
        //        Update Diary note length in profile section
//                  var diary_note_length = parseInt($("#diary_note_length").text());
//                  diary_note_length -= 1;
//                  $("#diary_note_length").text(''+diary_note_length);

                }
        });
    }
  });
});

