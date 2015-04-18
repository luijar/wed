require(['jquery', 'tuple'], function($, Tuple) {
	
	var BIG_DAY = Date.parse('Fri, 01 July 2016 00:00:00 GMT-0400');
	
	function timer(time,update,complete) {
	    var start = new Date().getTime();
	    var interval = setInterval(function() {
	        var now = time-(new Date().getTime()-start);
	        if( now <= 0) {
	            clearInterval(interval);
	            complete();
	        }
	        else update(Math.floor(now/1000));
	    },100); // the smaller this number, the more accurate the timer will be
	}

	function toDisplay(millis) {
		var hours = Math.floor(millis / (1000*60*60));
        var mins  = Math.floor(millis / (1000*60));
        var secs  = Math.floor(millis / 1000);
        return new Tuple(hours, mins, secs);
	}

	$(document).ready(function () {	
		timer(
		    BIG_DAY, 
		    function(timeleft) { 
		    	var parts = toDisplay(timeleft);		    	
		        document.getElementById('timer').innerHTML = 
		        	parts._1+ 'hours' + parts._2 + 'minutes' + parts._3 + ' seconds';
		    },
		    function() { 
		        //alert("Timer complete!");
		    }
		);

	});	
});