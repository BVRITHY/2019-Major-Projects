<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<title>User Register Page</title>
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
.style7 {color: #FF0000}
.style9 {font-weight: bold}
.style11 {font-weight: bold}
.style14 {font-weight: bold}
.style33 {font-weight: bold}
.style39 {color: #FF0000; font-weight: bold; }
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
          <li><a href="CompanyLogin.jsp">Donor</a></li>
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
          <h2>Welcome To Patient Registration..!</h2>
          <p class="infopost"><img src="images/Register.jpg" width="211" height="152" /></p>
          <p class="infopost">&nbsp;</p>
          <div class="clr"></div>
          
          <div class="post_content">
            <form action="UserRegisterAuthentication.jsp" method="post" id="" enctype="multipart/form-data">
                    <label for="name"><span class="style33 style7 style9">
					
					User Name (required)</span></label>
                    <p class="style7"><strong>
                    <input id="name" name="userid" class="text" />
                    </strong></p>
			        <span class="style7"><strong>
			        <label for="password">Password (required)</label>
                    </strong>			        </span><p class="style7"><strong>
                    <input type="password" id="password" name="pass" class="text" />
                    </strong></p>
	                <span class="style7"><strong>
	                <label for="email">Email Address (required)</label>
                          </strong></span>
			        <p class="style7"><strong>
                    <input id="email" name="email" class="text" />
                    </strong></p>
			        <span class="style7"><strong>
			        <label for="mobile">Mobile Number (required)</label>
                    </strong></span>
			        <p class="style7"><strong>
                    <input id="mobile" name="mobile" class="text" />
                    </strong></p>
			        <span class="style7"><strong>
			        <label for="address">Your Address</label>
                    </strong></span>
			        <p class="style7"><strong>
                    <textarea id="address" name="address" rows="3" cols="50"></textarea>
                    </strong></p>
			        <span class="style7"><strong>
			        <label for="dob">Date of Birth (required)<br />
                    </label>
                    </strong></span>
			        <p class="style7"><strong>
                    <input id="dob" name="dob" class="text" />
                    </strong></p>
	                <span class="style7"><strong>
	                <label for="gender">Select Gender (required)</label>
                          </strong></span>
			        <p class="style7"><strong>
                    <select id="s1" name="gender" style="width:480px;" class="text">
                      <option>--Select--</option>
                      <option>MALE</option>
                      <option>FEMALE</option>
                    </select>
                    </strong></p>
			        <span class="style7"><strong>
			        <label for="pincode"></label>
			        <label for="location"></label>
                    </strong></span>
			        <p><strong>
                    <span class="style39">
                    <label for="pic">Select Profile Picture (required)</label>
                    </span><span class="style7"><label for="pic"></label>
                      </span>
                    <label for="pic"></label>
                    <input type="file" id="pic" name="pic" class="text" />
                    </strong></p>
                    <p><br />
                      <input name="submit" type="submit" value="REGISTER" />
                    </p>
                    <p>&nbsp;</p>
			        <p align="left" class="style14"><a href="UserLogin.jsp" class="style11">Back</a></p>
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
