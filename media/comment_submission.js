


function change_favorite()
{
    console.log("in change_favorite");
    var username = $('input[name=username]').val();
    console.log("username");
    var ta_id = $('input[name=ta_id]').val();
    console.log("ta_id");
    var button_value = $('input[name=submit_favorite]').val();
    var is_favorite = true;
    $.ajax({    type: 'POST',
		url: "/add_favorite/",
		data: { username: username, ta_id: ta_id, button_value: button_value },
		dataType: "json",
		success: function(response)
		{
		    document.getElementById('submit_favorite').value = response.new_button_text;
		},
		/*success: function(response)
		{
		    $('#favorite_div').load('favorite_button.html #favorite_div');
		    }*/
		});
 
}

function submit_comment()
{
    var username = $('input[name=username]').val();
    var ta_id = $('input[name=ta_id]').val();
    var text = $('textarea[name=text]').val();
    var permissions = $('select[name=permissions]').val();
    console.log("in submit_comment");
    console.log("username = " + username + ", permissions = " + permissions + ", ta_id = " + ta_id + ", text = " + text);
    $.ajax({    type: 'POST',
		url: "/comment_update/",
		data: { username : username,
		        text : text,
		        permissions : permissions,
		        ta_id : ta_id, },
		success: function(response){
		//console.log("in success function");
		    var new_comment = "<tr><td colsapn=\"2\">" + response.text + "<br/> --" + response.username + " at " + response.time +"</td></tr>";
		    $('.comment_display').append(new_comment);
	        },
		dataType: "json",
		});
    return false;
    // this is supposed to prevent the default submission behavior
}