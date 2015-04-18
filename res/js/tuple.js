define(function() {

	var Tuple = function() {
		var args = Array.prototype.slice.call(arguments, 0);
		args.map(function(val, index) {
			this['_' + (++index)] = val;	
		}, this);			
	};
	return Tuple;
});