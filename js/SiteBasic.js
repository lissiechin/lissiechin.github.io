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
/* parallax */
jQuery(document).ready(function($){
'use strict';
$.Scrollax();
});
/* -------------------------------------------*/
/* scroll to top */
//Get the button
var mybutton = document.getElementById("myBtn");
// When the user scrolls down 20px from the top of the document, show the button
window.onscroll = function() {
scrollFunction()
};
function scrollFunction() {
if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
mybutton.style.display = "block";
} else {
mybutton.style.display = "none";
}
}
// When the user clicks on the button, scroll to the top of the document
function topFunction() {
document.body.scrollTop = 0;
document.documentElement.scrollTop = 0;
}
/*            end of scroll to top      */
/*----------------------------------------------*/

/* Fade in tabs */
@-webkit-keyframes fadeEffect {
from {
opacity: 0;
}
to {
opacity: 1;
}
}
@keyframes fadeEffect {
from {
opacity: 0;
}
to {
opacity: 1;
}
}