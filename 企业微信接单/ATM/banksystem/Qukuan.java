package banksystem;

import javax.swing.*; 
import java.awt.*;
import java.awt.event.*;
public class Qukuan extends JDialog{
	TextField jine=new TextField(10);;
	public Qukuan(JFrame m,String s) {
		super(m,s);
		setDefaultCloseOperation(WindowConstants.HIDE_ON_CLOSE);
		setBounds(400,250,400,200);
		setVisible(true);
		setResizable(false);
		setLayout(null);
		
		//�޸�ͼ��
        Toolkit tk=Toolkit.getDefaultToolkit();
    	Image img=tk.getImage("bank/tb.jpg");//����ɹ��رյ�¼���ڣ���ͼ��ͱ���ͼƬ
    	setIconImage(img);
        
    	Container con = getContentPane();
        con.setBackground(Color.pink);
    	
		JLabel label1=new JLabel("������ȡ��Ľ��");
		label1.setFont(new Font("����",Font.BOLD,20));
		label1.setForeground(Color.red);
		JLabel label2=new JLabel("��");
		label2.setFont(new Font("Serif",Font.BOLD,13));
		JButton button1=new JButton("ȷ��");
		button1.setForeground(Color.black);
		
		//ʹ��ť����͸��
		button1.setBackground(Color.white);
		button1.setOpaque(false);
		
		button1.addActionListener(new ActionListener() {
			public void actionPerformed (ActionEvent event) {
				int j = Integer.parseInt(jine.getText()); //jΪȡ����
				if(!(jine.getText().equals(""))&&(j>0)){
					int i=0;
					i=Shujuk.qukuan(Integer.parseInt(Denlu.Kahao.getText()),Integer.parseInt(jine.getText()));
					if(i==1) {
						JOptionPane.showMessageDialog(Zhuye.z,"�ɹ�ȡ��"+jine.getText()+"Ԫ��");
						dispose();
						}
					else if(i==0)
						JOptionPane.showMessageDialog(Zhuye.z,"�������㣡");
					else {
						JOptionPane.showMessageDialog(Zhuye.z,"ϵͳ���ϣ����Ժ����ԣ�");
						dispose();
						}
					}
				else
					JOptionPane.showMessageDialog(Zhuye.z,"ȡ����Ӧ����0!");
				}
			});
		JPanel p1=new JPanel();
		JPanel p2=new JPanel();
		//����ť͸��
		Shujuk.touming a = new Shujuk.touming();//���������Shujuk��
		a.touming(button1);
		//�޸������ɫ������
		Shujuk.touming px = new Shujuk.touming();//������Shujuk��
		px.touming(p1);
		px.touming(p2);
		
		p1.setBounds(0,0,400,70);
		p1.add(label1);
		p2.setBounds(0,70,400,50);
		p2.add(label2);
		p2.add(jine);
		p2.add(button1);
		add(p1);
		add(p2);
		setVisible(true);
		}
	}