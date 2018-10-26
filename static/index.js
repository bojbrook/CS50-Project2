
document.addEventListener('DOMContentLoaded', () => {
  
  // gets the user name from localStorage
  const user = sessionStorage.user
  
  // if (user)
  document.querySelector('#user').innerHTML = user;
  
  var channel = document.querySelector('#room').innerHTML;
  // Connect to websocket
  var socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port);

  
  console.log("Please " + user);

  // When connected, configure buttons
  socket.on('connect', () => {
    
      // Each button should emit a "submit vote" event
      document.querySelector('#button-message-send').onclick = () => {
        const message = document.querySelector('#input-message-section').value;
        document.querySelector('#input-message-section').value = "";  //reseting the input
        // const user = document.querySelector('#user').innerHTML;
        // channel = document.querySelector('#room').innerHTML;
        data = {
          'message': message, 
          'user': user,
          'channel': channel
        };
        console.log(data);
        socket.emit("Send Message", data);

        document.querySelector('#input-message-section').innerHTML = "";
      }; 
              
    });

  // // When a new vote is announced, add to the unordered list
  socket.on("New Message", data => {
    if(data['channel'] === channel){
      const li = document.createElement('li');
      const p = document.createElement('p');
      p.innerHTML = data['user'];
      li.innerHTML = data['message'];
      li.appendChild(p);
      document.querySelector('#list').append(li);
    }
  });

});
