package banksystem;

import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
public class Xianshi extends JDialog{
	TextField yue=new TextField(10);
	double i=0;
	public Xianshi(JFrame m,String s){
		super(m,s);
		setBounds(400,250,400,180);
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
        
		JLabel label1=new JLabel("�������Ϊ��");
		label1.setFont(new Font("����",Font.BOLD,13));
		JLabel label2=new JLabel("Ԫ");
		label2.setFont(new Font("����",Font.BOLD,13));
		yue.setEditable(false);
		JButton button1=new JButton("ȷ��");
		button1.addActionListener(new ActionListener (){
			public void actionPerformed (ActionEvent event) {
				dispose();  
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
		p1.setBounds(0,30,400,50);
		p1.add(label1);
	    p1.add(yue);
	    p1.add(label2);
	    p2.setBounds(0,80,400,50);
	    p2.add(button1);
	    add(p1);
	    add(p2);
	    i=Shujuk.xianshi();
	    if(i>=0){
	    	yue.setText(String.valueOf(i));
       	}
        else if(i==-1){ 
       		JOptionPane.showMessageDialog(Zhuye.z,"ϵͳ���ϣ����Ժ�����");
       		
       	}
	    	setVisible(true);   
       }
}





