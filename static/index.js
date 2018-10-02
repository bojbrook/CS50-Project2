



document.addEventListener('DOMContentLoaded', () => {
  const user = document.querySelector('#user').innerHTML;
  // Check if correct user
  if (!localStorage.getItem('user')){
    console.log("Not right user")
  }
  var room = "";
  // Connect to websocket
  var socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port);

  // When connected, configure buttons
  socket.on('connect', () => {
    
      // Each button should emit a "submit vote" event
      document.querySelector('#button-message-send').onclick = () => {
        const message = document.querySelector('#input-message-section').value;
        // const user = document.querySelector('#user').innerHTML;
        room = document.querySelector('#room').innerHTML;
        data = {
          'message': message, 
          'user': user,
          'room': room
        };
        console.log(data);
        socket.emit("Send Message", data);

        document.querySelector('#input-message-section').innerHTML = "";
      }; 
              
    });

  // // When a new vote is announced, add to the unordered list
  socket.on("New Message", data => {
    if(data['room'] === room){
      const li = document.createElement('li');
      const p = document.createElement('p');
      p.innerHTML = data['user'];
      li.innerHTML = data['message'];
      li.appendChild(p);
      document.querySelector('#list').append(li);
    }
  });

});




// return false; //so page doesn't reload   