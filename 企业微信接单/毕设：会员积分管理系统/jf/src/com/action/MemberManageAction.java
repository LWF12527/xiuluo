package com.action;



import java.io.IOException;
import java.util.List;

import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;

import com.bean.MemberManageBean;
import com.bean.SystemBean;
import com.util.Constant;
import com.util.Filter;
public class MemberManageAction extends HttpServlet {

	/**
	 * Constructor of the object.
	 */
	public MemberManageAction() {
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
		String sysdir = new SystemBean().getDir();
		HttpSession session = request.getSession();
		try{
			String username2 = (String)session.getAttribute("user");
			if(username2 == null){
				request.getRequestDispatcher("error.jsp").forward(request, response);
			}
			else{
				String method = Filter.escapeHTMLTags(request.getParameter("method").trim());
				MemberManageBean mmBean = new MemberManageBean();
				if(method.equals("DELMEMBER")||method.equals("DELCO")||method.equals("DELTODAY")
						||method.equals("DELALLCLOSE")||method.equals("DELALLUSE")){//ɾ�����Ժ�̨����ҳ��Ļ�Ա
					String check[] = request.getParameterValues("checkit");
					if(check == null){
						if(method.equals("DELMEMBER")){//�������и��˻�Աҳ��
							request.setAttribute("message", "��ѡ��Ҫɾ���ļ�¼��");
							request.getRequestDispatcher(sysdir+"/member/person.jsp").forward(request, response);
						}
						else if(method.equals("DELCO")){//����������ҵ��Աҳ��
							request.setAttribute("message", "��ѡ��Ҫɾ���ļ�¼��");
							request.getRequestDispatcher(sysdir+"/member/co.jsp").forward(request, response);
						}
						else if(method.equals("DELTODAY")){//���Խ���ע���Աҳ��
							request.setAttribute("message", "��ѡ��Ҫɾ���ļ�¼��");
							request.getRequestDispatcher(sysdir+"/member/today.jsp").forward(request, response);
						}
						else if(method.equals("DELALLCLOSE")){//�������ж����Աҳ��
							request.setAttribute("message", "��ѡ��Ҫɾ���ļ�¼��");
							request.getRequestDispatcher(sysdir+"/member/close.jsp").forward(request, response);
						}
						else if(method.equals("DELALLUSE")){//�����������û�Աҳ��
							request.setAttribute("message", "��ѡ��Ҫɾ���ļ�¼��");
							request.getRequestDispatcher(sysdir+"/member/using.jsp").forward(request, response);
						}
					}
					else{
						int id[]= new int[check.length];
						for(int i = 0;i<check.length;i++){
							int s = Integer.parseInt(check[i]);				
							id[i] = s;
						}
						int flag = mmBean.delMember(id);
						if(flag == Constant.SUCCESS){
							if(method.equals("DELMEMBER")){//�������и��˻�Աҳ��
								request.getRequestDispatcher(sysdir+"/member/person.jsp").forward(request, response);
							}
							else if(method.equals("DELCO")){//����������ҵ��Աҳ��
								request.getRequestDispatcher(sysdir+"/member/co.jsp").forward(request, response);
							}
							else if(method.equals("DELTODAY")){//���Խ���ע���Աҳ��
								request.getRequestDispatcher(sysdir+"/member/today.jsp").forward(request, response);
							}
							else if(method.equals("DELALLCLOSE")){//�������ж����Աҳ��
								request.getRequestDispatcher(sysdir+"/member/close.jsp").forward(request, response);
							}
							else if(method.equals("DELALLUSE")){//�����������û�Աҳ��
								request.getRequestDispatcher(sysdir+"/member/using.jsp").forward(request, response);
							}
						}
						else{
							if(method.equals("DELMEMBER")){//�������и��˻�Աҳ��
								 request.getRequestDispatcher(sysdir+"/member/person.jsp").forward(request, response);
							}
							else if(method.equals("DELCO")){//����������ҵ��Աҳ��
								 request.getRequestDispatcher(sysdir+"/member/co.jsp").forward(request, response);
							}
							else if(method.equals("DELTODAY")){//���Խ���ע���Աҳ��
								 request.getRequestDispatcher(sysdir+"/member/today.jsp").forward(request, response);
							}
							else if(method.equals("DELALLCLOSE")){//�������ж����Աҳ��
								 request.getRequestDispatcher(sysdir+"/member/close.jsp").forward(request, response);
							}
							else if(method.equals("DELALLUSE")){//�����������û�Աҳ��
								 request.getRequestDispatcher(sysdir+"/member/using.jsp").forward(request, response);
							}
						}
					}
				}
				else if(method.equals("CLOSE")){
					String id=request.getParameter("id").trim();
					int flag=mmBean.closeMember(Integer.parseInt(id));
					if(flag==Constant.SUCCESS){
						request.setAttribute("message", "�����ɹ���");
						request.getRequestDispatcher("admin/member/person.jsp").forward(request, response);
					}
					else{
						request.setAttribute("message", "ϵͳά���У����Ժ����ԣ�");
						request.getRequestDispatcher("admin/member/person.jsp").forward(request, response);
					}
				}
				else{
					request.getRequestDispatcher("error.jsp").forward(request, response);
				}
			}
		}catch(Exception e){
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
