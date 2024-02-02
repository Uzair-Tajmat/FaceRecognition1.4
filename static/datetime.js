
`use strict`
var n = new Date();
y = n.getFullYear();
m = n.getMonth() + 1;
d = n.getDate();
console.log(n);
document.getElementById("date").textContent =  d + "/" + m + "/" + y; //it will print on html page

1
2
var today = new Date();
var time = today.getHours() + ":" + today.getMinutes() + ":" + today.getSeconds();
console.log(time);
document.getElementById("time").textContent =  time;

