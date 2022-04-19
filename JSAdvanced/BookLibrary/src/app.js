import { page } from "./lib.js";
import decorateContext, {updateUserNav} from "./middlewares/decorationContext.js";
import { createPage } from "./views/create.js";
import { detailsPage } from "./views/details.js";
import { editPage } from "./views/edit.js";
import { homePage } from "./views/home.js";
import { loginPage } from "./views/login.js";
import { myBooksPage } from "./views/my-books.js";
import { registerPage } from "./views/register.js";


// import * as api from './api/data.js'

// window.api = api - used for manual testing in console

// const root = document.getElementById('site-content') - moved into decationContextFolder/file


page(decorateContext);
page('/', homePage)
page('/login', loginPage)
page('/register', registerPage)
page('/create', createPage)
page('/details/:id', detailsPage)
page('/edit/:id', editPage)
page('/my-books', myBooksPage)


updateUserNav();
page.start();

// moved into decorationContext folder/file
// async function decorateContext(ctx, next) {
//     ctx.render = (content) => render(content, root)

//     next()
// }