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
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE); //�����˳�
        setResizable(false);    //���ɸĴ�С 
        setTitle("��ӭʹ��ATM����ϵͳ");
        //�޸�ͼ��
        Toolkit tk=Toolkit.getDefaultToolkit();
    	Image img=tk.getImage("bank/tb.jpg");//����ɹ��رյ�¼���ڣ���ͼ��ͱ���ͼƬ
    	setIconImage(img);
    	
    	//�滻����
        ImageIcon t1=new ImageIcon("bank/dl.jpg");
        JLabel label0=new JLabel(t1);
        label0.setSize(t1.getIconWidth(),t1.getIconHeight());
        add(label0);
        JPanel pan=(JPanel) getContentPane();
        getLayeredPane().add(label0,new Integer(Integer.MIN_VALUE));//����ǩ�������Ϊ��ײ����
        pan.setOpaque(false);
        
        JLabel label1=new JLabel("���п���  ��");     
        JLabel label2=new JLabel("���п����룺"); 
        Font font = new Font("����",Font.BOLD,20);
        label1.setFont(font);     
        label2.setFont(font);        
        JButton button1=new JButton("��¼");  
        JButton button2=new JButton("ע��"); 
      //����ť͸��
      	Shujuk.touming a = new Shujuk.touming();//���������Shujuk��
      	a.touming(button1);
      	a.touming(button2);
    
        dr h=new dr();   
        button1.addActionListener(h);  
        button2.addActionListener(h);     
        JPanel p1=new JPanel(); 
        p1.setOpaque(false);//�����͸����
        JPanel p2=new JPanel();
        p2.setOpaque(false);
        JPanel p3=new JPanel();
        p3.setOpaque(false); 
        p1.setBounds(0,150,800,50);    //ʹ����岻��Ҫ������ȣ����Զ�����
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
        add(new JLabel());//���ӿձ�ǩ����ֹ����λ;
        setVisible(true);         
 }   

public class dr implements ActionListener {  
           public void actionPerformed (ActionEvent event) {
        	   if(event.getActionCommand()=="ע��")  {   
        		   new Zhuce();  
               	}  
        	   	else if(event.getActionCommand()=="��¼") {
        	   		if(Shujuk.checkUser(Kahao.getText(),Mima.getText())==1) { 
            		   Icon tb = new ImageIcon("bank/tb.jpg");
            		   JOptionPane.showMessageDialog(Denlu.this,"��¼�ɹ�","��ӭ������",0,tb);   
	                   new Zhuye();  
	                   dispose();
        	   		}
	                else            
	                	JOptionPane.showMessageDialog(Denlu.this,"���Ż����벻��ȷ��");
        	   	}
             }          
           }
 
public static void main(String args[]){   
    Denlu a=new Denlu(); 
} 
}
