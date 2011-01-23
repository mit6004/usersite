  
function set_time_scale()
{
    var tscale = time_scale();
    document.getElementById('timescale').value = tscale;
}

function setup_start_timer()
{
    document.getElementById('start_timer').value = 0;
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
    document.getElementById('debug').value = "increment_start_timer";
    var timer_value = parseInt(document.getElementById('start_timer').value);
    timer_value = timer_value + 1;
    document.getElementById('start_timer').value = timer_value;
}

function set_start_timer_id_display()
{
    var timer_id = document.getElementById('start_timer_id').value;
    document.getElementById('start_timer_id_display').value = timer_id;
}

function begin_start_timer()
{
    document.getElementById('debug').value = "begin_Start_timer";
    var last_start_time = document.getElementById('start_timer').value;
    var timer_id = setInterval("increment_start_timer()", 1000);
    document.getElementById('start_timer_id').value = timer_id;
    set_start_timer_id_display();
}

function set_start_seconds()
{
    var timescale = document.getElementById('timescale').value;
    var start_units = document.getElementById('interval_start_units').value;
    var start_seconds = Math.floor(start_units/timescale);
    document.getElementById('start_seconds_display').value = start_seconds;
    begin_start_timer();
}

function set_interval_start_display()
{
    var start_units = playhead_position();
    var start = format_time(start_units);
    document.getElementById('interval_start_display').value = start;
    set_start_seconds();
}

function set_interval_start_units()
{
    var start_units = playhead_position();
    document.getElementById('interval_start_units').value = start_units;
    set_interval_start_display();
}



//helper function to add elements to the form
function createNewFormElement(inputForm, elementName, elementValue)
{
    document.getElementById('debug2').value = "in createNewFormElemet";
    document.getElementById('debug2').value = "in createNewFormElemet22";
    inputForm.appendChild(newElement);
    newElement.value = elementValue;
    return newElement;
}

// form to send interval to server
function check_and_send()
{
    var user = document.getElementById('user').value;
    var ta_id = document.getElementById('ta_id').value;

    document.getElementById('debug2').value = "in check and send";
    var last_start_time = document.getElementById('start_seconds_display').value;
    var interval_length = document.getElementById('start_timer').value;
    var skipped_to = document.getElementById('skip_seconds_display').value;
    var last_pause = document.getElementById('pause_seconds_display').value;

    var current_position = playhead_position();
    var timescale = document.getElementById('timescale').value;
    var current_second = Math.floor(current_position/timescale);
    document.getElementById('debug2').value = "current_second = " + current_second;
    
    // if the latter is true, we need to package 
    // up a new interval and send a message to server
    if ( last_pause < skipped_to )
	{
	    document.getElementById('debug2').value = "last_start_time < current";
	    //createNewFormElement(form, "start_time", last_start_time);
	    document.getElementById('iform_start_time').value = last_start_time;
	    document.getElementById('iform_end_time').value = last_pause;
	    document.getElementById('debug2').value = 
		"added start time as " + document.getElementById('iform_start_time').value;
	    /*
	    $.post("/post_test/", 
		   { iform_start_time : last_start_time, iform_end_time : last_pause } );
	    */
	    $('#iform').submit(function(event){
		    event.preventDefault();
		    var iform = this;
		    var data = {};
		    data.iform_start = $(iform).find('input[@name = iform_start_time]').val();
		    data.iform_end = $(iform).find('input[@name = iform_end_time]').val();
		    
		    $.post("/post_test/",
			   data,
			   function(responseData) {
			       alert(responseData.response_text);
			   },			
			   "json"
			   );
		});
	    $('#iform').submit();
	}
}


// interval pause
function clear_start_timer()
{
    var timer_id = document.getElementById('start_timer_id').value;
    document.getElementById('start_timer').value = 0;
    document.getElementById('debug').value = "clearing start timer";
    clearInterval(timer_id);
}

function set_pause_seconds()
{
    var timescale = document.getElementById('timescale').value;
    var pause_units = document.getElementById('interval_pause_units').value;
    var pause_seconds = Math.floor(pause_units/timescale);
    document.getElementById('pause_seconds_display').value = pause_seconds;
    clear_start_timer();
}  

function set_interval_pause_display()
{
    var pause_units = playhead_position();
    var pause = format_time(pause_units);
    document.getElementById('interval_pause_display').value = pause;
    set_pause_seconds();
}

function set_interval_pause_units()
{
    var pause_units = playhead_position();
    document.getElementById('interval_pause_units').value = pause_units;
    set_interval_pause_display();
}

// interval skip
function set_skip_seconds()
{
    var timescale = document.getElementById('timescale').value;
    var skip_units = document.getElementById('interval_skip_units').value;
    var skip_seconds = Math.floor(skip_units/timescale);
    document.getElementById('skip_seconds_display').value = skip_seconds;
}  

function set_interval_skip_display()
{
    var skip_units = playhead_position();
    var skip = format_time(skip_units);
    document.getElementById('interval_skip_display').value = skip;
    set_skip_seconds();
}

function set_interval_skip_units()
{
    var skip_units = playhead_position();
    document.getElementById('interval_skip_units').value = skip_units;
    set_interval_skip_display();
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
