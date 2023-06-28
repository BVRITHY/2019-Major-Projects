	<%@ include file="connect.jsp" %>
 	<%
  		
   	try {
		   
			String type=request.getParameter("type");
			String id=request.getParameter("id");
			String str = "Processed";
			String str1 = "Transplantation Done";
			
			if(type.equals("rprocess"))
			{
       		Statement st1 = connection.createStatement();
       		String query1 ="update organ_transplantation_request_details set requested_status='"+str+"' where si_no="+id+" ";
	   		st1.executeUpdate (query1);
			connection.close();
			response.sendRedirect("A_View_All_Patient_Transplantation_Requested_Details.jsp");  
			}
			else if(type.equals("otransplant"))
			{
			Statement st1 = connection.createStatement();
       		String query1 ="update organ_transplantation_request_details set tstatus='"+str1+"' where si_no="+id+" ";
	   		st1.executeUpdate (query1);
			connection.close();
			response.sendRedirect("A_View_All_Patient_Transplantation_Requested_Details.jsp");  
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
