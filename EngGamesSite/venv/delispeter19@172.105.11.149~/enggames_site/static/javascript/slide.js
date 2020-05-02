
const slides0 = document.querySelectorAll('.mach-img.section-1');
const slides1 = document.querySelectorAll('.mach-img.section-2');
const slides2 = document.querySelectorAll('.mach-img.section-3');
const slides3 = document.querySelectorAll('.mach-img.section-4');

const auto = true;
const intervalTime = 5000;

//const imgs = document.querySelectorAll('.mach-img');
//for(i in imgs){
//    console.log(imgs[i]);
//    imgs[i].onclick = function(){reset(imgs[i].classList[1])};
//}
let slideInterval0;
let slideInterval1;
let slideInterval2;
let slideInterval3;


function nextSlide(secNum, slides) {
    const current = document.querySelector('.section-'+secNum+'.current');

    current.classList.remove('current');

    if(current.nextElementSibling){
        current.nextElementSibling.classList.add('current');
    } else {
        slides[0].classList.add('current');
    }
}

function reset(section) {
    nextSlide();
    if(auto){
        if(section.substring(section.length-1,section.length) == 0){
            clearInterval(slideInterval0);
            slideInterval0 = setInterval(nextSlide, intervalTime, 0, slides0);
        } else {
            clearInterval(slideInterval1);
            slideInterval1 = setInterval(nextSlide, intervalTime, 1, slides1);
        }
    }
}

if(auto){
    slideInterval0 = setInterval(nextSlide, intervalTime, 1, slides0);
    slideInterval1 = setInterval(nextSlide, intervalTime, 2, slides1);
    slideInterval2 = setInterval(nextSlide, intervalTime, 3, slides2);
    slideInterval3 = setInterval(nextSlide, intervalTime, 4, slides3);
}