import { getAllAlbums } from "../data.js"; 
import { html } from "../lib.js";
import { getUserData } from "../util.js";





const catalogTemplate = (albums) => html`
<section id="catalogPage">
    <h1>All Albums</h1>
    ${albums.length == 0
        ? html`<p>No Albums in Catalog!</p>`
        : albums.map(singleAlbum)}
</section>`


const singleAlbum = (album) => html`
<div class="card-box">
    <img src=${album.imgUrl}>
    <div>
        <div class="text-center">
            <p class="name">Name: ${album.name}</p>
            <p class="artist">Artist: ${album.artist}</p>
            <p class="genre">Genre: ${album.genre}</p>
            <p class="price">Price: $${album.price}</p>
            <p class="date">Release Date: ${album.releaseDate}</p>
        </div>
        ${detailsBtn(album)}
    </div>
</div>`

const detailsBtn = (album) => {
    const userData = getUserData()
    const isOwner = userData && album._ownerId == userData.id
    if(isOwner == true) {
        return html`
        <div class="btn-group">
            <a href="/details/${album._id}" id="details">Details</a>
        </div>`
    } else {
        null
    }
}


export async function catalogPage(ctx) {
    
    const albums = await getAllAlbums()
    ctx.render(catalogTemplate(albums))
}