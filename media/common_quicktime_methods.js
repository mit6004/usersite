
// methods that depend on document.movie1
function playhead_position() {
	return document.movie1.GetTime();
}

function time_scale() {
	return document.movie1.GetTimeScale();
}




// internal methods
function set_display_area_to_fit_movie()
{
	var obj = document.movie1;
	var rectangle = obj.GetRectangle();

	if (rectangle)
	{
		rectangle = rectangle.split(',')
		var x1 = parseInt(rectangle[0]);
		var x2 = parseInt(rectangle[2]);
		var y1 = parseInt(rectangle[1]);
		var y2 = parseInt(rectangle[3]);

		var width = (x1 < 0) ? (x1 * -1) + x2 : x2 - x1;
		var height = (y1 < 0) ? (y1 * -1) + y2 : y2 - y1;
	}
	else
	{
		// a mov containing only audio
		var width = 200;
		var height = 0;
	}

  height_field = document.getElementById('video_height')
  width_field  = document.getElementById('video_width')
  
  if (height_field)
	  document.getElementById('video_height').value = height;

	if (width_field_
	  document.getElementById('video_width').value = width;

	obj.width = width;
	obj.height = height + 16;

	obj.SetControllerVisible(true);
}

function format_time(time_in_video_units){
	totalSec = time_in_video_units / time_scale();

	hours = parseInt( totalSec / 3600 ) % 24;
	minutes = parseInt( totalSec / 60 ) % 60;
	seconds = parseInt( totalSec ) % 60;
	fframes  = Math.round( ((totalSec % 60) - seconds) * 100);

	result =  zero_pad(hours) + ":" + zero_pad(minutes) + ":" + zero_pad(seconds) + ":" + zero_pad(fframes);
	return result;
};

function zero_pad(number)
{
	return (number < 10 ? "0" + number: number)
}

function myAddListener(obj, evt, handler, captures)
{
	if ( document.addEventListener )
		obj.addEventListener(evt, handler, captures);
	else
		// IE
		obj.attachEvent('on' + evt, handler);
}

function RegisterListener(eventName, objID, embedID, listenerFcn)
{
	var obj = document.getElementById(objID);
	if ( !obj )
		obj = document.getElementById(embedID);
	if ( obj )
		myAddListener(obj, eventName, listenerFcn, false);
}