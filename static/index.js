document.addEventListener('DOMContentLoaded', () => {

  // Connect to websocket
  var socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port);

  // When connected, configure buttons
  socket.on('connect', () => {
      // Each button should emit a "submit vote" event
      document.querySelector('button').onclick = () => {
        console.log('clicked button');
        const message = document.querySelector('input').value;
        console.log(message);
        socket.emit('submit message', {'message': message});
      }; 
              
    });

  // // When a new vote is announced, add to the unordered list
  socket.on('message sent', data => {
    const li = document.createElement('li');
    li.innerHTML = data;
    document.querySelector('#list').append(li);
  });

});




// return false; //so page doesn't reload   