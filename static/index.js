var ctn

document.addEventListener('DOMContentLoaded', nav)

function nav(){

    const burger = document.querySelector('.burger');
    const nav = document.querySelector('.main-nav');
	ctn = document.getElementById("ctn");
    
    burger.addEventListener('click', ()=>{
        nav.classList.toggle('show')
    })

}

function setUrl(path){

	console.log(path)
	ctn.setAttribute("src",`/${path}`)
}