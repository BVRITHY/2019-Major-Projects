
       <%
           
          String filename = request.getParameter("filename");
          String file = request.getParameter("file");
           
         response.setHeader("Content-Disposition", "attachment;filename=\"" + filename + "\"");
          out.write(file);
           
  

%>