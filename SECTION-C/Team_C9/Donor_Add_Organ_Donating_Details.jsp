<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<title>Add Donor</title>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<link href="css/style.css" rel="stylesheet" type="text/css" />
<link rel="stylesheet" type="text/css" href="css/coin-slider.css" />
<script type="text/javascript" src="js/cufon-yui.js"></script>
<script type="text/javascript" src="js/droid_sans_400-droid_sans_700.font.js"></script>
<script type="text/javascript" src="js/jquery-1.4.2.min.js"></script>
<script type="text/javascript" src="js/script.js"></script>
<script type="text/javascript" src="js/coin-slider.min.js"></script>
<style type="text/css">
<!--
.style1 {color: #FFFFFF}
.style18 {font-size: 15px}
.style19 {
	color: #FFFFFF;
	font-weight: bold;
}
.style20 {font-size: 14px}
.style21 {color: #FFFFFF; font-weight: bold; font-size: 16px; }
-->
</style>
</head>
<body>
<div class="main">
  <div class="header">
    <div class="header_resize">
      <div class="menu_nav">
        <ul>
          <li><a href="index.html"><span>Home </span></a></li>
          <li><a href="about_Project.html"><span></span></a></li>
        </ul>
      </div>
      <div class="logo">
        <h2><span class="style1">Conversational Networks for Automatic<br/>
          <small>Online Moderation</small></span></h2>
      </div>
      <div class="clr"></div>
      <div class="slider">
        <div id="coin-slider"> <a href="#"><img src="images/slide1.jpg" width="960" height="294" alt="" /> </a> <a href="#"><img src="images/slide2.jpg" width="960" height="294" alt="" /> </a> <a href="#"><img src="images/slide3.jpg" width="960" height="294" alt="" /> </a> </div>
        <div class="clr"></div>
      </div>
      <div class="clr"></div>
    </div>
  </div>
  <div class="content">
    <div class="content_resize">
      <div class="mainbar">
        <div class="article">
          <h2>Add Organ Donating Details</h2>
          
          <div class="clr"></div>
          
          <p>&nbsp;</p>
          <p>
		  <%@ include file="connect.jsp" %>    
		  <%
			  try
			  {
			  
			   ArrayList a1=new ArrayList();
			  String str = " select * from organ_name ";
			  Statement st = connection.createStatement();
			  ResultSet rs = st.executeQuery(str);
			  while(rs.next())
			  {
			  a1.add(rs.getString(2));
			  }
			  
		  %>
		  
		  <form action="Donor_Add_Organ_Donating_Details1.jsp" method="post" enctype="multipart/form-data">
                <table width="479" border="0"  cellpadding="0" cellspacing="0"  >
				     <tr>
<td  width="188" height="45" valign="middle" bgcolor="#FF0000" style="color: #2c83b0;"><div align="left" class="style7 style18 style19 style1" style="margin-left:20px;">Select Organ Type </div></td>
					 <td  width="291" valign="middle" height="45" style="color:#000000;"><div align="left" style="margin-left:20px;">
					   
				       <div align="left">
					       <select type="text" name="organ_name" >
					         <option>--Select--</option>
					         <%  
					 for(int i=0;i<a1.size();i++)
        	         {
        	         %>
					         <option><%= a1.get(i)%></option>
					         
				             <%}%>
				         </select>
			            </div>
					 </div>					  </td>
					</tr>
					<tr>
<td  width="188" height="45" valign="middle" bgcolor="#FF0000" style="color: #2c83b0;"><div align="left" class="style1 style18 style7" style="margin-left:20px;"><strong>Donor Name </strong></div></td>
<td  width="291" valign="middle" height="45" style="color:#000000;"><div align="left" style="margin-left:20px;">
  
    <div align="left">
      <input type="text" name="dname">
      </div>
</div></td>
					</tr>
					<tr>
<td  width="188" height="45" valign="middle" bgcolor="#FF0000" style="color: #2c83b0;"><div align="left" class="style1 style18 style7" style="margin-left:20px;"><strong>Donor Age</strong></div></td>
<td  width="291" valign="middle" height="45" style="color:#000000;"><div align="left" style="margin-left:20px;">
  
    <div align="left">
      <input type="text" name="age">
      </div>
</div></td>
					</tr>
					<tr>
<td  width="188" height="45" valign="middle" bgcolor="#FF0000" style="color: #2c83b0;"><div align="left" class="style1 style18 style7" style="margin-left:20px;"><strong>Blood Group<br />
</strong></div></td>
<td  width="291" valign="middle" height="45"><div align="left" style="margin-left:20px;">
  
    <div align="left">
      <select name="bg">
        <option>---Select---</option>
         <option>A Positive</option>
         <option>A Negative</option>
         <option>B Positive</option>
         <option>B Negative</option>
         <option>O Positive</option>
         <option>0 Negative</option>
         <option>AB Positive</option>
         <option>AB Negative</option>
      </select>
    </div>
</div></td>
					</tr>
					<tr>
<td  width="188" height="45" align="left" valign="middle" bgcolor="#FF0000" style="color: #2c83b0;"><div align="left" class="style1 style18 style7" style="margin-left:20px;"><strong>Height</strong></div></td>
<td  width="291" align="left" valign="middle" height="45"><div align="left" style="margin-left:20px;">
  
    <div align="left">
      <input type="text" name="height">
      </div>
</div></td>
					</tr>
					<tr>
                      <td height="74" align="left" valign="middle" bgcolor="#FF0000" style="color: #2c83b0;"><div align="left" class="style1 style18 style8" style="margin-left:20px;"><strong>Weight</strong></div></td>
					  <td align="left" valign="middle" height="74" style="color: #2c83b0;"><div align="left" style="margin-left:20px;">
					    
				        <div align="left">
				          <input type="text" name="weight" />
			              </div>
					  </div></td>
				  </tr>
					<tr>
					  <td height="74" align="left" valign="middle" bgcolor="#FF0000" style="color: #2c83b0;"><div align="left" class="style20">
					    <div align="center" class="style21">Registering User Type </div>
					  </div></td>
					  <td align="left" valign="middle" height="74" style="color: #2c83b0;">
					    
				          <div align="center">
					          <select name="utype">
					            <option>---Select---</option>
					            <option>Self</option>
					            <option>Relative</option>
					            <option>Parent</option>
					            <option>Gurdian</option>
					            <option>Other</option>
				              </select>
		                  </div></td>
				  </tr>
					
					<div > <tr><td height="45" colspan="2" id="learn_more" align="center"  style="color:#FFFFFF;"><input type="submit" value="Donate" style="width:100px; height:35px; background-color:#000000; color:#FFFFFF;"/>&nbsp;&nbsp;<input type="reset" name="Reset" style="width:100px; height:35px; background-color:#000000; color:#FFFFFF;"/></td></tr></div>
			</table>
		  </form>
		
		 <%
			  }
			  catch(Exception e)
			  {
			  out.print(e);
			  }
			  %>
          <p>&nbsp;</p>
          <p align="right"><a href="DonorUser_Main.jsp">Back</a></p>
          <div class="clr"></div>
        </div>
        <div class="article">
          
          <div class="clr"></div>
        
          
          <div class="clr"></div>
        </div>
       
      </div>
      <div class="sidebar">
        <div class="searchform">
         
        </div>
        <div class="clr"></div>
        <div class="gadget">
          <h2 class="star"><span>Donor</span> Menu</h2>
          <div class="clr"></div>
          <ul class="sb_menu">
          <li><a href="DonorUser_Main.jsp"><span>Donor Main </span></a></li>
          <li><a href="DonorLogin.jsp"><span>Log Out</span></a></li>
          </ul>
        </div>
      </div>
      <div class="clr"></div>
    </div>
  </div>
  <div class="fbg"></div>
  <div class="footer">
    <div class="footer_resize">
     
      <div style="clear:both;"></div>
    </div>
  </div>
</div>
</body>
</html>
