var current_tab_opened;
var page_count = 1;

function openFollows(cityName) {
  var i;
  current_tab_opened = cityName;
  page_count = 1;
  var x = document.getElementsByClassName("city");
  for (i = 0; i < x.length; i++) {
    x[i].style.display = "none";
  }
  document.getElementById(cityName).style.display = "block";
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


$(document).ready(function(){
    var username = $("#profile_owner").text();
    var page = page_count;

//        if more button was clicked increase the page number by 1
    $("#more_follows_btn").click(function(){
       page_count  += 1;
    });

    $("button").click(function(){
        if(current_tab_opened == "Following"){
            var type = "Following";
        }else if(current_tab_opened == "Followers"){
            var type = "Followers";
        }

            $.ajax({
                    type: 'GET',
                    data: {'username':username, 'type':type, 'page':page_count},
                    url: '/ajax/get_follows/',
                    dataType: 'json',
                    success: function (data) {
                        if(current_tab_opened == 'Followers'){
                            $('#followers_list').append('<li class="list-group-item">'+data.return_list+'</li>');
                        }else if (current_tab_opened == 'Following'){
                            $('#following_list').append('<li class="list-group-item">'+data.return_list+'</li>');
                        }
                    }
            });
    });


//    Code that tells if there is more Accounts to be added
//    to the follows list so as to display a [More] button
//    or stop displaying

});

function more_follows_button_clicked(){
        $("#more_follows_btn").click(function(){
            if ( $('#followers_list li').length == $('#fol_me').text() ) {
                $("#more_follows_btn").hide();
            }
            if ( $('#following_list li').length == $('#am_f').text() ) {
                $("#more_follows_btn").hide();
            }
        });
    }
