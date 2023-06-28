<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<title>View_All_Organ_Donated_Details</title>
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
.style5 {color: #3A94CD}
.style7 {color: #CC0000}
.style9 {color: #006600}
.style10{color:#FF3300}
.style22{color:#000000}
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
          <h2>View  Organ Donated Status Details...<span class="style5"></span></h2>
          <p class="infopost">&nbsp;</p>
          <div class="clr"></div>
          
          <div class="post_content">
		  <table width="716" height="111" border="1" align="left"  cellpadding="0" cellspacing="0"  ">
                    <tr>
                      <td  width="17"  valign="middle" height="34" style="color: #2c83b0;"><div align="center" class="style57 style56 style7"><b>ID</b></div></td>
                     
					  
					  <td  width="41" valign="middle" height="34" style="color: #2c83b0;"><div align="center" class="style57 style56 style7"><b>Organ Name</b></div></td>
					  <td  width="40" valign="middle" height="34" style="color: #2c83b0;"><div align="center" class="style57 style56 style7"><b>Donor Name</b></div></td>
					  <td  width="40" valign="middle" height="34" style="color: #2c83b0;"><div align="center" class="style57 style56 style7"><b>Donor Age</b></div></td>		
					  <td  width="41" valign="middle" height="34" style="color: #2c83b0;"><div align="center" class="style57 style56 style7"><b>Blood Group</b></div></td>
					  <td  width="36" valign="middle" height="34" style="color: #2c83b0;"><div align="center" class="style57 style56 style7"><b>Height</b></div></td>
                      <td  width="43" valign="middle" height="34" style="color: #2c83b0;"><div align="center" class="style57 style56 style7"><b>Weight</b></div></td>
                      <td  width="69" valign="middle" height="34" style="color: #2c83b0;"><div align="center" class="style57 style56 style7"><b>Registeting user type</b></div></td>
                      <td  width="67" valign="middle" height="34" style="color: #2c83b0;"><div align="center" class="style57 style56 style7"><b>Registered Date</b></div></td>
                      <td  width="68" height="34" valign="middle" bgcolor="#FFFF00" style="color: #2c83b0;"><div align="center" class="style57 style56 style7"><b>Donation Status</b></div></td>
					  <td  width="66" valign="middle" height="34" style="color: #2c83b0;"><div align="center" class="style57 style56 style7"><b>Blockchain Code</b></div></td>
					  <td  width="92" height="34" valign="middle" bgcolor="#FFFF00" style="color: #2c83b0;"><div align="center" class="style57 style56 style7"><b>Transplantation Status</b></div></td>

					  
					  
                    </tr>
                    <%@ include file="connect.jsp" %>
                    <%
					  
						String s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12;
						int i=0;
						
						String luser=(String)application.getAttribute("cuser");
						try 
						{
						   	String query="select * from organ_donated_details where loginuser='"+luser+"' "; 
						   	Statement st=connection.createStatement();
						   	ResultSet rs=st.executeQuery(query);
					   		while ( rs.next() )
					   		{
								i=rs.getInt(1);
								s1=rs.getString(2);
								s2=rs.getString(3);
								s3=rs.getString(4);
								s4=rs.getString(5);
								s5=rs.getString(6);
								s6=rs.getString(7);
								s7=rs.getString(8);
								s8=rs.getString(9);
								s9=rs.getString(10);
								s10=rs.getString(11);
								s11=rs.getString(12);

								
						
					%>
                    <tr>
                      <td height="49" align="center"  valign="middle"><div align="center" class="style5 style37 style54 style55 style22"><span class="style22">
                        <%out.println(i);%>
                      </span></div></td>
                     
          <td height="49" align="center"  valign="middle"><div align="center" class="style5 style20 style37 style54 style55 style22">
                            <span class="style10">
                            <b><%out.println(s1);%></b>
                      </span></div></td>
                      <td height="49" align="center"  valign="middle"><div align="center" class="style5 style20 style37 style54 style55 style22">
                            <span class="style22">
                            <%out.println(s2);%>
                      </span></div></td>
                      <td height="49" align="center"  valign="middle"><div align="center" class="style5 style20 style37 style54 style55 style22">
                            <span class="style22">
                            <%out.println(s3);%>
                      </span></div></td>
					<td height="49" align="center"  valign="middle"><div align="center" class="style5 style20 style37 style54 style55 style22">
                            <span class="style22">
                            <%out.println(s4);%>
                      </span></div></td>
							
					<td height="49" align="center"  valign="middle"><div align="center" class="style5 style20 style37 style54 style55 style22">
                            <span class="style22">
                            <%out.println(s5);%>
                      </span></div></td>
							
					<td height="49" align="center"  valign="middle"><div align="center" class="style5 style20 style37 style54 style55 style22">
                            <span class="style22">
                            <%out.println(s6);%>
                      </span></div></td>
							
					<td height="49" align="center"  valign="middle"><div align="center" class="style5 style20 style37 style54 style55 style22">
                            <span class="style22">
                            <%out.println(s7);%>
                      </span></div></td>				
											
					<td height="49" align="center"  valign="middle"><div align="center" class="style5 style20 style37 style54 style55 style22">
                            <span class="style22">
                            <%out.println(s8);%>
                      </span></div></td>
					  <td height="49" align="center"  valign="middle"><div align="center" class="style5 style20 style37 style54 style55 style22">
                            <span class="style22">
                            <%out.println(s9);%>
                      </span></div></td>
                     
                      <td height="49"align="center" valign="middle" bgcolor="#FFFF00" style="color:#000000;"><div align="center" class="style22 style5 style20 style30 style37">
                          <div align="center" class="style20 style37 style46"><b> <%out.println(s10);%></b></div>
                      </div></td>
                       <td width="43" height="49"align="center" valign="middle" style="color:#000000;"><div align="center" class="style22 style5 style20 style30 style37">
                          <div align="center" class="style20 style37 style46"><b> <%out.println(s11);%></b></div>
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
		          <p>&nbsp;</p>
		          
		          <p><a href="DonorUser_Main.jsp" class="style16">Back</a></p>
				  
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
			<li><a href="UserLogin.jsp">Logout</a></li>
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