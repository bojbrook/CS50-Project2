document.addEventListener('DOMContentLoaded', () => {

  // setting up the form submit for username
  document.querySelector('form').onsubmit = () => {
    console.log("Form was clicked");
    var username = document.querySelector('#input-username').value;
    console.log(username);
    return false;
  }


  // Connect to websocket
  var socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port);

  // When connected, configure buttons
  socket.on('connect', () => {
    
      // Each button should emit a "submit vote" event
      document.querySelector('#button-message-send').onclick = () => {
        const message = document.querySelector('#input-message-section').value;
        const user = "Bowen Brooks";
        console.log(message);
        data = {
          'message': message, 
          'user': user
        };
        socket.emit('submit message', data);
      }; 
              
    });

  // // When a new vote is announced, add to the unordered list
  socket.on('message sent', data => {
    const li = document.createElement('li');
    const p = document.createElement('p');
    p.innerHTML = data['user'];
    li.innerHTML = data['message'];
    li.appendChild(p);
    document.querySelector('#list').append(li);
  });

});




// return false; //so page doesn't reload   