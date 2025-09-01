package banksystem;

import java.awt.*;
import javax.swing.*;
import java.sql.*;

public class Shujuk {
	static int ok ;
	static double a=xianshi();
	public Shujuk() {} 
	
	static public class touming{			//依赖关系
		public void touming(JButton button) {
			button.setBackground(Color.white);
			button.setOpaque(false);
			button.setFont(new Font("楷体",Font.BOLD,25));
			}
		public void touming(JPanel panel) {
			panel.setBackground(Color.pink);
			panel.setOpaque(false);
			panel.setFont(new Font("楷体",Font.BOLD,15));
			}
		}
	public static int checkUser(String k,String m)  {   //输入ID和密码
    	try{         //1.注册驱动              
    		Class.forName("com.mysql.cj.jdbc.Driver");        //2.连接数据库           
    		Connection conn =  DriverManager.getConnection("jdbc:mysql://localhost:3306/atm","root","123456");
    		String temp_ID=k;       
    		String temp_pass=m;     
    		String sql_user="select userID,userPW from users  where UserID=? and UserPW=?";                   
    		PreparedStatement ps=conn.prepareStatement(sql_user); //    //封装登入数据    
    		ps.setString (1,temp_ID);         
    		ps.setString (2,temp_pass);    
    		ResultSet rs=ps.executeQuery();  //返回结果集           
    		if(rs.next()==true) {              
    			conn.close();
    			return 1;
    			} 
    		}       
    	catch(Exception sqle){              
    		System.err.println(sqle);    //顺序输出异常      
    		return 0;
    		} 
    	return 0;
    	}
    
