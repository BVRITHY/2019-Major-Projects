<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<title>Develop a Secure and Trust Based Key Management Protocol for Cloud Computing Environments</title>
<meta http-equiv="Content-type" content="text/html; charset=utf-8" />
<link rel="stylesheet" href="css/style.css" type="text/css" media="all" />
<script type="text/javascript" src="js/jquery-1.4.2.min.js"></script>
<script type="text/javascript" src="js/jquery.jcarousel.js"></script>
<script src="js/cufon-yui.js" type="text/javascript" charset="utf-8"></script>
<script src="js/Chaparral_Pro.font.js" type="text/javascript" charset="utf-8"></script>
<script type="text/javascript" src="js/jquery-func.js"></script>
<link rel="shortcut icon" type="image/x-icon" href="css/images/favicon.ico" />
</head>
     <%
if(request.getParameter("mg")!=null){%>
    
   <script>alert('Login Sucessfully..!')</script>
}  

<%}
if(request.getParameter("msg1")!=null){%>

 <script>alert('Owner Registration Failed..!')</script>
}
<%
}
%>
<%
if(request.getParameter("m3")!=null){%>
    
   <script>alert('username already exists')</script>
}  

<%}
if(request.getParameter("")!=null){%>

 <script>alert('Owner Registration Failed..!')</script>
}
<%
}
%>
<body>
<!-- START PAGE SOURCE -->
<div id="header">
    <br>
  <div class="shell">
    <h1>Develop a Secure and Trust Based Key Management Protocol for Cloud Computing Environments</h1>
    <div class="search">
      
    </div>
  </div>
</div>
<div id="navigation">
  <div class="shell">
    <ul>
      <li><a  href="index.html">HOME</a></li>
      <li><a  class="active" href="owner.jsp"> Owner</a></li>
     
       <li><a href="cloud.jsp">Cloud</a></li>
      <li><a href="manager.jsp">Trust  Manager</a></li>
       <li><a href="user.jsp">User</a></li>
    </ul>
  </div>
</div>
<div id="featured">
  <div class="shell">
    <div class="slider-carousel">
      <ul>
        <li>
          <div class="info">
           <p> Earlier MAKA protocols are designed for singleserver architecture. As Internet users grow
exponentially, the number of cloud servers
rendering different services has also grown
significantly. For the single-server architecture, it
is difficult for users to maintain a variety of
passwords for each server. To improve user
experience, many scholars propose more flexible
MAKA protocols for multi-server environments.
Combined with the unified management features
of the cloud platform, such protocols can be
conveniently applied. users and cloud servers
only need to register in the registration center
(RC) to mutual authentication and key agreement
. </p>
         </div>
          <div class="image"> <a href="#"><img src="css/images/logo.gif" alt="" /></a> </div>
          <div class="cl">&nbsp;</div>
        </li>
        <li>
          <div class="info">
           <p>Earlier MAKA protocols are designed for singleserver architecture. As Internet users grow
exponentially, the number of cloud servers
rendering different services has also grown
significantly. For the single-server architecture, it
is difficult for users to maintain a variety of
passwords for each server. To improve user
experience, many scholars propose more flexible
MAKA protocols for multi-server environments.
Combined with the unified management features
of the cloud platform, such protocols can be
conveniently applied. users and cloud servers
only need to register in the registration center
(RC) to mutual authentication and key agreement
. </p>
          </div>
          <div class="image"> <a href="#"><img src="css/images/logo.gif" alt="" /></a> </div>
          <div class="cl">&nbsp;</div>
        </li>
     
      </ul>
    </div>
  </div>
</div>
<div id="main">
  <div class="shell">
    <div id="main-boxes">
       
     <center>   
       <p align="justify">
    <p><font color="black" size="5"> Data Owner Registration </font></p><br/>
    
    <form name="myform" autocomplete="off" action="ownerregact.jsp" method="post"  onsubmit="return validateform()">
    <table align="center" width="321">
    <tr>
    <td width="191" height="43"><font color="black">User Name </td>
    <td width="218"><input autocomplete="off" name="username" required="" placeholder="User Name" /></td>
    </tr>
    <tr>
    <td height="43"><font color="black">Password </td>
    <td width="218"><input type="password" name="password" required="" placeholder="Password" /></td>
    </tr>
    <tr>
    <td height="43"><font color="black"> Email ID</td>
    <td><input name="email" autocomplete="off" required="" placeholder="Email ID"/></td>
    </tr>

        
    <tr>
    <td height="43"><font color="black">Select Gender</td>
    <td><select name="gender" style="width:170px;" required="">
    <option>--Select--</option>
    <option>MALE</option>
    <option>FEMALE</option>
    </select></td>
    </tr>
     
    
    <tr>
    <td height="65"><font color="black">Address</td>
    <td><textarea name="address" rows="3" cols="20" required=""></textarea></td>
    </tr> 
    <tr>
    <td height="43"><font color="black">Mobile Number </td>
    <td><input name="mobile" id="txtphoneno" required="" placeholder="Mobile Number"/></td>
    </tr>  

         <tr>
    <td height="43"><font color="black">Face Image </td>
    <td><input type="file" name="image"  required="" /></td>
    </tr>  
    <tr>
    <td height="43" rowspan="3">
    <p>&nbsp;</p></td>
    <td align="left" valign="middle"> <p>&nbsp;
    </p>
    <p>
    <input name="submit" type="submit" value="REGISTER" />
    </p>
    <div align="right">
    </div></td>
    </tr>
    </table>
    </form>
    </p>     
        
     </center>   
        
        
        
    </div>
    
    
    <div class="cl">&nbsp;</div>
  </div>
</div>
<div class="footer">
  <div class="shell">
    <p class="rf"></a></p>
    <div style="clear:both;"></div>
  </div>
</div>
<script type="text/javascript">pageLoaded();</script>
<!-- END PAGE SOURCE -->
</body>
</html>