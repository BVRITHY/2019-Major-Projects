<%@page import="novelefficient.decryption"%>
<%@page import="java.sql.*"%>
<%@page import="novelefficient.Dbconnection"%>
<%@ page session="true" %>
<%@page import="novelefficient.Mail"%>


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
      <li><a  href="userhome.jsp">HOME</a></li>
      <li><a href="user_view.jsp">View Data</a></li>   
        
      <li><a class="active" href="user_download.jsp">Download Files</a></li>
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
           <p> We live in a digital world where every detail of our information is being transferred from one smart device to another via cross-platform, third-party cloud services. Smart technologies, such as, Smartphones are playing dynamic roles in order to successfully complete our daily routines and official tasks that require access to all types of critical data. Before the advent of these smart technologies, securing critical information was quite a challenge. However, after the advent and global adoption of such technologies, information security has become one of the primary and most fundamental task for security professionals. The integration of social media has made this task even more challenging to undertake successfully. To this day, there are plentiful studies in which numerous authentication and security techniques were proposed </p>
         </div>
          <div class="image"> <a href="#"><img src="css/images/logo.gif" alt="" /></a> </div>
          <div class="cl">&nbsp;</div>
        </li>
        <li>
          <div class="info">
           <p>developed for Smartphone and cloud computing technologies. These studies have successfully addressed multiple authentication threats and other related issues in existing Smartphone and cloud computing technologies. However, to the best of our understanding and knowledge, these studies lack many aspects in terms of authentication attacks, logical authentication analysis and the absence of authentication implementation scenarios. Due to these authentication anomalies and ambiguities, such studies cannot be fully considered for successful implementation.
</p>
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
<%
String fname = null;
    String fkey = null;
    String file = null;
    
    String user = session.getAttribute("email").toString();
String filename = request.getParameter("fname");
String typee = request.getParameter("typee");
String skey = request.getParameter("key");
Connection con=Dbconnection.getConnection();
 Statement st5 = con.createStatement();
            ResultSet rt5 = st5.executeQuery("select * from upload where filename='" + filename + "' ");
            if (rt5.next()) {
                fname = rt5.getString("filename");
                fkey = rt5.getString("skey");
                file = rt5.getString("file");
               
            } 
   String sql = "select * from request where skey = '"+skey+"' and filename = '"+filename+"'";
   Statement st = con.createStatement();
   ResultSet rs = st.executeQuery(sql);
   if(rs.next()){
       %>
   
       <center><p><font size="5" color="black">Download File </font></p><br/></center>
     
    <form action="user_download3.jsp"  method="post"  >
    <center><table width="371" border="0" >

    <tr><td><font color="black"> File Name :</td>
    <td><input type="text" name="filename"  readonly="" value="<%=fname%>" /></td></tr>
    
    <tr><td><font color="black"> Content Type :</td>
        <td><textarea  name="typee"  readonly="" value="" ><%=file%></textarea></td></tr>
    
   
    <td><input type="hidden" name="file"  readonly="" value="<%=file%>" /></td></tr>
    
 
    <td rowspan="2">
    <td><br><input type="submit" name="submit" value="Download" /></td>
   
    </td>
    <tr></tr>      
    </table></center>
    </form>    
       
       <%
       //  response.setHeader("Content-Disposition", "attachment;filename=\"" + filename + "\"");
        //   out.write(file);
           
   }
   else{
       
       
       
       PreparedStatement ps=con.prepareStatement("update user set status = 'Attacker' where email = '"+user+"'");
   System.out.println(ps);
       
       
       
       
       
       
       
       
       
       
       response.sendRedirect("logout.jsp?msgg=Failed"); 
   }

%>

          
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