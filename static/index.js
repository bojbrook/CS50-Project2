const MONTHS = ["Jan","Feb","Mar","Apr","May","June","July","Aug","Sept","Oct","Nov","Dec"];


document.addEventListener('DOMContentLoaded', () => {
  
  // gets the user name from localStorage
  // const user = sessionStorage.user
  const user = localStorage.getItem('user')
  
  // if (user)
  // document.querySelector('#user').innerHTML = user;
  
  //getting the channel Name & setting current channel
  var channel = document.querySelector('#room').innerHTML;
  document.querySelector('#room').innerHTML = channel.toUpperCase();
  localStorage.setItem('currentChannel',channel);

  // Connect to websocket
  var socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port);

  
  console.log("Logged in " + user);

  // logging out a use
  document.querySelector('#nav-logout').onclick = () =>{
    localStorage.setItem("currentChannel","null");
  }

  // When connected, configure buttons
  socket.on('connect', () => {
    
      // Each button should emit a "submit vote" event
      document.querySelector('#button-message-send').onclick = () => {
        const message = document.querySelector('#input-message-section').value;
        document.querySelector('#input-message-section').value = "";  //reseting the input
        // const user = document.querySelector('#user').innerHTML;
        // channel = document.querySelector('#room').innerHTML;\
        const time = getTime();
        console.log(getTime())
        data = {
          'message': message, 
          'user': user,
          'channel': channel,
          'time': time
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
      li.className="list-group-item";


      const p = document.createElement('p');
      p.className = "message-sender";
      p.innerText = "-"+data['user'];
      
      span_time = document.createElement('span');
      span_time.className = "message-time";
      span_time.innerText = data['time'];
      
      p.appendChild(span_time);

      
      li.innerText= data['message'];
      li.appendChild(p);
      document.querySelector('#list').append(li);
    }
  });

});


// returns the time in a readable string
function getTime(){
  var d = new Date();
  const month = MONTHS[d.getMonth()];
  const day = d.getDate();
  let hour = d.getHours();
  const min = d.getMinutes();

  if(hour > 12){
    hour = hour - 12;

  }
  return month + " " + day + " " + hour + ":" + min;
}
