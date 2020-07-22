const img=new Image();
const body=document.querySelector('body');
const name=document.querySelector('.js-name');


function paintBg(){
    img.src="1.jpg"
    img.classList.add(bgimage);
    body.prepend(img);
}
function init()
{
    paintBg()
}

init();