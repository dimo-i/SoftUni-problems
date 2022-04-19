import { getAlbumById, deleteAlbum } from "../data.js";
import { html } from "../lib.js";
import { getUserData } from "../util.js";



const detailsTemplate = (album, isOwner, onDelete) => html`
<section id="detailsPage">
    <div class="wrapper">
        <div class="albumCover">
            <img src=${album.imgUrl}>
        </div>
        <div class="albumInfo">
            <div class="albumText">
                <h1>Name: ${album.name}</h1>
                <h3>Artist: ${album.artist}</h3>
                <h4>Genre: ${album.genre}</h4>
                <h4>Price: $${album.price}</h4>
                <h4>Date: ${album.releaseDate}</h4>
                <p>Description: ${album.description}</p>
            </div>
            <!-- Only for registered user and creator of the album-->
            ${albumControlBtn(album, isOwner, onDelete)}
        </div>
    </div>
</section>`


const albumControlBtn = (album, isOwner, onDelete) => {
    console.log(isOwner)
    if (isOwner) {
        return html`
        <div class="actionBtn">
            <a href="/edit/${album._id}" class="edit">Edit</a>
            <a @click = ${onDelete} href="javascript:void(0)" class="remove">Delete</a>
        </div>`
    } else {
        return null
    }
}


export async function detailsPage(ctx) {
    const album = await getAlbumById(ctx.params.id)
    const userData = getUserData();
    const isOwner = userData && album._ownerId == userData.id

    ctx.render(detailsTemplate(album, isOwner, onDelete))

    async function onDelete() {
        const choice = confirm("Are you sure you want to delete the Album")
        if (choice) {
            await deleteAlbum(ctx.params.id)
            ctx.page.redirect('/catalog')
        }
    }
}