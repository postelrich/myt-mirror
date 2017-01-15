
register_module('counter', {
  ready: function (config) {
    console.log(config);
		var counter_socket = io('http://' + window.location.host + '/counter'); 
		counter_socket.on('connected', function(data) {
			console.log("counter socket connection: ", data.msg);
		});
		counter_socket.on('current_count', function(data) {
			console.log("current_count", data);
      $('#counter-count').text(data.data);
		});
		counter_socket.emit('count', config);
  }
});
