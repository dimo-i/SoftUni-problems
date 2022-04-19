import { page, render } from './lib.js';
/*debug*/
import * as api from './api/data.js'
import { loginPage } from './views/login.js';
import { logout } from './api/data.js';
import { homePage } from './views/home.js';
import { getUserData } from './util.js';
import { registerPage } from './views/register.js';
import { detailsPage } from './views/details.js';
import { editPage } from './views/edit.js';
import { catalogPage } from './views/catalog.js';
import { createGamePage } from './views/create.js';



//debug
window.api = api;
/* ^debug^*/


const root = document.getElementById('main-content')

document.getElementById('logoutBtn').addEventListener('click', onLogout);


page(decorateContext);
page('/', homePage)
page('/login', loginPage)
page('/register', registerPage)
page('/details/:id', detailsPage);
page('/edit/:id', editPage);
page('/catalog', catalogPage);
page('/create', createGamePage)


 // TAKES FUNCTION


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
    const user = document.getElementById('user')
    const guest = document.getElementById('guest')

    if (userData){

        user.style.display = 'block'
        guest.style.display = 'none'
    } else {
        user.style.display = 'none'
        guest.style.display = 'block'
    }
} 