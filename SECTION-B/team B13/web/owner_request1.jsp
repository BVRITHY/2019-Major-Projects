<%@page import="java.time.format.DateTimeFormatter"%>
<%@page import="java.time.LocalDate"%>
<%@page import="java.sql.*"%>
<%@page import="novelefficient.Dbconnection"%>
<%@page import="novelefficient.Mail"%>
<%@ page session="true" %>
    <%
    String email = request.getParameter("user");
    String filename = request.getParameter("filename"); 
   // String owner = session.getAttribute("username").toString();
 
   // String date = request.getParameter("uploadeddt"); 
    String key = null;
    
    
    
    try{
   
        
    Connection con=Dbconnection.getConnection();
    
    
    
    String sql = "select * from upload where filename = '"+filename+"' ";
    Statement st1 = con.createStatement();
    ResultSet rs1 = st1.executeQuery(sql);
    if(rs1.next()){
    
     key = rs1.getString("skey");
    
    }
    PreparedStatement ps=con.prepareStatement("update request set skey = '"+key+"',status = 'sent' where email = '"+email+"' and filename = '"+filename+"' ");
    System.out.println(ps);
    Mail m = new Mail();
    
          String msg ="File Name:"+filename+"\ndecryption key :"+key;
          m.secretMail(msg,filename,email);
    
    int i=ps.executeUpdate();
    if(i>0)
    {
    response.sendRedirect("manager_request.jsp?m1=Registered");
    }
    else{
    response.sendRedirect("managert_request.jsp?m2=Failed");    
    }
    %>
    <%
    }

    catch(Exception e)
    {
        
       out.println(e);
          
    }
    %>