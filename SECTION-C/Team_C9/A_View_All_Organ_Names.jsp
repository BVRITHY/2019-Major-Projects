<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<title>A_View_All_Organ_Names</title>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<link href="css/style.css" rel="stylesheet" type="text/css" />
<link rel="stylesheet" type="text/css" href="css/coin-slider.css" />
<script type="text/javascript" src="js/cufon-yui.js"></script>
<script type="text/javascript" src="js/cufon-chunkfive.js"></script>
<script type="text/javascript" src="js/jquery-1.4.2.min.js"></script>
<script type="text/javascript" src="js/script.js"></script>
<script type="text/javascript" src="js/coin-slider.min.js"></script>
<style type="text/css">
<!--
.style1 {font-size: 36px}
.style2 {font-size: 16px}
.style3 {color: #FFFFFF}
.style4 {color: #FF00FF}
.style5 {color: #FF0000}
-->
</style>
</head>
<body>
<div class="main">
  <div class="header">
    <div class="header_resize">
      <div class="menu_nav">
        <ul>
          <li><a href="index.html"><span>Home Page</span></a></li>
        </ul>
      </div>
      <div class="clr"></div>
      <div class="logo">
        <h1><a href="index.html" class="style1">Blockchain Based Management for Organ Donation and Transplantation</a></h1>
      </div>
      <div class="searchform"></div>
      <div class="clr"></div>
      <div class="slider">
        <div id="coin-slider"> <a href="#"><img src="images/slide1.jpg" width="960" height="360" alt="" /><span><big>Blockchain Based Management for Organ Donation and Transplantation</big></span></a> <a href="#"><img src="images/slide2.jpg" width="960" height="360" alt="" /><span><big>Blockchain Based Management for Organ Donation and Transplantation</big></span></a> <a href="#"><img src="images/slide3.jpg" width="960" height="360" alt="" /><span><big>Blockchain Based Management for Organ Donation and Transplantation</big></span></a> </div>
        <div class="clr"></div>
      </div>
      <div class="clr"></div>
    </div>
  </div>
  <div class="content">
    <div class="content_resize">
      <div class="mainbar">
        <div class="article">
          <h2><span class="style4">View All Blockchain Hashcode for Organ Name </span></h2>
          <p>&nbsp;</p>
          <table width="619" align="center"  cellpadding="0" cellspacing="0" >
            <tr>
              <td width="147" height="37" valign="middle" bgcolor="#FF0000" style="color: #2c83b0;"><div align="center" class="style27 style105 style65 style2 style3"><em><strong>ID</strong></em></div></td>
              
              <td width="209" valign="middle" bgcolor="#FF0000" style="color: #2c83b0;"><div align="center" class="style27 style105 style65 style2 style3"><em><strong>Organ Name </strong></em></div></td>
              <td width="397" valign="middle" bgcolor="#FF0000" style="color: #2c83b0;"><div align="center" class="style27 style105 style65 style2 style3"><em><strong>Hash Code</strong></em></div></td>
			</tr>
            <%@ include file="connect.jsp" %>
            <%
					  
						String s1,s2,s3,s4,s5,s6,s7;
						int i=0;
						try 
						{
						   	String query="select * from organ_name"; 
						   	Statement st=connection.createStatement();
						   	ResultSet rs=st.executeQuery(query);
					   		while ( rs.next() )
					   		{
								i=rs.getInt(1);
								s1=rs.getString(2);
								s2=rs.getString(3);
								
								
					%>
            <tr bgcolor="#99CCFF">
            
              
              <td height="67"  align="center"  valign="middle" bgcolor="#FFFFFF"><div align="center" class="style71 style70 style20 style37 style54 style55 style86 style57 style5"><strong>
                  <%out.println(i);%>
              </strong></div></td>
              <td  align="center"  valign="middle" bgcolor="#FFFFFF"><div align="center" class="style71 style70 style20 style37 style54 style55 style86 style57 style5"><strong>
                  <%out.println(s1);%>
              </strong></div></td>
              <td align="center"  valign="middle" bgcolor="#FFFFFF"><div align="center" class="style71 style70 style20 style37 style54 style55 style86 style57 style5"><strong>
                  <%out.println(s2);%>
              </strong></div></td>
            </tr>
			 
						<%	}
						
									
					connection.close();
					}
					catch(Exception e)
					{
						out.println(e);
					}
					%>
    </table>
	  <p align="right"><a href="Hospital_Main.jsp">Back</a></p>
        </div>
      </div>
      <div class="clr"></div>
    </div>
  </div>
  <div class="fbg">
    <p>&nbsp;</p>
    <p>&nbsp;</p>
    <p>&nbsp;</p>
    <p>&nbsp;</p>
  </div>
  <div class="footer">
    <div class="footer_resize">
      <div style="clear:both;"></div>
    </div>
  </div>
</div>
<div align=center></div>
</body>
</html>
