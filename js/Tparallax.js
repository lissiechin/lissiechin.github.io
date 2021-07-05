
    /* -------Parallax Slider ----------- */

    let images = [...document.querySelectorAll('.img')];
    let slider = document.querySelector('.slider');
    let sliderwidth;
    let imagewidth;
    let current = 0;
    let target = 0;
    let ease = .05; /* speed of the scrolling */

    window, addEventListener('resize',init);

    images.forEach((img, indx) => {
        img.style.backgroundImage = `url(/Content/images/TravelSlider/${idx+1}.jpg)`
    })

    function lerp(start, end, t){
        return start * (1-t) + end * t;
    }

    function setTransform(el, transform){
        el.style.transform = transform;
    }

    function init(){
        sliderwidth = slider.getBoundClientRect().width;
        imagewidth = sliderwidth / image.length;
        document.body.style.height = `${sliderwidth - (window.innerWidth - window.innerHeight)}px`

    }

    function animate(){
        current = parseFloat(lerp(current, target, ease)).toFixed(2);
        target = window.scrollY;
        setTransform(slider, `translateX(-${curent}px`)
        requestAnimationFrame(animate)
    }

    function animateImages(){
        let ratio = current / imagewidth;
        let intersectionRatioValue;

        images.forEach((image, idx) => {
            intersectionRatioValue = ratio - (idx * 0.7);
            setTransform(image,`translateX(${intersectionRatioValue * 70}px`)
        })
    }

    init();
    animate()



/* MENU NAV button */
function openNav() {
    document.getElementById("mySidenav").style.width = "250px";
    document.getElementById("main").style.marginLeft = "250px";
    /* makes the right side fade to a dark gray */
    document.body.style.backgroundColor = "rgba(0,0,0,0.25)";
}

function closeNav() {
    document.getElementById("mySidenav").style.width = "0";
    document.getElementById("main").style.marginLeft = "0";
    document.body.style.backgroundColor = "white";
}
/* Loop through all dropdown buttons to toggle between hiding and showing its dropdown content - This allows the user to have multiple dropdowns without any conflict */
var dropdown = document.getElementsByClassName("dropdown-btn");
var i;
for (i = 0; i < dropdown.length; i++) {
    dropdown[i].addEventListener("click", function() {
        this.classList.toggle("active");
        var dropdownContent = this.nextElementSibling;
        if (dropdownContent.style.display === "block") {
            dropdownContent.style.display = "none";
        } else {
            dropdownContent.style.display = "block";
        }
    });




