<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<title>Authentication Page</title>
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
.style3 {
	color: #FF0000;
	font-weight: bold;
}
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
          <h2>Authentication..!</h2>
          <p class="infopost">&nbsp;</p>
          <div class="clr"></div>
          
          <div class="post_content">
            <%@ include file="connect.jsp" %>

<%
   	String type=request.getParameter("type");      
    try{
	
		
		
		if(type.equalsIgnoreCase("Hospital"))
		{
		
			String Hospitalname=request.getParameter("Hospitalid");      
         	String Password=request.getParameter("pass");
			
			application.setAttribute("Hospital",Hospitalname);
			
			String sql="SELECT * FROM Hospital where Hospitalname='"+Hospitalname+"' and password='"+Password+"'";
			Statement stmt = connection.createStatement();
			ResultSet rs =stmt.executeQuery(sql);
			
			if(rs.next())
			{
				response.sendRedirect("Hospital_Main.jsp");
			}
			else
			{
				response.sendRedirect("HospitalRe-Login.jsp");
			}
		}
		
		
		
		 else if(type.equalsIgnoreCase("user"))
		{
			String username=request.getParameter("userid");      
   	        String Password=request.getParameter("pass");
			
			application.setAttribute("user",username);
			
			String sql="SELECT * FROM user where username='"+username+"' and password='"+Password+"'";
			Statement stmt = connection.createStatement();
			ResultSet rs =stmt.executeQuery(sql);
			
			
			if(rs.next())
			{
				String sql1="SELECT * FROM user where username='"+username+"' and status='Authorized'";
				Statement stmt1 = connection.createStatement();
				ResultSet rs1 =stmt1.executeQuery(sql1);
			
				if(rs1.next())
			    {
				response.sendRedirect("User_Main.jsp");
				}
				else
				{
									%>
									<br/><h3><p align="left" class="style3">&nbsp;</p>
									  <p align="left" class="style4" style="color:#000000">You are not the Authorized User, Please wait!! </p>
									</h3>
									<br/><br/><a href="UserLogin.jsp">Back</a>
									<%
			    }
			}
			else
			{
				response.sendRedirect("UserRe-Login.jsp");
			}
		}
		else if(type.equalsIgnoreCase("cuser"))
		{
			
			String company=request.getParameter("company");
			String cusername=request.getParameter("cuserid");      
         	String Password=request.getParameter("pass");
			
			application.setAttribute("cname",company);
			application.setAttribute("cuser",cusername);
			
			String sql="SELECT * FROM cuser where (cusername='"+cusername+"' and password='"+Password+"') ";
			Statement stmt = connection.createStatement();
			ResultSet rs =stmt.executeQuery(sql);
			
			
			if(rs.next())
			{
			
					String sql1="SELECT * FROM cuser where cusername='"+cusername+"' and status='Authorized'";
					Statement stmt1 = connection.createStatement();
					ResultSet rs1 =stmt1.executeQuery(sql1);
			
					if(rs1.next())
					{
					response.sendRedirect("DonorUser_Main.jsp");
					}
					else
					{
									%>
									<br/><h3><p align="left" class="style3">&nbsp;</p>
									  <p align="left" class="style4" style="color:#000000">You are not the Authorized User, Please wait!! </p>
									</h3>
									<br/><br/><a href="DonorLogin.jsp">Back</a>
									<%
			   		 }
			}		 
			else
			{
				response.sendRedirect("DonorUserRe-Login.jsp");
			}
		}
		else{
		
			}
	}
	catch(Exception e)
	{
		out.print(e);
	}
%>
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
