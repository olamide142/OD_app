
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
  $("#follow_button").click(function(){
        var action = this.innerHTML.trim();
//        action = action.trim()
        console.log(action);
        var following = $("#profile_owner").text();
        //    csrfToken since am sending a post request
        var csrftoken = getCookie('csrftoken');

         $.ajax({
                type: 'POST',
                data: {'action':action, 'csrfmiddlewaretoken':csrftoken, 'following':following},
                url: '/ajax/follow/',
                dataType: 'json',
                success: function (data) {
                    if(action == 'Follow'){
                        $("#follow_button").text('Unfollow');
                        var x = $("#fol_me").text();
                        $("#fol_me").text(x.trim() - 1+2);
                    }else{
                        $("#follow_button").text('Follow');
                        var x = $("#fol_me").text();
                        $("#fol_me").text(x.trim() - 1);
                    }
                }
        });
    });

});


function get_follows(){

}