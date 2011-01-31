

function setup_seconds()
{
    var tscale = time_scale();
    document.getElementById('timescale').value = tscale;

    document.getElementById('start_seconds_display').value = 0;
    document.getElementById('pause_seconds_display').value = 0;
    document.getElementById('start_timer').value = 0;
}


function clear_start_timer()
{
    var timer_id = document.getElementById('start_timer_id').value;
    console.log("clearing start timer");
    document.getElementById('start_timer').value = 0;
    clearInterval(timer_id);
}


function stop_start_timer()
{
    var current_value = document.getElementById('start_timer').value;
    console.log("stopping the start timer. current value = " + current_value);
    // doesn't clear the displayed value or the timer value
    // only stops the timer. Need to wait until after 
    // check_and_send to clear the timer (reset to 0)
    var timer_id = document.getElementById('start_timer_id').value;
    clearInterval(timer_id);
}


function get_current_second()
{
    var units = playhead_position();
    var timescale = parseInt(document.getelementById('timescale').value);
    return Math.floor(units/timescale);
}



//interval start 
function increment_start_timer()
{
    var timer = document.getElementById('start_timer').value;
    var timer_value = parseInt(timer);
    var timer_id = document.getElementById('start_timer_id').value;
    console.log("in increment_start_timer with timer #" + timer_id + " " + timer_value);
    timer_value = timer_value + 1;
    document.getElementById('start_timer').value = timer_value;
}


function begin_start_timer(init)
{
    var timer_id = setInterval("increment_start_timer()", 1000);
    console.log("(begin_start_timer) create the start_timer with id = " + timer_id);
    document.getElementById('start_timer_id').value = timer_id;
    console.log("(begin_start_timer) value of init = " + init);

    //var timer_id = document.getElementById('start_timer_id').value;
    document.getElementById('start_timer').value = init;
    var last_start_time = document.getElementById('start_timer').value;    
    
    console.log("(begin_start_timer) start_timer set to = " + last_start_time);
    //increment_start_timer();
}

function set_interval_start()
{
    var start_units = playhead_position();
    document.getElementById('interval_start_units').value = start_units;
    var start = format_time(start_units);
    document.getElementById('interval_start_display').value = start;
    var timescale = document.getElementById('timescale').value;
    var start_seconds = Math.floor(start_units/timescale);
    console.log("(set_interval_start) start_seconds = " + start_seconds);
    document.getElementById('start_seconds_display').value = start_seconds;
    //begin_start_timer();
}

function set_graph(ta_id)
{
    var url = "/view_history/" + parseInt(ta_id) + "/";
    $('#view_graph').load(url);

}


// form to send interval to server
function check_and_send()
{
    var last_start_time = parseInt(document.getElementById('start_seconds_display').value);
    var interval_length = parseInt(document.getElementById('start_timer').value);
    var last_pause = document.getElementById('pause_seconds_display').value;

    /* 
       Note: it's necessary to use parseInt because of the string addition
       that will happen if we dont' convert them to ints first 
    */

    var current_position = playhead_position();
    var timescale = document.getElementById('timescale').value;
    var current_second = Math.floor(current_position/timescale);

    console.log("(check_and_send) last_start_time = " + last_start_time);
    console.log("(check_and_send) interval_length = " + interval_length);
    var last_watched_second = last_start_time + interval_length;
    console.log("(check_and_send) laast_watched_second = " + last_watched_second);
    console.log("(check_and_send) with current_second = " + current_second);        

    // if the latter is true, we need to package 
    // up a new interval and send a message to server
    if ( (last_start_time + interval_length) < current_second) 
	{
	    console.log("passed the if statement....");
	    console.log("--last_start_time = " + last_start_time);
	    console.log("--interval_length = " + interval_length);
	    $.ajax({
		    type:'POST',
			url: "/post_test/",
			data: { iform_start : last_start_time,
			    iform_end : last_pause, 
			    user : document.getElementById('user').value,
			    ta_id : document.getElementById('ta_id').value,
			    },
			success: function(responseData) 
			{
			    // added to modify graph
			    $('.view_graph_div').replaceWith(responseData);
			    console.log(responseData);
			    //alert(responseData);
			},
			dataType: "text"			
			});
	    set_interval_start();
	    begin_start_timer(0);
	}
    else {
	var last_start = document.getElementById('start_timer').value;
	console.log("in check and send, starting the timer again at "+ last_start);
	begin_start_timer(last_start);
    }
    //set_interval_start();
    // start the timers again
}


// interval pause
function set_interval_pause()
{
    var pause_units = playhead_position();
    document.getElementById('interval_pause_units').value = pause_units;
    var pause = format_time(pause_units);
    document.getElementById('interval_pause_display').value = pause;
    var timescale = document.getElementById('timescale').value;
    var pause_seconds = Math.floor(pause_units/timescale);
    console.log("(set_interval_pause) pause_seconds = " + pause_seconds);

    document.getElementById('pause_seconds_display').value = pause_seconds;
    stop_start_timer();
}


/*
// interval skip
function set_interval_skip()
{
    var skip_units = playhead_position();
    document.getElementById('interval_skip_units').value = skip_units;
    var skip = format_time(skip_units);
    document.getElementById('interval_skip_display').value = skip;
    var timescale = document.getElementById('timescale').value;
    var skip_seconds = Math.floor(skip_units/timescale);
    document.getElementById('skip_seconds_display').value = skip_seconds;
}



// set seconds
function set_seconds()
{
    var timescale = document.getElementById('timescale').value;
    
    var start_units = document.getElementById('interval_start_units').value;
    var start_seconds = Math.floor(start_units/timescale);
    document.getElementById('start_seconds_display').value = start_seconds;
    
    var pause_units = document.getElementById('interval_pause_units').value;
    var pause_seconds = Math.floor(pause_units/timescale);
    document.getElementById('pause_seconds_display').value = pause_seconds;
    
    var skip_units = document.getElementById('interval_skip_units').value;
    var skip_seconds = Math.floor(skip_units/timescale);
    document.getElementById('skip_seconds_display').value = skip_seconds;
}
*/