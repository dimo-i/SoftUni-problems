import { page, render } from './lib.js'; //to be checked
import { homePage } from './views/home.js';    //to be checked
import { getUserData } from './util.js';
import { logout } from './data.js';
import { loginPage } from './views/login.js';
import { registerPage } from "./views/register.js"
import { catalogPage } from "./views/catalog.js"
import { detailsPage } from './views/details.js';
import { editPage } from './views/edit.js';
import { createPage } from './views/create.js';
import { profilePage } from './views/profile.js';


// /*debug*/
// import * as api from './data.js'   //to be checked
// window.api = api;

const root = document.querySelector('main')

document.getElementById('logoutBtn').addEventListener('click', onLogout);

page(decorateContext);   
page('/', homePage);   
page('/login', loginPage)
page('/register', registerPage)   
page('/memes', catalogPage);   
page('/details/:id', detailsPage)
page('/edit/:id', editPage)   
page('/create', createPage)   
page('/profile', profilePage)   

updateUserNav()
page.start()

function decorateContext(ctx, next) {
    ctx.render = (content) => render(content, root);
    ctx.updateUserNav = updateUserNav
    next()
}   //to be checked


function onLogout(){
    logout();
    updateUserNav();
     page.redirect('/')
    
}   //to be checked

function updateUserNav(){
    const userData = getUserData();

    if (userData){
        document.querySelector('.user').style.display = 'block'
        document.querySelector('.guest').style.display = 'none'
        document.querySelector('.user span').textContent = `Welcome, ${userData.email}`
    } else {
        document.querySelector('.user').style.display = 'none'
        document.querySelector('.guest').style.display = 'block'
    }
}   
// to be checked
//IF usernav not updating try with await get(logout) ,possibly related to error 204(if active)