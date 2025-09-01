package banksystem;

import javax.swing.*; 
import java.sql.*;  
import java.awt.*; 
import java.awt.event.*;

public class Denlu extends JFrame {  
	static TextField Kahao=new TextField(20);
    static JPasswordField Mima=new JPasswordField(18);

public Denlu(){     
        setSize(800,430); 
        setLocationRelativeTo(null);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE); //不可退出
        setResizable(false);    //不可改大小 
        setTitle("欢迎使用ATM管理系统");
        //修改图标
        Toolkit tk=Toolkit.getDefaultToolkit();
    	Image img=tk.getImage("bank/tb.jpg");//登入成功关闭登录窗口，找图标和背景图片
    	setIconImage(img);
    	
    	//替换背景
        ImageIcon t1=new ImageIcon("bank/dl.jpg");
        JLabel label0=new JLabel(t1);
        label0.setSize(t1.getIconWidth(),t1.getIconHeight());
        add(label0);
        JPanel pan=(JPanel) getContentPane();
        getLayeredPane().add(label0,new Integer(Integer.MIN_VALUE));//见标签面板设置为最底层面板
        pan.setOpaque(false);
        
        JLabel label1=new JLabel("银行卡号  ：");     
        JLabel label2=new JLabel("银行卡密码："); 
        Font font = new Font("楷体",Font.BOLD,20);
        label1.setFont(font);     
        label2.setFont(font);        
        JButton button1=new JButton("登录");  
        JButton button2=new JButton("注册"); 
      //将按钮透明
      	Shujuk.touming a = new Shujuk.touming();//将类放在了Shujuk里
      	a.touming(button1);
      	a.touming(button2);
    
        dr h=new dr();   
        button1.addActionListener(h);  
        button2.addActionListener(h);     
        JPanel p1=new JPanel(); 
        p1.setOpaque(false);//将面板透明化
        JPanel p2=new JPanel();
        p2.setOpaque(false);
        JPanel p3=new JPanel();
        p3.setOpaque(false); 
        p1.setBounds(0,150,800,50);    //使用面板不需要调整宽度，会自动居中
        p1.add(label1);   
        p1.add(Kahao);  
        p2.setBounds(0,200,800,50);    
        p2.add(label2);   
        p2.add(Mima);  
        p3.setBounds(0,300,800,70);       
        p3.add(button1);   
        p3.add(button2);
        add(p1);   
        add(p2);  
        add(p3);  
        add(new JLabel());//最后加空标签，防止面板错位;
        setVisible(true);         
 }   

public class dr implements ActionListener {  
           public void actionPerformed (ActionEvent event) {
        	   if(event.getActionCommand()=="注册")  {   
        		   new Zhuce();  
               	}  
        	   	else if(event.getActionCommand()=="登录") {
        	   		if(Shujuk.checkUser(Kahao.getText(),Mima.getText())==1) { 
            		   Icon tb = new ImageIcon("bank/tb.jpg");
            		   JOptionPane.showMessageDialog(Denlu.this,"登录成功","欢迎！！！",0,tb);   
	                   new Zhuye();  
	                   dispose();
        	   		}
	                else            
	                	JOptionPane.showMessageDialog(Denlu.this,"卡号或密码不正确！");
        	   	}
             }          
           }
 
public static void main(String args[]){   
    Denlu a=new Denlu(); 
} 
}
