var canvas = document.getElementById("board")
var ctx = canvas.getContext("2d")
var w = canvas.width
var h = canvas.height
var n = 10 //block size
var l = 5 // initial snake length
ctx.fillStyle = "#FF0000"
ctx.fillRect(0,0,l*n,n)
var dirs = [[0,-n],[0,n],[-n,0],[n,0]]
var index = 3
var body = []
for (var i=0;i<l;i++) {
  body.push([i*n,0])
}
document.onkeyup = (e) => {
  if (e.keyCode==38) {
    index = 0
  } else if (e.keyCode==40) {
    index = 1
  } else if (e.keyCode==37) {
    index = 2
  } else if (e.keyCode==39) {
    index = 3
  }
  //console.log("keycode="+e.keyCode)
}
function update() {
  //console.log("update")
  var x = body[0][0]
  var y = body[0][1]
  ctx.fillStyle = "#FFFFFF"
  ctx.fillRect(x,y,n,n)
  body.shift()
  x = body[body.length-1][0]+dirs[index][0]
  y = body[body.length-1][1]+dirs[index][1]
  if (x<0) {
    x = w-n
  }
  if (x>=w) {
    x = w-x
  }
  if (y<0) {
    y = h-n
  }
  if (y>=h) {
    y = h-y
  }
  ctx.fillStyle = "#FF0000"
  ctx.fillRect(x,y,n,n)
  body.push([x,y])
}
setInterval(update, 100)
