<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<title>Add Posts</title>

<%@ include file = "connect.jsp" %>
<%@ page import = "java.io.*"%>
<%@ page import = "java.util.*" %>
<%@ page import = "java.util.Date" %>
<%@ page import = "com.oreilly.servlet.*"%>
<%@ page import = "java.text.SimpleDateFormat" %>
<%@ page import = "javax.crypto.Cipher" %> 
<%@ page import = "org.bouncycastle.util.encoders.Base64" %>
<%@ page import = "javax.crypto.spec.SecretKeySpec" %>
<%@ page import = "java.security.KeyPairGenerator,java.security.KeyPair,java.security.Key" %>
<%@ page import = "java.security.MessageDigest,java.security.DigestInputStream" %>
<%@ page import = "java.math.BigInteger" %>

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
.style20 {
	color: #FF0000;
	font-size: 16px;
	font-weight: bold;
}
.style21 {
	font-size: 18px;
	color: #FF0000;
	font-weight: bold;
}
.style22 {
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
          <li><a href="index.html"><span>Home </span></a></li>
          <li class="active"><a href="admin_Login.jsp"><span>Admin</span></a></li>
          <li><a href="user_Login.jsp"><span>User</span></a></li>
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
          <h2 class="style22">Organ Donation Status !!! </h2>
          
          <div class="clr"></div>
          
          <p>&nbsp;</p>
          <p>
		  
		  <%
				try {
				
					ArrayList list = new ArrayList();
					ServletContext context = getServletContext();
					String dirName =context.getRealPath("Gallery/");
					String paramname=null;
					String file=null;
					String organ_name=null,dname=null,age=" ",bg=null,height=null,weight=null,utype=null;
					String ee=null;
					String checkBok=" ";
					int ff=0;
					String bin = "";
					FileInputStream fs=null;
					File file1 = null;	
					
						MultipartRequest multi = new MultipartRequest(request, dirName,	10 * 1024 * 1024); // 10MB
						Enumeration params = multi.getParameterNames();
						while (params.hasMoreElements()) 
						{
							paramname = (String) params.nextElement();
							if(paramname.equalsIgnoreCase("organ_name"))
							{
								organ_name=multi.getParameter(paramname);
							}
							if(paramname.equalsIgnoreCase("dname"))
							{
								dname=multi.getParameter(paramname);
							}
							if(paramname.equalsIgnoreCase("age"))
							{
								age=multi.getParameter(paramname);
							}
							if(paramname.equalsIgnoreCase("bg"))
							{
								bg=multi.getParameter(paramname);
							}
							if(paramname.equalsIgnoreCase("height"))
							{
								height=multi.getParameter(paramname);
							}
							
							if(paramname.equalsIgnoreCase("weight"))
							{
								weight=multi.getParameter(paramname);
							}
							
							if(paramname.equalsIgnoreCase("utype"))
							{
								utype=multi.getParameter(paramname);
							}
							}
					
							
							String str = "select * from organ_donated_details where organ_name='"+organ_name+"' and donar_name='"+dname+"' ";
							Statement st = connection.createStatement();
							ResultSet rs = st.executeQuery(str);
							if(rs.next())
							{
							%><p class="style21">Donated Already </p>
							  <p align="right"><a href="Donor_Add_Organ_Donating_Details.jsp">Back</a></p>
							<%
							}
							else
							{
							
							String luser=(String)application.getAttribute("cuser");
							
							
							SimpleDateFormat sdfDate = new SimpleDateFormat("dd/MM/yyyy");
		   	           SimpleDateFormat sdfTime = new SimpleDateFormat("HH:mm:ss");

			           Date now = new Date();

			           String strDate = sdfDate.format(now);
			           String strTime = sdfTime.format(now);
			           String dt = strDate + "   " + strTime;
			
					 
					String filename="filename.txt";
      				PrintStream p = new PrintStream(new FileOutputStream(filename));
					p.print(new String(organ_name));
			
					MessageDigest md = MessageDigest.getInstance("SHA1");
					FileInputStream fis11 = new FileInputStream(filename);
					DigestInputStream dis1 = new DigestInputStream(fis11, md);
					BufferedInputStream bis1 = new BufferedInputStream(dis1);
					//Read the bis so SHA1 is auto calculated at dis
					while (true) {
						int b1 = bis1.read();
						if (b1 == -1)
							break;
					}
 
					BigInteger bi1 = new BigInteger(md.digest());
					String spl1 = bi1.toString();
					String h1 = bi1.toString(16);
							
							
							
							String keys1 = "ef50a0ef2c3e3a5f";
      		                KeyPairGenerator kg1 = KeyPairGenerator.getInstance("RSA");
				            Cipher encoder1 = Cipher.getInstance("RSA");
				            KeyPair kp1 = kg1.generateKeyPair();
				            Key pubKey1 = kp1.getPublic();
				            byte[] pub1 = pubKey1.getEncoded();
				           // String encrypted1 = new String(Base64.encode(desc.getBytes()));
			             //   String encrypted2 = new String(Base64.encode(uses.getBytes()));
							
							
							
							String status ="Processing";
							String tstatus ="Waiting";
                            PreparedStatement ps=connection.prepareStatement("insert into organ_donated_details(							 			organ_name,donar_name,donor_age,blood_group,height,weight,ruser_type,registered_date,donation_status,hcode,tstatus,loginuser) values(?,?,?,?,?,?,?,?,?,?,?,?)");

							ps.setString(1,organ_name);
							ps.setString(2,dname);
							ps.setString(3,age);	
							ps.setString(4,bg);
							ps.setString(5,height);
							ps.setString(6,weight);
							ps.setString(7,utype);
							ps.setString(8,dt);
							ps.setString(9,status);
							ps.setString(10,h1);
							ps.setString(11,tstatus);
							ps.setString(12,luser);
							
							ps.executeUpdate();
							
							%>
							   <p class="style20">Donors Details Added Sucessfully</p>
							   <p align="right"><a href="Donor_Add_Organ_Donating_Details.jsp">Back</a></p>
							<%
							
						  }  
						  }
						catch (Exception e) 
						{
							out.println(e.getMessage());
						}
					%>
					
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
          <li><a href="admin_Main.jsp"><span>Donor Main </span></a></li>
          <li><a href="admin_Login.jsp"><span>Log Out</span></a></li>
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
