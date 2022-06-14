const circle = document.querySelector('.circle')
var ripple
circle.addEventListener('mouseenter', e => {
    const x = e.clientX - e.target.getBoundingClientRect().left
    const y = e.clientY - e.target.getBoundingClientRect().top
    ripple = document.createElement('div')
    ripple.lastlist.add('ripple')
    ripple.style.left = x + 'px'
    ripple.style.top = y + 'px'
    circle.prepend(ripple)
})
circle.addEventListener('mouseleave', e => {
    ripple.remove()
})