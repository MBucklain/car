const io = require("socket.io")(5000);
const io1 = require('socket.io')(4001, {
  cors: {
    origin:'*'
  }
});


let interval;
let dataFromReact;
console.log("here")
io.on("connection", (socket) => {
  console.log("here6")
  io1.on("connection", (socket1) => { 
    console.log("here4")
    socket1.on("rcvdFromReact", data1 => { 
      dataFromReact = data1;
      socket.emit("my_message", data1);
    });
  });
  io1.on("connect_error", (err) => {
    console.log(`connect_error due to ${err.message}`);
  });
});
console.log("here")

    
    
io.on("connection", socket => {
  socket.send("hello");
  console.log("here1")
  io1.on("connection", socket1 => {
  // either with send()
  console.log('Connected');
  socket.on("fromAPI", (data) => {
    console.log(data);
   socket1.emit("fromNodejs", data);

  });
 });
});

console.log("here")
