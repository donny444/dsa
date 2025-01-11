const LinkedList = require("./linked_list.js");
const Stack = require("./stack.js");
const Queue = require("./queue.js");

const data1 = new LinkedList("มด2");
data1.push("มด3");
data1.unshift("มด1");
data1.showList()

const data2 = new Stack("ลูกชิ้น1");
data2.push("ลูกชิ้น2");
data2.push("ลูกชิ้น3");
data2.push("ลูกชิ้น4");
data2.pop();
//Something wrong here
console.log(data2);

const data3 = new Queue("รภไฟ1");
data3.enqueue("รถไฟ2");
data3.enqueue("รถไฟ3");
data3.dequeue();
console.log(data3);