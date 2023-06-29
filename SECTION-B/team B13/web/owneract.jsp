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
    Random s = new Random();
    int otp = s.nextInt(10000 - 5000) +25000 ;
    
    Statement st = con.createStatement();
    ResultSet rs = st.executeQuery("select * from owner where email= '"+username+"' and password='"+password+"'");
    if(rs.next())
    {

    String user = rs.getString("username");
    session.setAttribute("user",user);
    String email = rs.getString("email");
    session.setAttribute("email",email);
    
    PreparedStatement ps=con.prepareStatement("update owner set otp = "+otp+" where email = '"+username+"'");
    ps.executeUpdate();
    
    Mail m = new Mail();
          String msg ="User Name:"+username+"\nOTP :"+otp;
          m.secretMail(msg,email,email);
                   
    response.sendRedirect("otp.jsp");
    }
    else 
    {
    response.sendRedirect("owner.jsp?msg1=LoginFail");
    }
    }
    catch(Exception e)
    {
    System.out.println("Error in emplogact"+e.getMessage());
    }
%>