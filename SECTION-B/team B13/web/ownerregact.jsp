<%@page import="java.sql.*"%>
<%@page import="novelefficient.Dbconnection"%>
<%@ page session="true" %>
    <%
    String username = request.getParameter("username");
    String password = request.getParameter("password"); 
    String email = request.getParameter("email");
 
    String gender = request.getParameter("gender"); 
    String address = request.getParameter("address");
    String mobile = request.getParameter("mobile");
    String image = request.getParameter("image");
    int ik = 0;
    
    try{
   
        
    Connection con=Dbconnection.getConnection();
    PreparedStatement ps=con.prepareStatement("insert into owner values(?,?,?,?,?,?,?,?,?)");

    ps.setString(1,username);
    ps.setString(2,password);
    ps.setString(3,email);
  
    ps.setString(4,gender);
    ps.setString(5,address);
    ps.setString(6,mobile);
    ps.setString(9,image);
    ps.setString(7,"status");
   ps.setInt(8, ik);
    
    int i=ps.executeUpdate();
    if(i>0)
    {
    response.sendRedirect("owner.jsp?msg=Registered");
    }
    else{
    response.sendRedirect("ownerreg.jsp?msg1=Failed");    
    }
    %>
    <%
    }

    catch(Exception e)
    {
        
       out.println(e);
          
    }
    %>