text = 'Hello there, how are you?'
//
function br(){
    document.write('<br>'+'-------------------------------------------------------------------------------'+'<br>')
}
function b(){
    document.write('<br>')
}
//
function writee(text){
    document.write(text.toString().fixed().fontcolor('#20abcd').fontsize('3px'))
}
//
writee(text)
br()
//
thing = 'van anh'
writee('Google'.link('https://google.com/search?q='+thing)); br()
//
str = 'toi;ten;la;nguyen;thai;toan'
arr = str.split(';')
str = arr.join(' ')
writee(str);br(  )
//
writee('toString() & eval()');br()
//
writee(Date())
br()
//
writee(Math.E)
b()
writee(Math.SQRT2)
br()
//
function checkage(){
    writee('xin chao')
}
//
writee('<input type="button" name="age" onclick="checkage()">')
br()
//
