package banksystem;

import java.awt.*;
import javax.swing.*;
import java.awt.event.*;
public class Zhuce extends JFrame{
		JFrame x=new JFrame("���û�ע��");
		TextField name=new TextField(20);
		TextField sex=new TextField(20);
		TextField kahao=new TextField(20);
		TextField mima=new TextField(20);
		TextField phone=new TextField(20);
		public Zhuce(){
			x.setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE);
			x.setBounds(210,110,700,430);
			x.setVisible(true);
			x.setResizable(false);
			x.setLayout(null);
			x.setLocationRelativeTo(null);//���������
			
			//�޸�ͼ��
	        Toolkit tk=Toolkit.getDefaultToolkit();
	    	Image img=tk.getImage("bank/tb.jpg");//����ɹ��رյ�¼���ڣ���ͼ��ͱ���ͼƬ
	    	x.setIconImage(img);
	    	
	    	Container con = x.getContentPane();
	        con.setBackground(Color.pink);
	    	
			JLabel label1=new JLabel("�ͻ�ע��");
			JLabel label2=new JLabel("��    ����");
			JLabel label3=new JLabel("��    ��");
			JLabel label4=new JLabel("��    �ţ�");
			JLabel label5=new JLabel("��    �룺");
			JLabel label6=new JLabel("�ֻ���  ��");
			label1.setFont(new Font("����",Font.BOLD,40)); 
			label2.setFont(new Font("����",Font.BOLD,20));
			label3.setFont(new Font("����",Font.BOLD,20));
			label4.setFont(new Font("����",Font.BOLD,20));
			label5.setFont(new Font("����",Font.BOLD,20));
			label6.setFont(new Font("����",Font.BOLD,20));
			JButton button1=new JButton("ע��");
			JButton button2=new JButton("ȡ��");
			zc h=new zc();
			button1.addActionListener(h);
			button2.addActionListener(h);
			
			//����ť͸��
			Shujuk.touming a = new Shujuk.touming();//���������Shujuk��
			a.touming(button1);
			a.touming(button2);
			
			JPanel p1=new JPanel();
			JPanel p2=new JPanel();
			JPanel p3=new JPanel();
			JPanel p4=new JPanel();
			JPanel p5=new JPanel();
			JPanel p6=new JPanel();
			JPanel p7=new JPanel();
			//�޸������ɫ������
			Shujuk.touming px = new Shujuk.touming();//������Shujuk��
			px.touming(p1);
			px.touming(p2);
			px.touming(p3);
			px.touming(p4);
			px.touming(p5);
			px.touming(p6);
			px.touming(p7);
			
			p1.setBounds(0,0,700,70);
			p1.add(label1);
			p2.setBounds(0,70,700,50);
			p2.add(label2);
			p2.add(name);
			p3.setBounds(0,120,700,50);
			p3.add(label3);
			p3.add(sex);
			p4.setBounds(0,170,700,50);
			p4.add(label4);
			p4.add(kahao); 
			p5.setBounds(0,220,700,50);
			p5.add(label5);
			p5.add(mima);
			p6.setBounds(0,270,700,70);
			p6.add(label6);
			p6.add(phone);
			p7.setBounds(0,340,700,100);
			p7.add(button1);
			p7.add(button2);
			x.add(p1);
			x.add(p2);
			x.add(p3);
			x.add(p4);
			x.add(p5);
			x.add(p6);
			x.add(p7);
			}
	class zc implements ActionListener{
			public void actionPerformed (ActionEvent e) {
				String s1=name.getText();
				String s2=sex.getText();
				String s3=kahao.getText();
				String s4=mima.getText();
				String s5=phone.getText();
				System.out.println(s1);
				if(e.getActionCommand()=="ע��") 
					{
						if((s1.equals("") || s2.equals("") || s3.equals("") || s4.equals("") || s5.equals("")))
						{
							JOptionPane.showMessageDialog(Zhuce.this,"�벹ȫ��Ϣ��");
						}
						else{
							Shujuk.zhucezh(s1,s2,s3,s4,s5);
							if(banksystem.Shujuk.ok!=0){
								JOptionPane.showMessageDialog(Zhuce.this,"ע��ɹ���");
								x.dispose();
							}
							else
								JOptionPane.showMessageDialog(Zhuce.this,"�����Ѵ���");
								x.dispose();
						}
					}
				else
					x.dispose();
				}    
			}
		}
