<%@page import="java.sql.ResultSet"%>
<%@page import="java.sql.PreparedStatement"%>
<%@page import="novelefficient.Dbconnection"%>
<%@page import="java.sql.Connection"%>
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
if(request.getParameter("msg")!=null){%>
    
   <script>alert('Request Sent Sucessfully..!')</script>
}  

<%}
if(request.getParameter("msg1")!=null){%>

 <script>alert('Failed..!')</script>
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
    <li><a  href="cloudhome.jsp">HOME</a></li>
      <li><a   href="cloud_owner.jsp">View Owners</a></li>
      <li><a class="active" href="cloud_files.jsp">View Files</a></li>
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
       
        
        <p><center><font size="5" color="black">View Files</font></center></p><br/>
    <style>
        th{
            color: #50aac3;
        }
         tr{
            color: black;
        }
        
        td{
            text-align: center;
        }
    </style>
     
    
    <% 
String user = session.getAttribute("cloud").toString();


try{ 
	Connection con = null;
        con = Dbconnection.getConnection();
        PreparedStatement pst=con.prepareStatement("select * from upload ");
        ResultSet rs=pst.executeQuery();
        %>
        
        <center>   <table style="width:80%" border="2"></center>
         
        <tr>
        
        <th>File Name</th>
        <th>Uploaded Date</th>
        <th>Email</th>
        <th>Cipher</th>
      
        
     
     
 </tr>

<%
       
	while(rs.next()){
            %><tr>
                <td><%=rs.getString("filename")%></td>
                <td><%=rs.getString("cdate")%></td>
                <td><%=rs.getString("email")%></td>
                <td><textarea><%=rs.getString("cipher")%></textarea></td>
               
         
        </tr>
      <%  }
        
        %> </table>

<% }
	catch(Exception e)
	{
		System.out.println(e);
	}
	%>
        
        <br><br><br>
         <hr>    
        
            
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