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
		
		//�޸�ͼ��
        Toolkit tk=Toolkit.getDefaultToolkit();
    	Image img=tk.getImage("bank/tb.jpg");//����ɹ��رյ�¼���ڣ���ͼ��ͱ���ͼƬ
    	setIconImage(img);

    	Container con = getContentPane();
        con.setBackground(Color.pink);
    	
		
		JLabel label1=new JLabel("�ͻ�������Ϣ��ѯ���޸�");      
		JLabel label2=new JLabel("��    ����");      
		JLabel label3=new JLabel("��    ��");     
		JLabel label4=new JLabel("��    �ţ�");    
		JLabel label5=new JLabel("�ֻ���  ��");         
		label1.setFont(new Font("����",Font.BOLD,20));    
		label2.setFont(new Font("����",Font.BOLD,13));    
		label3.setFont(new Font("����",Font.BOLD,13));    
		label4.setFont(new Font("����",Font.BOLD,13));    
		label5.setFont(new Font("����",Font.BOLD,13));    
		kahao.setEditable(false);   
		//���Ų����޸�     
		
		JButton button1=new JButton("ȷ��");
		JButton button2=new JButton("ȡ��"); 
		button1.addActionListener(new ActionListener() { 
			public void actionPerformed (ActionEvent event) {     
				if(event.getActionCommand()=="ȷ��"&&!(name.getText().equals(""))&&!(sex.getText().equals(""))&&!(phone.getText().equals(""))) 
				{      
					int x=Shujuk.chagai(name.getText(),sex.getText(),phone.getText());      
					System.out.println(x);         
					if(x==1){ 
						JOptionPane.showMessageDialog(Zhuye.z,"�޸ĳɹ���");
						dispose();
						}         
					else if(x==0){ 
						JOptionPane.showMessageDialog(Zhuye.z,"�޸ĳ���");
						dispose();
						}  
					else if(x==-1){ 
						JOptionPane.showMessageDialog(Zhuye.z,"ϵͳ����");
						dispose();
						} 
					}    
				else if(event.getActionCommand()=="ȷ��"&&((name.getText().equals(""))||(sex.getText().equals(""))||(phone.getText().equals(""))))
					{
						JOptionPane.showMessageDialog(Zhuye.z,"�벹ȫ��Ϣ��");
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
		//����ť͸��
		Shujuk.touming a = new Shujuk.touming();//���������Shujuk��
		a.touming(button1);
		a.touming(button2);
		//�޸������ɫ������
		Shujuk.touming px = new Shujuk.touming();//������Shujuk��
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
 		//1.ע������       
 		String driverClassName = "com.mysql.jdbc.Driver";         
 		Class.forName("com.mysql.jdbc.Driver");       //2.�������ݿ�        
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
 		JOptionPane.showMessageDialog(Zhuye.z,"ϵͳ���ϣ����Ժ����ԣ�");       
 		}            
 	setVisible(true);            
 	}
}
