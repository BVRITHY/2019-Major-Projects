
<%@page import="java.sql.*"%>
<%@page import="novelefficient.Dbconnection"%>
<%@ page session="true" %>
    <%
  
        
    String email = request.getParameter("email");

    
    
    
    
    try{
     
        
    Connection con = null;
    con = Dbconnection.getConnection();
    PreparedStatement ps=con.prepareStatement("update user set status = 'Blocked' where email = '"+email+"'");
  
    ps.executeUpdate();
    
    int i=ps.executeUpdate();
    if(i>0)
    {
    response.sendRedirect("manager_owner.jsp?msg=Success");
    }
    else{
    response.sendRedirect("manager_owner.jsp?msg1=Failed");    
    }
    %>
    <%
    }

    catch(Exception e)
    {
            out.println(e.getMessage());
    }
    %>