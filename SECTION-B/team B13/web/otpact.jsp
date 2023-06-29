<%@page import="java.util.Random"%>
<%@page import="java.sql.*"%>
<%@page import="novelefficient.Dbconnection"%>
<%@ page session="true" %>
<%@page import="novelefficient.Mail"%>
<%
    String otp = request.getParameter("otp");
    
    try{
       
    Connection con=Dbconnection.getConnection();
    
    Statement st = con.createStatement();
    ResultSet rs = st.executeQuery("select * from owner where otp= '"+otp+"' ");
    if(rs.next())
    {

    response.sendRedirect("ownerhome.jsp?msg=Success");
    }
    else 
    {
    response.sendRedirect("otp.jsp?msg1=LoginFail");
    }
    }
    catch(Exception e)
    {
    System.out.println("Error in emplogact"+e.getMessage());
    }
%>