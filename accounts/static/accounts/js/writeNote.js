
$(document).ready(function(){
  $("#post_btn").click(function(){
    //  note gotten from textarea
    var note = document.getElementById("message-text").value;
//    csrfToken since am sending a post request
    var csrftoken = getCookie('csrftoken');

    $.ajax({
        type: 'POST',
        data: {'note':note, 'csrfmiddlewaretoken':csrftoken},
        url: '/ajax/addNote/',
        dataType: 'json',
        success: function (data) {
            prepend_new_note_to_top_of_post_tray(id=data.post_id, body=data.body);
//            $("#writeNote").attr("aria-hidden", "false");
            console.log("Success");
        }
    });
  });
});



  maxL = 200;
  var bName = navigator.appName;

  function taLimit(taObj) {
    if (taObj.value.length == maxL) return false;
    return true;
  }

  function taCount(taObj, Cnt) {
    objCnt = createObject(Cnt);
    objVal = taObj.value;
    if (objVal.length > maxL) objVal = objVal.substring(0, maxL);
    if (objCnt) {
      if (bName == "Netscape") {
        objCnt.textContent = maxL - objVal.length;
      } else {
        objCnt.innerText = maxL - objVal.length;
      }
    }
    return true;
  }

  function createObject(objId) {
    if (document.getElementById) return document.getElementById(objId);
    else if (document.layers) return eval("document." + objId);
    else if (document.all) return eval("document.all." + objId);
    else return eval("document." + objId);
  } //End Count content



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



function prepend_new_note_to_top_of_post_tray(id, body){
//Ok calm down lams i see you came back
//to read this code. This is exactly what you
//were trying to do
//>>  when a user is on his profie page
//    and he writes a note, this function is to
//    run after ajax submition was successful.
//    the job of the function is to clone an empty
//    div that contains the template for how a note
//    would appear, after cloning into a variable
//    it prepends that new note <div> into the post_tray
//    (thats the board with all the posts... i hope that made sense
//    if it doesn't just write it all over or blow your brains out)

     $temp1 = $('#temp').clone();
//     change the id from temp to the post_id that was returned with the ajax response
     $temp1.attr("id", id);
//     make the div display
     $temp1.addClass("w3-show");
//     Set the id of all child element
      $temp1.children()[2].innerText = 'just now';
      $temp1.children()[5].innerText = body;
      $temp1.children()[8].id = 'delete_'+id;
     $temp1.prependTo('#post_tray');

}




function delete_note(id){
    del_id = this.id;
    var note_id = "delete_"+this.id;
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
        //        Make the post <div> FadeOut
                  $("#"+del_id).fadeOut(500);
                  console.log("Success");
        //        Update Diary note length in profile section
                  var diary_note_length = Number($("#diary_note_length").text());
                  diary_note_length -= 1;
                  $("#diary_note_length").text(''+diary_note_length);

                }
        });
    }
}