<%@page import="java.sql.*"%>
<%@page import="novelefficient.Dbconnection"%>
<%@ page session="true" %>
<%
    String username = request.getParameter("username");
    String password = request.getParameter("password");
    String cloud = request.getParameter("cloud");
    try{
       
    Connection con=Dbconnection.getConnection();
    Statement st = con.createStatement();
    ResultSet rs = st.executeQuery("select * from cloud where username= '"+username+"' and password='"+password+"'");
    if(rs.next())
    {
    
    session.setAttribute("cloud",cloud);
                   
    response.sendRedirect("cloudhome.jsp?msg=Login_Successfull");
    }
    else 
    {
    response.sendRedirect("cloud.jsp?m1=LoginFail");
    }
    }
    catch(Exception e)
    {
    System.out.println("Error in idmlogact"+e.getMessage());
    }
%>