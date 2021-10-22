let imgArray = [
    'static/carousel1.jpg',
    'static/carousel2.jpg',
    'static/carousel3.jpg',
    'static/carousel4.jpg',
    'static/carousel5.jpg'
];

let img = document.getElementById('slide');
let i = 0;

const slideShow = () => {
    img.src = imgArray[i];
    i = (i < imgArray.length - 1) ? i+1 : 0;
}

const interval = () => {
    setInterval(slideShow,1000);
}
