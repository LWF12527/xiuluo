package banksystem;

import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
public class Gaimi extends JDialog{
	TextField ymima=new TextField(15);
	TextField xmima=new TextField(15);
	public Gaimi(JFrame m,String s) {
		super(m,s);
		setBounds(400,250,400,300);
		setVisible(true);
        setDefaultCloseOperation(JDialog.DISPOSE_ON_CLOSE);
        setResizable(false);
        setLayout(null);//�����κβ���?
        Container con = getContentPane();
        con.setBackground(Color.pink);
        
        //�޸�ͼ��
        Toolkit tk=Toolkit.getDefaultToolkit();
    	Image img=tk.getImage("bank/tb.jpg");//����ɹ��رյ�¼���ڣ���ͼ��ͱ���ͼƬ
    	setIconImage(img);

        JLabel label1=new JLabel("�޸�����");
        label1.setFont(new Font("����",Font.BOLD,20));
        JLabel label2=new JLabel("ԭ���룺");
        label2.setFont(new Font("����",Font.BOLD,13));
        JLabel label3=new JLabel("�����룺");
        label3.setFont(new Font("����",Font.BOLD,13));
        JButton button1=new JButton("ȷ��");
        JButton button2=new JButton("ȡ��");
  
        button1.addActionListener(new ActionListener() {
    		public void actionPerformed (ActionEvent event){
    			if(event.getActionCommand()=="ȷ��"&&!(ymima.getText().equals(""))&&!(xmima.getText().equals("")))
                 {//���벻��Ϊ��
    				int i=Shujuk.gaimi(ymima.getText(),xmima.getText());
    				if(i==1)
    				{
    					JOptionPane.showMessageDialog(Zhuye.z,"�޸�����ɹ��������µ�¼��");
    				    Zhuye.z.dispose();
    				    new Denlu();
    				}
    				else if(i==0)
    					JOptionPane.showMessageDialog(Zhuye.z,"ԭ�������");
    				else
    				{
    					JOptionPane.showMessageDialog(Zhuye.z,"ϵͳ���ϣ�");
    					dispose();
    			    }
    			}
    			else {
    				if(event.getActionCommand()=="ȷ��"&&((ymima.getText().equals(""))||(xmima.getText().equals(""))))
    					JOptionPane.showMessageDialog(Zhuye.z,"�벹ȫ��Ϣ��");
    			}
     			}
    		});
        button2.addActionListener(new ActionListener() {
        	public void actionPerformed (ActionEvent event){
        		dispose();
        	}
        });
        JPanel p1=new JPanel();
        JPanel p2=new JPanel();
        JPanel p3=new JPanel();
        JPanel p4=new JPanel();
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
        p1.setBounds(0,0,400,40);
        p1.add(label1);
        p2.setBounds(0,60,400,40);
        p2.add(label2);
        p2.add(ymima);
        p3.setBounds(0,100,400,40);
        p3.add(label3);
        p3.add(xmima);
        p4.setBounds(0,160,400,40);
        p4.add(button1);
        p4.add(button2);
        add(p1);
        add(p2);
        add(p3);
        add(p4);
        setVisible(true);
        }
	}
