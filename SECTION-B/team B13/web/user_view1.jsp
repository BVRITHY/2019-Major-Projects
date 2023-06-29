<%@page import="java.time.format.DateTimeFormatter"%>
<%@page import="java.time.LocalDate"%>
<%@page import="java.sql.*"%>
<%@page import="novelefficient.Dbconnection"%>
<%@ page session="true" %>
    <%
    String username = session.getAttribute("email").toString();
    String filename = request.getParameter("filename"); 
    String owner = request.getParameter("email"); 
    String date = request.getParameter("cdate"); 
    String cipher = request.getParameter("data");
    String file = request.getParameter("file");
    String status = "pending";
    int id = 0;
    
    try{
   
        
    Connection con=Dbconnection.getConnection();
    PreparedStatement ps=con.prepareStatement("insert into request values(?,?,?,?,?,?,?,?)");
    ps.setInt(1,id);
    ps.setString(2,filename);
    ps.setString(3,username);
    ps.setString(4,cipher);  
    ps.setString(5,file);
    ps.setString(6,status);  
    ps.setString(7,owner);
    ps.setString(8,status);
   
    
    int i=ps.executeUpdate();
    if(i>0)
    {
    response.sendRedirect("user_view.jsp?msg=Registered");
    }
    else{
    response.sendRedirect("user_view.jsp?msg1=Failed");    
    }
    %>
    <%
    }

    catch(Exception e)
    {
        
       out.println(e);
          
    }
    %>