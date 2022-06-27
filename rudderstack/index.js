const express = require("express")
const app = express();
const http = require("http")
const server = http.createServer(app);

const { Server } = require("socket.io")
const io = new Server(server)

app.get("/", (req, res) => {
  res.sendFile(__dirname + "/index.html")
})


var usermap = {};
io.on("connection", (socket) => {
  console.log("user connected ", socket.id);
  socket.on("disconnect", () => {
    console.log("user disconnected")
  });
  socket.on("chat message", (from, to, msg) => {
    if (to === "") {
      socket.broadcast.emit("chat message", from, to, msg);
    } else {
      room = usermap[to];
      socket.to(room).emit("chat message", from, to,  msg);
    }
  });
  socket.on("joined", (name) => {
    usermap[name] = socket.id;
  });
});

server.listen(4000, () => {
  console.log("now up on 4000");
})

