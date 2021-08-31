
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
/* ----------footer styling ----------------*/
#content-wrap {
padding-bottom: 2.5px;
/* Footer height  & em refers to the font-size (2.5 times the font size */
}
/*    begining new layout CSS     */
}
.column {
float: left;
width: 25%;
/* 33.33 for 3 images*/
padding: 5px;
}
/* Clearfix (clear floats) */
.row::after {
content: "";
clear: both;
display: table;
}
/* Responsive layout - makes the three columns stack on top of each other instead of next to each other */
@media screen and (max-width: 500px) {
.column {
width: 100%;
}
}
.container {
position: relative;
max-width: 800px;
/* Maximum width */
margin: 0 auto;
/* Center it */
}
.container .content {
position: absolute;
/* Position the background text */
bottom: 0;
/* At the bottom. Use top:0 to append it to the top */
background: rgb(0, 0, 0);
/* Fallback color */
background: rgba(0, 0, 0, 0.5);
/* Black background with 0.5 opacity */
color: #f1f1f1;
/* Grey text */
width: 100%;
/* Full width */
padding: 20px;
/* Some padding */
height: auto;
-webkit-animation: fadeEffect 1s;
animation: fadeEffect 1s;
}
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
