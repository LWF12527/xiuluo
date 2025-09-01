package banksystem;

import javax.swing.*;   
import java.awt.*; import java.awt.event.*; 
import java.sql.Connection; 
import java.sql.*;
public class Chagai extends JDialog{  
	TextField name=new TextField(20);  
	TextField sex=new TextField(20);  
	TextField kahao=new TextField(20); 
	TextField phone=new TextField(20);  
	public Chagai(JFrame m,String s){    
		super(m,s);        
		setBounds(350,150,400,350);       
		setVisible(true);   
		setDefaultCloseOperation(JDialog.DISPOSE_ON_CLOSE);       
		setResizable(false);       
		setLayout(null);
		
		//修改图标
        Toolkit tk=Toolkit.getDefaultToolkit();
    	Image img=tk.getImage("bank/tb.jpg");//登入成功关闭登录窗口，找图标和背景图片
    	setIconImage(img);

    	Container con = getContentPane();
        con.setBackground(Color.pink);
    	
		
		JLabel label1=new JLabel("客户个人信息查询与修改");      
		JLabel label2=new JLabel("姓    名：");      
		JLabel label3=new JLabel("性    别：");     
		JLabel label4=new JLabel("卡    号：");    
		JLabel label5=new JLabel("手机号  ：");         
		label1.setFont(new Font("宋体",Font.BOLD,20));    
		label2.setFont(new Font("宋体",Font.BOLD,13));    
		label3.setFont(new Font("宋体",Font.BOLD,13));    
		label4.setFont(new Font("宋体",Font.BOLD,13));    
		label5.setFont(new Font("宋体",Font.BOLD,13));    
		kahao.setEditable(false);   
		//卡号不可修改     
		
		JButton button1=new JButton("确定");
		JButton button2=new JButton("取消"); 
		button1.addActionListener(new ActionListener() { 
			public void actionPerformed (ActionEvent event) {     
				if(event.getActionCommand()=="确定"&&!(name.getText().equals(""))&&!(sex.getText().equals(""))&&!(phone.getText().equals(""))) 
				{      
					int x=Shujuk.chagai(name.getText(),sex.getText(),phone.getText());      
					System.out.println(x);         
					if(x==1){ 
						JOptionPane.showMessageDialog(Zhuye.z,"修改成功！");
						dispose();
						}         
					else if(x==0){ 
						JOptionPane.showMessageDialog(Zhuye.z,"修改出错！");
						dispose();
						}  
					else if(x==-1){ 
						JOptionPane.showMessageDialog(Zhuye.z,"系统出错！");
						dispose();
						} 
					}    
				else if(event.getActionCommand()=="确定"&&((name.getText().equals(""))||(sex.getText().equals(""))||(phone.getText().equals(""))))
					{
						JOptionPane.showMessageDialog(Zhuye.z,"请补全信息！");
					} 
			} 
		});   
		button2.addActionListener(new ActionListener() { 
			public void actionPerformed (ActionEvent event) {
					dispose();
				}
			});   
		JPanel p1=new JPanel();     
		JPanel p2=new JPanel();     
		JPanel p3=new JPanel();    
		JPanel p4=new JPanel();    
		JPanel p5=new JPanel();    
		JPanel p6=new JPanel(); 
		//将按钮透明
		Shujuk.touming a = new Shujuk.touming();//将类放在了Shujuk里
		a.touming(button1);
		a.touming(button2);
		//修改面板颜色及字体
		Shujuk.touming px = new Shujuk.touming();//类在了Shujuk里
		px.touming(p1);
		px.touming(p2);
		px.touming(p3);
		px.touming(p4);
		px.touming(p5);
		px.touming(p6);
		p1.setBounds(0,0,400,50);  
		p1.add(label1);   
		p2.setBounds(0,50,400,50);  
		p2.add(label2);   
		p2.add(name);  
		p3.setBounds(0,100,400,50); 
		p3.add(label3);  
	 	p3.add(sex);   
	 	p4.setBounds(0,150,400,50);  
	 	p4.add(label4);   
	 	p4.add(kahao);   
	 	p5.setBounds(0,200,400,50);   
	 	p5.add(label5);  
	 	p5.add(phone);   
	 	p6.setBounds(0,250,400,70);   
	 	p6.add(button1);   
	 	p6.add(button2);      
	 	add(p1);   
	 	add(p2);  
	 	add(p3);   
	 	add(p4);   
	 	add(p5);      
	 	add(p6);      
 	try{        
 		//1.注册驱动       
 		String driverClassName = "com.mysql.jdbc.Driver";         
 		Class.forName("com.mysql.jdbc.Driver");       //2.连接数据库        
 		Connection conn =  DriverManager.getConnection("jdbc:mysql://localhost:3306/banksql","root","258080");        
 		Statement stmt=conn.createStatement();
 		ResultSet rs=stmt.executeQuery("select * from tablename where UserID='"+Integer.parseInt(Denlu.Kahao.getText())+"'");        
	
		if(rs.next()){           
		name.setText(rs.getString("Username"));       
		sex.setText(rs.getString("Usersex"));       
		kahao.setText(rs.getString("UserID"));       
		phone.setText(rs.getString("Userphone"));           
		conn.close();    
		}    
	}       
 	catch(Exception sqle){               
 		System.err.println(sqle);              
 		JOptionPane.showMessageDialog(Zhuye.z,"系统故障，请稍后在试！");       
 		}            
 	setVisible(true);            
 	}
}
