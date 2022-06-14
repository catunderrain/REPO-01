// b = 8
// a = (b == 3) ? 'yes' : 'no'
// console.log(a)
//---------------------------------------------------
// a = 2
// if(a==5){
//     console.log('oke five')
// }
// else if(a==7){
//     console.log('seven')
// }
// else{
//     console.log('cut')
// }
//--------------------------------------------------
// a = 4
// switch(a-2){
//     case 1:
//         console.log('dkm')
//         break
//     case 2:
//         console.log('hello')
//         break
// }
//------------------------------------------------
// for(i=2;i<5;i++)
// {
//     console.log(i)
// }
//-----------------------------------------------
// var x
// var mycars = ['gello','2','3']
// for(x in mycars){
//     console.log(mycars[x])
//     console.log(x)
// }
//----------------------------------------------
// a = 0
// while(a < 10){
//     a++
//     console.log(a)
// }
// --------------------------------------------------
// a=0
// do{
//     a++
//     console.log(a)
// }while(a<10)
//-----------------------------------------------
// function hello(name){
//     a = 'hello ' + name + ', how are you?'
//     console.log(a)
//     return a
// }
// hello('Van Anh')
//--------------------------------------------------
// a = 5
// console.log(typeof(a))
//--------------------------------
// condense:
// literal:
//----------------------
// a = ['1','a','@']
// console.log(a.length)
// console.log(a.prototype)
//-----------------------------
//IIFE
// (function(){
//     console.log("hello") 
// })()
//-----------------------------------
//Callbacks, promises and async await
// func = (name, func2) => {
//     console.log('Hello', name)
//     func2()
// }
// function funcx(name, func2){
//     console.log('Hello', name)
//     func2()
// }
// function other(){
//     console.log('Bye')
// }

// func('Toan', other)
// funcx('Tml VA', other)
//-------------------------------
// setTimeout(()=>{
//     console.log('Hello')
// },1000)
// console.log('Hi')
//---------------------------------
// async function hello(){
//     abc = new Promise(
//         (da) => {
//         setTimeout(
//             () => 
//             da('done'), 1000)
//     }
//     )
//     result = await abc
//     console.log(result)
// }
// hello()
//---------------------------------
// names = ['toan', 'anh']
// age = [-3, -1, 0 ,4 ,5]
// all = names.concat(age)
// // console.log(all)
// function zero(element){
//     return(element>0)
// }
// if (age.every(zero) == false)
//     console.log('okay')
// //
// j = age.concat(names).join(' ')
// console.log(j)
// //
// ind = names.indexOf('anh')
// console.log(ind)
// //
// function db(ele){
//     return ele*2
// }
// agedb = age.map(zero)
// console.log(agedb)
// //
// ages = age.splice(1,[2],[3,4])
// console.log(ages)
//--------------------------------------
// str = 'thaitoan'
// a = str.anchor()
// a = str.big()
// a = str.fontcolor('red')
// console.log(a)
// console.log(str.charCodeAt(3))
// b = String.fromCharCode(1611,2001)
// console.log(b)
//---------------------------------------
const colors = ["green", "red", "rgba(133,122,200)", "#f15025"];
console.log(Math.floor(Math.random() * colors.length))