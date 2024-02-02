var big_wrapper;
var ham_menu;

function declare(){
    big_wrapper = document.querySelector(".big-wrapper");
    ham_menu = document.querySelector(".ham-menu");
}

const main = document.querySelector("main")
declare();


function events(){
    ham_menu.addEventListener("click",()  => {
        big_wrapper.classList.toggle("active");
    });
}

events();