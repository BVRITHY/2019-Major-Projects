package org.apache.jsp;

import javax.servlet.*;
import javax.servlet.http.*;
import javax.servlet.jsp.*;
import java.time.format.DateTimeFormatter;
import java.time.LocalDate;
import java.sql.*;
import novelefficient.Dbconnection;
import novelefficient.Mail;

public final class owner_005frequest1_jsp extends org.apache.jasper.runtime.HttpJspBase
    implements org.apache.jasper.runtime.JspSourceDependent {

  private static final JspFactory _jspxFactory = JspFactory.getDefaultFactory();

  private static java.util.List<String> _jspx_dependants;

  private org.glassfish.jsp.api.ResourceInjector _jspx_resourceInjector;

  public java.util.List<String> getDependants() {
    return _jspx_dependants;
  }

  public void _jspService(HttpServletRequest request, HttpServletResponse response)
        throws java.io.IOException, ServletException {

    PageContext pageContext = null;
    HttpSession session = null;
    ServletContext application = null;
    ServletConfig config = null;
    JspWriter out = null;
    Object page = this;
    JspWriter _jspx_out = null;
    PageContext _jspx_page_context = null;

    try {
      response.setContentType("text/html");
      pageContext = _jspxFactory.getPageContext(this, request, response,
      			null, true, 8192, true);
      _jspx_page_context = pageContext;
      application = pageContext.getServletContext();
      config = pageContext.getServletConfig();
      session = pageContext.getSession();
      out = pageContext.getOut();
      _jspx_out = out;
      _jspx_resourceInjector = (org.glassfish.jsp.api.ResourceInjector) application.getAttribute("com.sun.appserv.jsp.resource.injector");

      out.write("\n");
      out.write("\n");
      out.write("\n");
      out.write("\n");
      out.write("\n");
      out.write("\n");
      out.write("    ");

    String email = request.getParameter("email");
    String filename = request.getParameter("filename"); 
    String owner = request.getParameter("owner");
 
   // String date = request.getParameter("uploadeddt"); 
    String key = null;
    
    
    
    try{
   
        
    Connection con=Dbconnection.getConnection();
    
    
    
     String sql = "select * from upload where filename = '"+filename+"' and email = '"+owner+"'";
    Statement st1 = con.createStatement();
    ResultSet rs1 = st1.executeQuery(sql);
    if(rs1.next()){
    
     key = rs1.getString("skey");
    
    }
    PreparedStatement ps=con.prepareStatement("update request set skey = '"+key+"',status = 'sent' where email = '"+email+"' and filename = '"+filename+"' and owner = '"+owner+"'");
    
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
    
      out.write("\n");
      out.write("    ");

    }

    catch(Exception e)
    {
        
       out.println(e);
          
    }
    
    } catch (Throwable t) {
      if (!(t instanceof SkipPageException)){
        out = _jspx_out;
        if (out != null && out.getBufferSize() != 0)
          out.clearBuffer();
        if (_jspx_page_context != null) _jspx_page_context.handlePageException(t);
        else throw new ServletException(t);
      }
    } finally {
      _jspxFactory.releasePageContext(_jspx_page_context);
    }
  }
}
