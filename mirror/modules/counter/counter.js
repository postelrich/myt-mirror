
// Simple example of how to write the js for a module. It shows how to communicate
// with python application via websockets. The counter starts a countdown in the python
// side. Python decrements and emits an update which the js handler catches and updates
// the view.
register_module('counter', {

  ready: function (config) {
		var counter_socket = io('http://' + window.location.host + '/counter'); 

    // Ack socket connection
		counter_socket.on('connected', function(data) {
			console.log("counter socket connection: ", data.msg);
		});

    // Handler for updating count received from socket
		counter_socket.on('current_count', function(data) {
      $('#counter-count').text(data.data);
		});

    // Start counter
		counter_socket.emit('count', config);
  }

});
