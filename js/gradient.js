var css = document.querySelector("h4")
var color1 = document.querySelector(".color1") 
var color2 = document.querySelector(".color2")
var gradient = document.querySelector("gradient")

function setGradient(){
	gradient.style.backgroud = "linear-gradient (45deg, "
	+ cplor1.value
	+", "
	+color2.value
	+")";
	css.textContent = gradient.style.background + ";";
}

color1.addEventListener("input", setGradient);
color2.addEventListener("input", setGradient);
