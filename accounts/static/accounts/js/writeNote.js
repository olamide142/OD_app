
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
            $("#post_tray").prepend(data.post_id);
//            $("#writeNote").attr("aria-hidden", "false");
            alert("Success");
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

