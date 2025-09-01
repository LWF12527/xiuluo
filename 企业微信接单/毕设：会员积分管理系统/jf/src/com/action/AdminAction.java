package com.action;

import java.io.IOException;
import java.util.List;
import java.util.StringTokenizer;

import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;

import com.bean.AdminBean;
import com.bean.SystemBean;
import com.util.Constant;
import com.util.MD5;

public class AdminAction extends HttpServlet {

	/**
	 * Constructor of the object.
	 */
	public AdminAction() {
		super();
	}

	/**
	 * Destruction of the servlet. <br>
	 */
	public void destroy() {
		super.destroy(); // Just puts "destroy" string in log
		// Put your code here
	}

	/**
	 * The doGet method of the servlet. <br>
	 *
	 * This method is called when a form has its tag value method equals to get.
	 * 
	 * @param request the request send by the client to the server
	 * @param response the response send by the server to the client
	 * @throws ServletException if an error occurred
	 * @throws IOException if an error occurred
	 */
	public void doGet(HttpServletRequest request, HttpServletResponse response)
			throws ServletException, IOException {

		doPost(request,response);
	}

	/**
	 * The doPost method of the servlet. <br>
	 *
	 * This method is called when a form has its tag value method equals to post.
	 * 
	 * @param request the request send by the client to the server
	 * @param response the response send by the server to the client
	 * @throws ServletException if an error occurred
	 * @throws IOException if an error occurred
	 */
	public void doPost(HttpServletRequest request, HttpServletResponse response)
			throws ServletException, IOException {

		response.setContentType(Constant.CONTENTTYPE);
		request.setCharacterEncoding(Constant.CHARACTERENCODING);
		try{
			String method=request.getParameter("method").trim();
			AdminBean loginbean = new AdminBean();
			HttpSession session = request.getSession();
			session.setMaxInactiveInterval(1200);
			SystemBean systembean = new SystemBean();
			String sysdir = systembean.getDir();
			if(method.equals("one")){//admin��¼
				String username = request.getParameter("username");
				String password = request.getParameter("password");
				if(username == null||username.trim().equals("")){
					request.setAttribute("message", "����ȷ�����û�����");
					request.getRequestDispatcher(sysdir+"/login.jsp").forward(request, response);
				}
				else if(password == null||password.trim().equals("")){
					request.setAttribute("message", "���������룡");
					request.getRequestDispatcher(sysdir+"/login.jsp").forward(request, response);
				}
				else{
					String md5password = MD5.MD5(password);
					String agent = request.getHeader("user-agent"); 
					StringTokenizer st = new StringTokenizer(agent,";"); 
					String useros=st.nextToken();
					String loginip = request.getRemoteAddr();			
					int flag = loginbean.adminLogin(username,md5password, password,useros,loginip);
					switch (flag){
						case Constant.SUCCESS:
							List list = loginbean.getAdminInfo(username);
							session.setAttribute("user", username);
							session.setAttribute("list", list);
							request.getRequestDispatcher(sysdir+"/").forward(request, response);
							break;
						case Constant.NAME_ERROR:
							request.setAttribute("message", "�û���������ȷ�Ϲ���Ȩ�ޣ�");
							request.getRequestDispatcher(sysdir+"/login.jsp").forward(request, response);
							break;
						case Constant.PASSWORD_ERROR:
							request.setAttribute("message", "���������ȷ�Ϲ���Ȩ�ޣ�");
							request.getRequestDispatcher(sysdir+"/login.jsp").forward(request, response);
							break;
					}
				}
			}
			else if(method.equals("editpwd")){//admin edit password
				String username2 = (String)session.getAttribute("user");
				if(username2 == null){
					request.getRequestDispatcher("error.jsp").forward(request, response);
				}
				else{
					String oldpwd = MD5.MD5(request.getParameter("oldpwd").trim());
					String newpwd = MD5.MD5(request.getParameter("newpwd").trim());
					String username = (String)session.getAttribute("user");
					int flag = loginbean.editPassword(username, oldpwd, newpwd);
					switch (flag){
						case Constant.SUCCESS:
							request.setAttribute("message", "�����޸ĳɹ���");
							request.getRequestDispatcher(sysdir+"/system/editpwd.jsp").forward(request, response);
							break;
						case Constant.PASSWORD_ERROR:
							request.setAttribute("message", "ԭʼ���������ȷ��Ȩ�ޣ�");
							request.getRequestDispatcher(sysdir+"/system/editpwd.jsp").forward(request, response);
							break;
						case Constant.SYSTEM_ERROR:
							request.setAttribute("message", "ϵͳά���У����Ժ����ԣ�");
							request.getRequestDispatcher(sysdir+"/system/editpwd.jsp").forward(request, response);
							break;
					}
				}		
			}
			else if(method.equals("exit")){//admin exit
				String username2 = (String)session.getAttribute("user");
				if(username2 == null){
					request.getRequestDispatcher("error.jsp").forward(request, response);
				}
				else{
					session.removeAttribute("user");
					session.removeAttribute("list");
					System.gc();
					request.getRequestDispatcher("index.jsp").forward(request, response);
				}			
			}
			else if(method.equals("manager")){//add,update manager
				String username2 = (String)session.getAttribute("user");
				if(username2 == null){
					request.getRequestDispatcher("error.jsp").forward(request, response);
				}
				else{
					
						String username = request.getParameter("username").trim();
						String password = MD5.MD5(request.getParameter("password").trim());
						
						
						int flag = loginbean.addManager(username, password, "2", "1");
						if(flag == Constant.SUCCESS){
							request.setAttribute("message", "���ӹ���Ա�ɹ���");
							request.getRequestDispatcher(sysdir+"/system/user.jsp").forward(request, response);
						}
						else if(flag == Constant.SAME_NAME){
							request.setAttribute("username", username);
							request.setAttribute("message", "���û����Ѿ����ڣ�");
							request.getRequestDispatcher(sysdir+"/system/user.jsp").forward(request, response);
						}
						else{
							request.setAttribute("message", "ϵͳά���У����Ժ����ԣ�");
							request.getRequestDispatcher(sysdir+"/system/user.jsp").forward(request, response);
						}		
					
				}
			}
			else if(method.equals("delm")){//delete manager
				String username2 = (String)session.getAttribute("user");
				if(username2 == null){
					request.getRequestDispatcher("error.jsp").forward(request, response);
				}
				else{
					int id = Integer.parseInt(request.getParameter("id").trim());
					if(id == 1){
						request.setAttribute("message", "����ɾ��ԭʼ�ʺţ�");
						request.getRequestDispatcher(sysdir+"/system/user.jsp").forward(request, response);
					}
					else{
						int flag = loginbean.delManager(id);
						if(flag == Constant.SUCCESS){
							request.setAttribute("message", "ɾ���ɹ���");
							request.getRequestDispatcher(sysdir+"/system/user.jsp").forward(request, response);
						}	
						else{
							request.setAttribute("message", "ϵͳά���У����Ժ����ԣ�");
							request.getRequestDispatcher(sysdir+"/system/user.jsp").forward(request, response);
						}	
					}
				}			
			}
			else if(method.equals("dellog")){//delete login note
				String username2 = (String)session.getAttribute("user");
				if(username2 == null){
					request.getRequestDispatcher("error.jsp").forward(request, response);
				}
				else{
					String check[] = request.getParameterValues("checkit");
					if(check == null){
						request.setAttribute("message", "��ѡ��Ҫɾ���ļ�¼��");
						request.getRequestDispatcher(sysdir+"/system/log.jsp").forward(request, response);
					}
					else{
						int id[]= new int[check.length];
						for(int i = 0;i<check.length;i++){
							int s = Integer.parseInt(check[i]);				
							id[i] = s;
						}
						int flag = loginbean.delLog(id);
						if(flag == Constant.SUCCESS){
							request.setAttribute("message", "ɾ����¼�ɹ���");
							request.getRequestDispatcher(sysdir+"/system/log.jsp").forward(request, response);
						}
						else{
							request.setAttribute("message", "ϵͳά���У����Ժ����ԣ�");
							request.getRequestDispatcher(sysdir+"/system/log.jsp").forward(request, response);
						}
					}
				}			
			}
			else{//�޲�������ת������ҳ��
				request.getRequestDispatcher("error.jsp").forward(request, response);
			}
		}catch(Exception e){
			e.printStackTrace();
			request.getRequestDispatcher("error.jsp").forward(request, response);
		}
		
	}

	/**
	 * Initialization of the servlet. <br>
	 *
	 * @throws ServletException if an error occure
	 */
	public void init() throws ServletException {
		// Put your code here
	}

}
