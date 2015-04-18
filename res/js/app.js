require(['tuple'], function(Tuple) {
	
	var BIG_DAY = new Date(2016, 12-6, 1);
	
	$(document).ready(function () {					
		$('#defaultCountdown').countdown({until: BIG_DAY});		
	});	
});