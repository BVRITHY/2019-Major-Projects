<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<%@ include file="connect.jsp" %>
 <%@ page import="org.bouncycastle.util.encoders.Base64"%>
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<title>User Profile</title>
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
.style7 {color: #000000}
.style8 {color: #CC0000}
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
          <h2>User <%=request.getParameter("uname")%>'s Profile</h2>
          <p class="infopost">&nbsp;</p>
          <div class="clr"></div>
          
          <div class="post_content">
            <table width="500" border="1.5" align="center"  cellpadding="0" cellspacing="0"  >
                   
                    <%
						
						String user=request.getParameter("uname");
						String cname=request.getParameter("cname");
		   				String ccat=request.getParameter("ccat");
		  				int id= Integer.parseInt(request.getParameter("id"));
		   				
						
						String s1,s2,s3,s4,s5;
						int i=0;
						try 
						{
						   	String query="select * from user where username='"+user+"'"; 
						   	Statement st=connection.createStatement();
						   	ResultSet rs=st.executeQuery(query);
					   		if ( rs.next() )
					   		{
								i=rs.getInt(1);
								s1=rs.getString(4);
								s2=rs.getString(5);
								s3=rs.getString(6);
								s5=rs.getString(7);
								s4=rs.getString(9);
								
								
								
								
								
								
								
					%>
                    <tr>
                      <td width="196" rowspan="6" ><div class="style7 style26" style="margin:10px 13px 10px 13px;" ><strong><a class="#" id="img1" href="#" >
                          <input  name="image" type="image" src="user_Pic.jsp?picture=<%="userimage"%>&id=<%=i%>" style="width:150px; height:150px;" />
                      </a></strong></div></td>
                    </tr>
                    <tr>
                      <td  width="131" valign="middle" height="40" style="color: #2c83b0;"><div align="left" class="style15 style4 style3 style22 style36 style8" style="margin-left:20px;"><b>E-Mail</b></div></td>
                      <td  width="195" valign="middle" height="40" style="color:#FF3300;"><div align="left" class="style9 style10 style22 style38" style="margin-left:20px;">
                          <b><%out.println(s1);%></b>
                      </div></td>
                    </tr>
                    <tr>
                      <td  width="131" valign="middle" height="40" style="color: #2c83b0;"><div align="left" class="style15 style4 style3 style22 style36 style8" style="margin-left:20px;"><b>Mobile</b></div></td>
                      <td  width="195" valign="middle" height="40" style="color: #000000;"><div align="left" class="style9 style10 style22 style38" style="margin-left:20px;">
                          <%out.println(s2);%>
                      </div></td>
                    </tr>
                    <tr>
                      <td  width="131" align="left" valign="middle" height="40" style="color: #2c83b0;"><div align="left" class="style15 style4 style3 style22 style36 style8" style="margin-left:20px;"><b>Address</b></div></td>
                      <td  width="195" align="left" valign="middle" height="40" style="color: #000000;"><div align="left" class="style9 style10 style22 style38" style="margin-left:20px;">
                          <%out.println(s3);%>
                      </div></td>
                    </tr>
                    <tr>
                      <td  width="131" align="left" valign="middle" height="40" style="color: #2c83b0;"><div align="left" class="style15 style4 style3 style22 style36 style8" style="margin-left:20px;"><b>Date of Birth</b></div></td>
                      <td  width="195" align="left" valign="middle" height="40" style="color: #000000;"><div align="left" class="style9 style10 style22 style38" style="margin-left:20px;">
                          <%out.println(s5);%>
                      </div></td>
                    </tr>
                    <tr>
                      <td   width="131" align="left" valign="middle" height="51" style="color: #2c83b0;"><div align="left" class="style15 style4 style3 style22 style36 style8" style="margin-left:20px;"><b>Status</b></div></td>
					  
					  
					  
                      <td  width="195" align="left" valign="middle" height="51" style="color: #000000;"><div align="left">
                          <div align="left" class="style9 style10 style22 style38" style="margin-left:20px;">
                            <b><%out.println(s4);%></b>
                      </div></td>
						
                    </tr>
					
                    <%
						}
						connection.close();
					}
					catch(Exception e)
					{
						out.println(e.getMessage());
					}
					%>
            </table>
				  
				  <p class="style19">&nbsp;</p>
				  <p><a href="Donor_Review.jsp?cname=<%=cname%>&ccat=<%=ccat%>&id=<%=id%>" class="style16">Back</a></p>
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
          <h2 class="star"><span>Donor</span> Menu</h2>
          <div class="clr"></div>
          <ul class="sb_menu">
            <li><a href="DonorUser_Main.jsp">Home</a></li> 
			<li><a href="DonorLogin.jsp">Logout</a></li>
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