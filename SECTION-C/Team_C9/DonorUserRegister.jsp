<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<title>Donor User Register</title>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<link href="css/style.css" rel="stylesheet" type="text/css" />
<link rel="stylesheet" type="text/css" href="css/coin-slider.css" />
<script type="text/javascript" src="js/cufon-yui.js"></script>
<script type="text/javascript" src="js/cufon-aller.js"></script>
<script type="text/javascript" src="js/jquery-1.4.2.min.js"></script>
<script type="text/javascript" src="js/script.js"></script>
<script type="text/javascript" src="js/coin-slider.min.js"></script>
<style type="text/css">
<!--
.style1 {font-size: 14px}
.style2 {font-size: 24px}
.style4 {color: #000000}
-->
</style>
</head>
<body>
<div class="main">
  <div class="header">
    <div class="header_resize">
      <div class="menu_nav">
        <ul>
          <li class="active"><a href="index.html"><span>Home Page</span></a></li>
		  <li><a href="HospitalLogin.jsp">Hospital</a></li>
		  <strong></strong>
          <li><a href="DonorLogin.jsp">Donor</a></li>
          <li><a href="UserLogin.jsp"><span>Patients</span></a></li>
        </ul>
      </div>
      <div class="logo">
        <h1 class="style1"><a href="index.html" class="style2">Blockchain Based Management for Organ Donation and Transplantation</a></h1>
      </div>
      <div class="clr"></div>
      <div class="slider">
        <div id="coin-slider"> <a href="#"><img src="images/slide1.jpg" width="970" height="305" alt="" /> </a> <a href="#"><img src="images/slide2.jpg" width="970" height="305" alt="" /> </a> <a href="#"><img src="images/slide3.jpg" width="970" height="305" alt="" /> </a> </div>
      </div>
      <div class="clr"></div>
    </div>
  </div>
  <div class="content">
    <div class="content_resize">
      <div class="mainbar">
        <div class="article">
          <h2>Welcome To Donor User Registration.!</h2>
          <p class="infopost"><img src="images/Register.jpg" width="202" height="142" /></p>
          <div class="clr"></div>
		  <div class="post_content">
		  <form action="DonorUserRegisterStatus.jsp" method="post" id="" enctype="multipart/form-data">
                    
                 </p>
             	<label for="name"><span class="style33"><br/>                    
                    <span class="style4">User Name (required)</span></span></label>
                    <p class="style33">
                      <input id="name" name="cuserid" class="text" />
                    </p>
			        <span class="style33">
			        <label for="password"><span class="style4">Password (required)</span></label>
                    </span>
			        <p class="style33">
                      <input type="password" id="password" name="pass" class="text" />
                    </p>
	          <span class="style33">
			        <label for="email"><span class="style4">Email Address (required)</span></label>
              </span>
			        <p class="style33">
                      <input id="email" name="email" class="text" />
                    </p>
			        <span class="style33">
			        <label for="mobile"><span class="style4">Mobile Number (required)</span></label>
                    </span>
			        <p class="style33">
                      <input id="mobile" name="mobile" class="text" />
                    </p>
			        <span class="style33">
			        <label for="address"><span class="style4">Your Address</span></label>
                    </span>
			        <p class="style33">
                      <textarea id="address" name="address" rows="3" cols="19"></textarea>
                    </p>
			        <span class="style33">
			        <label for="dob"><span class="style4">Date of Birth (required)</span><br />
                    </label>
                    </span>
			        <p class="style33">
                      <input id="dob" name="dob" class="text" />
                    </p>
			        <span class="style33">
			        <label for="gender"><span class="style4">Select Gender (required)</span></label>
                    </span>
			        <p class="style33">
                      <select id="s1" name="gender" style="width:160px;" class="text">
                        <option>--Select--</option>
                        <option>MALE</option>
                        <option>FEMALE</option>
                      </select>
                    </p>
			        <p class="style33">
                      <label for="pic"><span class="style4">Select Profile Picture (required)</span></label>
                      <input type="file" id="pic" name="pic" class="text" />
                    </p>
					<p><br />
                      <input name="submit" type="submit" value="REGISTER" />
                    </p>
                    <p>&nbsp;</p>
			        <p align="left" class="style14"><a href="index.html" class="style11">Back</a></p>
					
            </form>
			
			
		  </div>
          <div class="clr"></div>
        </div>
      </div>
      <div class="sidebar">
        <div class="searchform">
          <form id="formsearch" name="formsearch" method="post" action="#">
            <span>
            <input name="editbox_search" class="editbox_search" id="editbox_search" maxlength="80" value="Search our ste:" type="text" />
            </span>
            <input name="button_search" src="images/search.gif" class="button_search" type="image" />
          </form>
        </div>
        <div class="clr"></div>
        <div class="gadget">
          <h2 class="star"><span>Sidebar</span> Menu</h2>
          <div class="clr"></div>
          <ul class="sb_menu">
            <li><a href="index.html">Home</a></li>
            <li><a href="#"></a></li>
          </ul>
        </div>
      </div>
      <div class="clr"></div>
    </div>
  </div>
  <div class="fbg">
    <div class="fbg_resize">
      <div class="clr"></div>
    </div>
  </div>
  <div class="footer">
    <div class="footer_resize">
      <div style="clear:both;"></div>
    </div>
  </div>
</div>
<div align=center></a></div></body>
</html>