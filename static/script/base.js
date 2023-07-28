const navToggle = document.querySelector('.hamburger-btn')
const primaryNav = document.querySelector('#primary-navigation')

navToggle.addEventListener('click', ()=>{
    state = primaryNav.getAttribute('data-visible')
    
    if (state === 'false'){
        primaryNav.setAttribute('data-visible', true)
        navToggle.setAttribute('aria-expanded', true)
        document.body.classList.add('nav-open')
        // console.log('true')
    }
    else if(state == 'true'){
        primaryNav.setAttribute('data-visible', false)
        navToggle.setAttribute('aria-expanded', false)
        document.body.classList.remove('nav-open')
        // console.log('false')
    }

})