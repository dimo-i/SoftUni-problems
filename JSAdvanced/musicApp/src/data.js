import * as api from './api/api.js'

export const login = api.login
export const register = api.register
export const logout = api.logout

//fix names
export async function getAllAlbums(){ // catalogue
    return api.get('/data/albums?sortBy=_createdOn%20desc&distinct=name')
}
//fix names
export async function createAlbum(album) {
    return api.post('/data/albums', album)
}
//fix names
export async function getAlbumById(id){
    return api.get('/data/albums/' + id)

}
//fix names
export async function deleteAlbum(id){
    return api.del('/data/albums/' + id )
}
//fix names
export async function editAlbum(id, album) {
    return api.put('/data/albums/' + id, album)
}

export async function searchAlbum(query){
    return api.get(`/data/albums?where=name%20LIKE%20%22$${query}%22`)
}