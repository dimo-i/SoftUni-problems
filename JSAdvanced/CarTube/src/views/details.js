import { deleteCar, getCarById } from "../data.js";
import { html } from "../lib.js";
import { getUserData } from "../util.js";



const detailsTemplate = (car, isOwner, onDelete) => html`
<section id="listing-details">
    <h1>Details</h1>
    <div class="details-info">
        <img src=${car.imageUrl}>
        <hr>
        <ul class="listing-props">
            <li><span>Brand:</span>${car.brand}</li>
            <li><span>Model:</span>${car.model}</li>
            <li><span>Year:</span>${car.year}</li>
            <li><span>Price:</span>${car.price}$</li>
        </ul>
        <p class="description-para">${car.description}</p>
        ${btnControlsTemplate(car, isOwner, onDelete)}
    </div>
</section>`



const btnControlsTemplate = (car, isOwner, onDelete) => {
    if (isOwner) {
        return html`
        <div class="listings-buttons">
            <a href="/edit/${car._id}" class="button-list">Edit</a>
            <a @click = ${onDelete} href="javascript:void(0)" class="button-list">Delete</a>
        </div>`
    } else {
        return null
    }
}


export async function detailsPage(ctx) {

    const car = await getCarById(ctx.params.id)
    const userData = getUserData();
    const isOwner = userData && car._ownerId == userData.id

    ctx.render(detailsTemplate(car, isOwner, onDelete))

    async function onDelete() {
        const choice = confirm('Are you sure you want ot delete this Car FOREVER');


        if (choice) {
            await deleteCar(ctx.params.id)
            ctx.page.redirect('/catalog')
        }
    }

}