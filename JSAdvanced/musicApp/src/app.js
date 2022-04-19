import { page, render } from './lib.js';
import { getUserData } from './util.js';
import { logout } from './data.js';

// import * as api from './data.js'   
// /*debug*/
// window.api = api;

import { homePage } from './views/home.js';
import { loginPage } from './views/login.js';
import { registerPage } from './views/register.js';
import { catalogPage } from './views/catalog.js';
import { createPage } from './views/create.js';
import { detailsPage } from './views/details.js';
import { editPage } from './views/edit.js';
import { searchPage } from './views/search.js';


const root = document.getElementById('main-content')

document.getElementById('logoutBtn').addEventListener('click', onLogout);

page(decorateContext);   
page('/', homePage);   
page('/login', loginPage)
page('/register', registerPage);
page('/catalog', catalogPage);
page('/details/:id', detailsPage);
page('/edit/:id', editPage);
page('/create', createPage);
page('/search', searchPage)


updateUserNav()
page.start()

function decorateContext(ctx, next) {
    ctx.render = (content) => render(content, root);
    ctx.updateUserNav = updateUserNav
    next()
} 


function onLogout(){
    logout();
    updateUserNav();
    page.redirect('/')
    
}  

function updateUserNav(){
    const userData = getUserData();

    const guestLog = document.getElementById('guestLogin')
    const guestReg = document.getElementById('guestRegister')
    const userCr = document.getElementById('userCreate')
    const userOut = document.getElementById('userLogout')



    if (userData){
        guestLog.style.display = 'none'
        guestReg.style.display = 'none'
        userCr.style.display = 'inline-block'
        userOut.style.display = 'inline-block'

    } else {
        guestLog.style.display = 'inline-block'
        guestReg.style.display = 'inline-block'
        userCr.style.display = 'none'
        userOut.style.display = 'none'
    }
}   

