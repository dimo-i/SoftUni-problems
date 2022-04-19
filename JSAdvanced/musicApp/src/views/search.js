
import { searchAlbum } from "../data.js";
import { html } from "../lib.js"
import { albumPreviewTemplate } from "./albumPreview.js";


const searchTemplate = (onSearch) => html`
<section id="searchPage">
<h1>Search by Name</h1>
<div class="search">
    <input id="search-input" type="text" name="search" placeholder="Enter desired albums's name">
    <button @click=${onSearch} class="button-list">Search</button>
</div>

<h2>Results:</h2>

<!--Show after click Search button-->
<div class="search-result">
    <p class="no-result">No result.</p>
</div>
</section>`



export async function searchPage(ctx) {

    
    ctx.render(searchTemplate(onSearch))

    async function onSearch(event){
        event.preventDefault();

    }
}