	public static int shanchu(String mm,String id)  { 
		try{       
				Class.forName("com.mysql.cj.jdbc.Driver");         
				Connection conn = DriverManager.getConnection("jdbc:mysql://localhost:3306/atm","root","123456");        
				Statement stmt=conn.createStatement(); 
				String sql="delete from users  where UserID='"+Integer.parseInt(id)+"' and  UserPw= '"+Integer.parseInt(mm)+"'";   
				int rs=stmt.executeUpdate(sql);  //受修改影响的行数      
				conn.close(); 
				if(rs>0)
					return 1;
				else 
					return 0;
			}       
		catch(Exception sqle) {             
			System.err.println(sqle);
			return -1; 
			} 
}
	
public static int zhucezh(String name,String sex,String kahao,String mima,String phone)  {
	try{      //1.注册驱动 
		Class.forName("com.mysql.cj.jdbc.Driver");      //2.连接数据库     
		Connection conn = DriverManager.getConnection("jdbc:mysql://localhost:3306/atm","root","123456");   
		Statement stmt=conn.createStatement();  
		String sql="insert into users  values(?,?,?,?,?,?)";  //通配符
		PreparedStatement ps=(PreparedStatement) conn.prepareStatement(sql); //封装注册数据 
		ps.setString(1,kahao);  //设置入库顺序
		ps.setString(2,name);  
		ps.setString(3,mima);  
		ps.setString(4,phone);  
		ps.setString(5,sex);  
		ps.setInt(6,0);  
		ok=ps.executeUpdate();  //受影响行数
		conn.close();  
		return ok;  
	}     
catch(Exception sqle){             
	System.err.println(sqle);           
	return 0;     
		} 
	}	  
public static int chagai(String name,String sex,String phone)  {
	try{ 
		//1.注册驱动            
		Class.forName("com.mysql.cj.jdbc.Driver");       
		//2.连接数据库         
		Connection conn = DriverManager.getConnection("jdbc:mysql://localhost:3306/atm","root","123456");       
		Statement stmt=conn.createStatement();      
		ResultSet rs=stmt.executeQuery("select * from users  where UserID='"+Integer.parseInt(Denlu.Kahao.getText())+"'");        
		if(rs.next()==true) {       
			stmt.executeUpdate("Update users  set Usersex='"+sex+"',Username='"+name+"',Userphone='"+phone+"' where UserID='"+Integer.parseInt(Denlu.Kahao.getText())+"'");           
			conn.close();      
			return 1;      
			}   
		else
			return 0;
	}      
catch(Exception sqle){              
	System.err.println(sqle);            
	return -1;      
	}   
}    

public static int gaimi(String y,String x)  {   
	long p;      
	p=checkUser(Denlu.Kahao.getText(),y);    
	if(p==1) {
		try {       //1.注册驱动       
			Class.forName("com.mysql.cj.jdbc.Driver");       //2.连接数据库         
			Connection conn =  DriverManager.getConnection("jdbc:mysql://localhost:3306/atm","root","123456");        
			Statement stmt=conn.createStatement(); 
			ResultSet rs=stmt.executeQuery("select * from users  where UserID='"+Integer.parseInt(Denlu.Kahao.getText())+"'");  
			if(rs.next()==true){       
				stmt.executeUpdate("Update users  set UserPW='"+x+"' where UserID='"+Integer.parseInt(Denlu.Kahao.getText())+"'");           
				conn.close();      
				} 
			 	return 1;
			}       
		catch(Exception sqle){               
				System.err.println(sqle);            
				return -1;     
				}  
			}
	else 
		return 0;      
}     

public static double xianshi()  {   
	double j = 0;    
	try{       //1.注册驱动       
		Class.forName("com.mysql.cj.jdbc.Driver");       //2.连接数据库         
		Connection conn =  DriverManager.getConnection("jdbc:mysql://localhost:3306/atm","root","123456");
		Statement stmt=conn.createStatement();       
		ResultSet rs=stmt.executeQuery("select * from users  where UserID='"+Integer.parseInt(Denlu.Kahao.getText())+"'");         
		if(rs.next()==true)  {          
			j=rs.getInt("Useryue");         
			conn.close();  
			return j; 
			} 
		}       
	catch(Exception sqle){               
		System.err.println(sqle);            
			return -1;      
			}   
	return 0;   
	}   

public static int qukuan(long k,long j)  {    
	try{        //1.注册驱动       
		Class.forName("com.mysql.cj.jdbc.Driver");       //2.连接数据库         
		Connection conn =  DriverManager.getConnection("jdbc:mysql://localhost:3306/atm","root","123456");        
		Statement stmt=conn.createStatement();       
		ResultSet rs=stmt.executeQuery("select * from users  where UserID='"+k+"'");         
		if(rs.next()==true) {    
			j=rs.getInt("Useryue")-j;    //取款后剩余金额  
			if(j<0)       
				return 0;      
			else
				stmt.executeUpdate("Update users  set Useryue='"+j+"' where UserID='"+k+"'");           
			conn.close();      
			return 1;      
			}    
		}      
	catch(Exception sqle){               
		System.err.println(sqle);            
		return -1;     
		}   
		return 0;             
}
public static int cunkuan(long k,long j)  {    
	try{        //1.注册驱动       
		Class.forName("com.mysql.cj.jdbc.Driver");       //2.连接数据库         
		Connection conn =  DriverManager.getConnection("jdbc:mysql://localhost:3306/atm","root","123456");        
		Statement stmt=conn.createStatement();       
		ResultSet rs=stmt.executeQuery("select * from users  where UserID='"+k+"'");         
		if(rs.next()==true) {    
			j=rs.getInt("Useryue")+j;              
			stmt.executeUpdate("Update    users  set  Useryue='"+j+"' where UserID='"+k+"'");    
			conn.close();      
			return 1;      
			}    
		}   
           catch(Exception sqle){              
        	   System.err.println(sqle);            
        	   return -1;     
        	   }   
           return 0;  
        }     

public static int zhuanzhang(long k,long j)
	{   
        long i = 0;   
        long p = 0;    
        i=Shujuk.cunkuan(k, 0);   
        if(i==1) {    
        	p=Shujuk.qukuan(Integer.parseInt(Denlu.Kahao.getText()), j);    
        	if(p==1) { 
        		try {  //1.注册驱动 
        			Class.forName("com.mysql.cj.jdbc.Driver");       //2.连接数据库         
				    Connection conn =  DriverManager.getConnection("jdbc:mysql://localhost:3306/atm","root","123456");        
				    Statement stmt=conn.createStatement();       
				    ResultSet rs=stmt.executeQuery("select * from users  where UserID='"+k+"'");         
				    if(rs.next()) {    
				    	j=rs.getInt("Useryue")+j;             
				    	stmt.executeUpdate("Update    users  set  Useryue='"+j+"' where UserID='"+k+"'");      
				    	conn.close();      
				    	return 1;      
				    	}   
        			}       
			    catch(Exception sqle){               
			    	System.err.println(sqle);            
			    	return -1;      
			    	}   
        		 }
        	else
        		return 2;     
			 }
        return 0;     //卡号不存在
		 }
}
    
