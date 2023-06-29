<%@page import="javax.imageio.ImageIO"%>
<%@page import="java.awt.image.BufferedImage"%>
<%@page import="java.io.File"%>
<%@page import="java.util.Random"%>
<%@page import="java.sql.*"%>
<%@page import="novelefficient.Dbconnection"%>
<%@ page session="true" %>
<%@page import="novelefficient.Mail"%>

<%
    String username = request.getParameter("username");
    String password = request.getParameter("password");
    
   
    try{
       
    Connection con=Dbconnection.getConnection();
  //  Random s = new Random();
  //  int otp = s.nextInt(10000 - 5000) +25000 ;
    
    Statement st = con.createStatement();
    ResultSet rs = st.executeQuery("select * from user where email= '"+username+"' and password='"+password+"' and status!= 'Blocked'");
    if(rs.next())
    {

    String user = rs.getString("username");
    session.setAttribute("user",user);
    String email = rs.getString("email");
    session.setAttribute("email",email);
    
  
            response.sendRedirect("userhome.jsp?m1=Success");
            
        } else {
    
     
            response.sendRedirect("user.jsp?m2=Failed");
           
        }
                   
          
          
          
   
    
 
    }
    catch(Exception e)
    {
    System.out.println("Error in emplogact"+e.getMessage());
    }
%>