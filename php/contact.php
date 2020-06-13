<!-- https://www.w3schools.com/php/default.asp  >> LEARN PHP --->
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" >
<html>
  <head>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="https://www.w3schools.com/w3css/3/w3.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
    <link rel="stylesheet" type ="text/css" href ="main.css"/>
    <title> Contact</title>
  </head>
  <body>
    <div id ="page-container">
      <div id ="content-wrap">
        <!---------- Side Bar --------->
        
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
        
        <div id = "mySidenav" class="sidenav">
          <!-- The close button in the sidenav-->
          
          <a href="javascript:void(0)" class="closebtn" onclick="closeNav()" style =" text-align: right; padding: 10px; font-family: garamond;"> &#x2715; </a>
          
          <!-- create a home button leading back to the Home(main) page-->
          
          <a href ="index.html" style= "text-align: center; font-size: 50px;"> &#8962; </a>
          <a href="About.html" style ="text-align:center;">About</a>
          <!--<a href="Favorites.html" style ="text-align:center;">Favorites</a>-->
          <a href ="STO.html" style = "text-align: center;"> St. Olaf </a>
          <!--drop down menu within the sidebar-->
          <button style ="background-color:#111; border-color: #111; margin: auto;" class ="dropdown-btn"> Medium
          </button>
          <div class = "dropdown-container" style ="text-align:center;">
            <a href = "2D portfolio.html"> 2-Dimensional</a>
            <a href = "3D portfolio.html"> 3-Dimensional</a>
            <a href = "New Media.html"> New Media</a>
          </div>
          <a href="Photography.html" style ="text-align:center;">Photography</a>
          <a href="Contact.html" style ="text-align:center;">Contact</a>
        </div>
        
        <div id="main">
          <span style="font-size:30px;cursor:pointer" onclick="openNav()">&#9776; Menu </span>
          
          <!-- TEXT ~ BODY STARTS ------------>
          
          <body2>
            <h1> Contact </h1>
            <!----contact form!----->
            <div class="container">
              <div style="text-align:center">
                <p style= "margin-top: 50px; text-align: center;">Feel free to leave a message <br>or<br> check out my social media!</p>
              </div>
              <!---social Media buttons---->
              
              <div style="margin: 24px 0; text-align: center; padding:20px;font-size: 36px;">
                <a href="https://www.instagram.com/_chissie/"><i class="fa fa-instagram"></i></a>
                <a href="https://www.linkedin.com/in/elisabeth-c-6b0660186/"><i class="fa fa-linkedin"></i></a>
              </div>
              <div class="row">
                <div class="column">
                  <br>
                  <p style="text-align: center;"> Hello, This is still in the process of actually functioning. Hopefully, it will be up and running soon. Bye bye </p>
                  <br>
                </div>
                <?php
                $nameErr =  $emailErr = "";
                $name = $comment = $email = "";
                if($_SERVER["REQUEST_METHOD"] == "POST") {
                if (empty($_POST["name"])) {
                $nameErr = "Name is required";
                } else {
                $name = test_input($_POST["name"]);
                // check if name only contains letters and whitespace
                if (!preg_match("/^[a-zA-Z ]*$/",$name)) {
                $nameErr = "Only letters and white space allowed";
                }
                }
                
                if (empty($_POST["email"])) {
                $emailErr = "Email is required";
                } else {
                $email = test_input($_POST["email"]);
                // check if e-mail address is well-formed
                if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
                $emailErr = "Invalid email format";
                }
                }
                if (empty($_POST["comment"])) {
                $comment = "";
                } else {
                $comment = test_input($_POST["comment"]);
                }
                }
                function form_input($data){
                $data = trim($data);
                $data = stripslashes($data);
                $data = htmlspecialchars($data);
                return $data
                }
                ?>
                <div class="column">
                  <p><span class="error">* required field</span></p>
                  <form method="post" action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]);?>">
                    Name: <input type="text" name="name" value="<?php echo $name;?>">
                    <span class="error">* <?php echo $nameErr;?></span>
                    <br><br>
                    E-mail: <input type="text" name="email" value="<?php echo $email;?>">
                    <span class="error">* <?php echo $emailErr;?></span>
                    <br><br>
                    Website: <input type="text" name="website" value="<?php echo $website;?>">
                    <span class="error"><?php echo $websiteErr;?></span>
                    <br><br>
                  Comment: <textarea name="comment" rows="5" cols="40"><?php echo $comment;?></textarea></form>
                  </form>    
                   </div>
                   <?php
                   echo ;
                   echo $name;
                   echo ;
                   echo $email;
                   echo ;
                   echo $comment;
                   ?>

                  <!--     <div class="column">
                    <form action="/action_page.php">
                      <label for="fname">First Name</label>
                      <input type="text" id="fname" name="firstname" placeholder="Your name..">
                      <label for="lname">Last Name</label>
                      <input type="text" id="lname" name="lastname" placeholder="Your last name..">
                      <label for="subject">Subject</label>
                      <textarea id="subject" name="subject" placeholder="Write something.." style="height:170px"></textarea>
                      <input type="submit" value="Submit">
                    </form>
                  </div> -->
                </div>
              </div>
              <br />
              <br/>
              <footer id ="footer">
                <p> <sub> Lissie Chin &copy; 2020 </sub></p>
              </footer>
            </body2>
          </div>
          <!-- way to contact: adding email –– reference: https://www.w3schools.com/html/tryit.asp?filename=tryhtml_input_email
          and other forms: https://www.w3schools.com/html/html_forms.asp -->
          ?>
          <style>
          h1{
          text-align: center;
          font-family: garamond;
          border: 1px solid black;
          
          /* box-shadow: first # = horizontal offset; second # = vertical offset; last = color*/
          
          box-shadow: 20px 40px #caedeb;
          font-size: 40px;
          letter-spacing: 15px;
          text-shadow: 3px 2px #cacbcc;
          width: 400px;
          height: 80px;
          margin-left: auto;
          margin-right: auto;
          padding-top: 34px}
          /*------------ contact form style------*/
          body {
          font-family: Arial, Helvetica, sans-serif;
          font-family: "Lato", sans-serif;
          transition: background-color .5s;}}
          /* the box-sizing enables the fitting (formating) of the website*/
          * {box-sizing: border-box;
          }
          input[type=text], select, textarea {
          width: 100%;
          padding: 12px;
          border: 1px solid #ccc;
          margin-top: 6px;
          margin-bottom: 16px;
          resize: vertical;
          }
          input[type=submit] {
          background-color: #4CAF50;
          color: white;
          padding: 12px 20px;
          border: none;
          cursor: pointer;
          }
          input[type=submit]:hover {
          background-color: #45a049;
          }
          
          #page-container {
          position: relative;
          min-height: 100%;
          }
          /*-------->
          /*------Social Media Buttons ----*/
          
          a{
          text-decoration:none;
          font-size: 30px;
          color: black;
          }
          
          a hover{
          opacity: 0.7;
          }
          
          /*-------->*/
          #content-wrap {
          padding-bottom: 2.5em;    /* Footer height  & em refers to the font-size (2.5 times the font size */
          }
          #footer {
          position: fixed;
          left: 0;
          bottom: 0;
          width: 100%;
          /* ----------footer styling ----------------*/
          
          /*footnote with name & date edited */
          
          background: #f1f1f1;
          padding: 10px;
          text-align: center;
          font-size: 11px;
          font-family: garamond;
          color: black;
          display: block;}            /* Footer height */
          /*------ styling the SIDE BAR ---------*/
          
          .sidenav{
          height: 100%;
          width: 0;
          position: fixed;
          z-index: 1;
          top: 0;
          left: 0;
          background-color: #111;
          overflow-x: hidden;
          transition: 0.5s;
          padding-top: 60px;
          font-family: garamond}
          .sidenav a, .dropdown-btn {
          padding: 8px 8px 8px 32px;
          text-decoration: none;
          font-family: garamond;
          font-size: 25px;
          color: #818181;
          display: block;
          transition: 0.3s;}
          .sidenav a:hover, .dropdown-btn:hover {
          color: #f1f1f1;}
          
          .sidenav .closebtn {
          position: sticky;
          top: 0;
          right: 25px;
          font-size: 36px;
          margin-left: 50px;}
          .openbtn {
          font-size: 20px;
          cursor: pointer;
          background-color: #111;
          color: white;
          padding: 10px 15px;
          border: none;
          position: sticky;}
          .openbtn:hover {
          background-color: #444;}
          #main {
          transition: margin-left .5s;
          padding: 16px;}
          
          .dropdown {
          background-color:#111;}
          /* makes the drop down background lighter*/
          .dropdown-container {
          display: none;
          background-color: #262626;
          padding-left: 8px;}
          
          .fa-caret-down {
          float: right;
          padding-right: 75px;}
          
          /* active class to activate when clicked on */
          *.active {
          background-color: #caedeb;
          color: white;*
          
          /*--On smaller screens, where height is less than 450px, change the style of the sidenav (less padding and a smaller font size)*/
          @media screen and (max-height: 450px) {
          .sidebar {padding-top: 15px;}
          .sidebar a {font-size: 18px;}
          }
          
          </style>
          
          <!-- function telling the website to either close or open the menu navigation bar -->
          <script>
          function openNav() {
          document.getElementById("mySidenav").style.width = "250px";
          document.getElementById("main").style.marginLeft = "250px";
          /* makes the right side fade to a dark gray */
          document.body.style.backgroundColor = "rgba(0,0,0,0.25)";}
          function closeNav() {
          document.getElementById("mySidenav").style.width = "0";
          document.getElementById("main").style.marginLeft= "0";
          document.body.style.backgroundColor = "white";}
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
          }
          </script>
        </div>
      </div>
    </div>
  </html>
  <!------
  /* Style the container/contact section */
  .container {
  border-radius: 5px;
  background-color: #f2f2f2;
  padding: 10px;
  }
  /* Create two columns that float next to eachother */
  .column {
  float: left;
  width: 50%;
  margin-top: 6px;
  padding: 20px;
  }
  /* Clear floats after the columns */
  .row:after {
  content: "";
  display: table;
  clear: both;
  }
  /* Responsive layout - when the screen is less than 600px wide, make the two columns stack on top of each other instead of next to each other */
  @media screen and (max-width: 600px) {
  .column, input[type=submit] {
  width: 100%;
  margin-top: 0;
  }------>