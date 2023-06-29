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
if(request.getParameter("msg1")!=null){%>
    
   <script>alert('File Uploaded Sucessfully..!')</script>
}  

<%}
if(request.getParameter("msgg")!=null){%>

 <script>alert('Error in File Upload..!')</script>
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
      <li><a href="ownerhome.jsp">HOME</a></li>
      <li><a class="active" href="owner_upload.jsp">Upload</a></li>
      <li><a href="owner_view.jsp">View Files</a></li>
      <li><a href="owner_request.jsp">View Request</a></li>      
       <li><a href="logout.jsp">Logout</a></li>
    </ul>
  </div>
</div>
<div id="featured">
  <div class="shell">
    <div class="slider-carousel">
      <ul>
        <li>
          <div class="info">
           <p> We
provide a new efficient RDPC protocol based on homomorphic
hash function. The new scheme is provably secure against forgery
attack, replace attack and replay attack based on a typical
security model. To support data dynamics, an operation record
table (ORT) is introduced to track operations on file blocks. We
further give a new optimized implementation for the ORT which
makes the cost of accessing ORT nearly constant. Moreover, we
make the comprehensive performance analysis which shows that
our scheme has advantages in computation and communication
costs. Prototype implementation and experiments exhibit that the
scheme is feasible for real applications. </p>
         </div>
          <div class="image"> <a href="#"><img src="css/images/1.png" alt="" /></a> </div>
          <div class="cl">&nbsp;</div>
        </li>
        <li>
          <div class="info">
           <p>We
provide a new efficient RDPC protocol based on homomorphic
hash function. The new scheme is provably secure against forgery
attack, replace attack and replay attack based on a typical
security model. To support data dynamics, an operation record
table (ORT) is introduced to track operations on file blocks. We
further give a new optimized implementation for the ORT which
makes the cost of accessing ORT nearly constant. Moreover, we
make the comprehensive performance analysis which shows that
our scheme has advantages in computation and communication
costs. Prototype implementation and experiments exhibit that the
scheme is feasible for real applications.</p>
          </div>
          <div class="image"> <a href="#"><img src="css/images/2.jpg" alt="" /></a> </div>
          <div class="cl">&nbsp;</div>
        </li>
     
      </ul>
    </div>
  </div>
</div>
<div id="main">
  <div class="shell">
    <div id="main-boxes">
        
     <center><p><font size="5" color="black">Upload File </font></p><br/></center>
     
    <form action="Upload"  method="post" enctype="multipart/form-data" >
    <center><table width="371" border="0" >

    <tr><td><font color="black"> File Name :</td>
    <td><input type="text" name="fname" required="" /></td></tr>
    
    <tr><td><font color="black"> Select File :</td>
    <td><input type="file" name="file" required="" /></td></tr>
    <tr>
    <td height="43"><font color="black">Cloud</td>
    <td><select  name="cloud" class="form-control" required="required" style="margin-left: 58px;width: 250px"><br>
                                        &nbsp;&nbsp;&nbsp;&nbsp;<option value="na" selected="" style="color:darkblue"><font color="white">Choose One:</option>
                                                       <option value="1" style="color:darkblue">Cloud1</option>
                                        <option value="2" style="color:darkblue">Cloud2</option>
                                        <option value="3"style="color:darkblue">Cloud3</option>
                                         
                                        </select></td>
    </tr>
    <td rowspan="2">
    <td><br><input type="submit" name="submit" value="Upload" /></td>
   
    </td>
    <tr></tr>      
    </table></center>
    </form>    
        
        
            
    </div>
    <br>
    
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