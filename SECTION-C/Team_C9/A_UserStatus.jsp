	<%@ include file="connect.jsp" %>
 	<%
  		
   	try {
		   
			String type=request.getParameter("type");
			String id=request.getParameter("id");
			String str = "Authorized";
			
			if(type.equals("user"))
			{
       		Statement st1 = connection.createStatement();
       		String query1 ="update user set status='"+str+"' where id="+id+" ";
	   		st1.executeUpdate (query1);
			connection.close();
			response.sendRedirect("A_AuthorizeUsers.jsp");  
			}
			else if(type.equals("cuser"))
			{
			Statement st1 = connection.createStatement();
       		String query1 ="update cuser set status='"+str+"' where id="+id+" ";
	   		st1.executeUpdate (query1);
			connection.close();
			response.sendRedirect("A_AuthorizeDonorUsers.jsp");  
			}
			else
			{
			
			}
	   		
       	}
      	catch(Exception e)
     	{
			out.println(e.getMessage());
   		}
   		
	%>
