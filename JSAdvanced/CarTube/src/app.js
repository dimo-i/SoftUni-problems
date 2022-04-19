import { page, render } from './lib.js'; 


/*debug*/
import * as api from './data.js';
import { logout } from './api/api.js';
import { getUserData } from './util.js';
import { homePage } from './views/home.js';
import { loginPage } from './views/login.js';
import { registerPage } from './views/register.js';
import { catalogPage } from './views/catalog.js';
import { createPage } from './views/create.js';
import { editPage } from './views/edit.js';
import { detailsPage } from './views/details.js';
import { myCarsPage } from './views/mycars.js';

window.api = api;

const root = document.getElementById('site-content')

document.getElementById('logoutBtn').addEventListener('click', onLogout);

page(decorateContext);  
page('/', homePage); 
page('/login', loginPage)
page('/register', registerPage)  
page('/catalog', catalogPage);
page('/create', createPage);
page('/edit/:id', editPage);
page('/details/:id', detailsPage)
page('/my-cars', myCarsPage)

updateUserNav()
page.start()

function decorateContext(ctx, next) {
    ctx.render = (content) => render(content, root);
    ctx.updateUserNav = updateUserNav;
    next()
}   


function onLogout(){

    logout();
    updateUserNav();
    page.redirect('/')
}   

function updateUserNav(){
    const userData = getUserData();
    const profile = document.getElementById("profile")
    const guest = document.getElementById("guest")
    
    if (userData){
        profile.style.display = 'block'
        guest.style.display = 'none'
        document.getElementById("welcomeMsg").textContent = `Welcome ${userData.username}`
    } else {
        profile.style.display = 'none'
        guest.style.display = 'block'

    }

}   