import { getRecentGames } from "../api/data.js";
import { html, page } from "../lib.js";
import { detailsPage } from "./details.js";

const homeTemplate = (cgames) => html`
<section id="welcome-world">

    <div class="welcome-message">
        <h2>ALL new games are</h2>
        <h3>Only in GamesPlay</h3>
    </div>
    <img src="./images/four_slider_img01.png" alt="hero">

    <div id="home-page">
        <h1>Latest Games</h1>
        <!-- Display div: with information about every game (if any) -->
        ${cgames.length == 0 
        ? html `<p class="no-articles">No games yet</p>` : cgames.map(gameTemplate)}

    </div>
</section>`


const gameTemplate = (gam) => html`
<div class="game">
    <div class="image-wrap">
        <img src="${gam.imageUrl}">
    </div>
    <h3>${gam.title}</h3>
    <div class="rating">
        <span>☆</span><span>☆</span><span>☆</span><span>☆</span><span>☆</span>
    </div>
    <div class="data-buttons">
        <a href="/details/${gam._id}" class="btn details-btn">Details</a>
    </div>
</div>`


export async function homePage(ctx) {
    const gam = await getRecentGames();

    ctx.render(homeTemplate(gam))

}
