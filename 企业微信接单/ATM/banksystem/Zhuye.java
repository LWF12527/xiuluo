package banksystem;

import javax.swing.*;
import javax.sound.sampled.*;//������Ƶ�İ�
import java.awt.*;
import java.awt.event.*;
import java.io.*;
public class Zhuye extends JFrame {
	static JFrame z=new JFrame();//ʵ��һ������
	@SuppressWarnings("removal")
	public Zhuye(){
		setTitle("ATM����ϵͳ");
		setBounds(370,190,800,500);
		setVisible(true);
		setResizable(false);
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);//��������
		setLayout(null);

		//�޸Ĵ���ͼ��
		Toolkit tk=Toolkit.getDefaultToolkit();
		Image img=tk.getImage("bank/tb.jpg");//����ɹ��رյ�¼���ڣ���ͼ��ͱ���ͼƬ
		setIconImage(img);
		//����ͼƬ
		ImageIcon t1=new ImageIcon("bank/zy.jpg");
		JLabel label0=new JLabel(t1);
		label0.setSize(t1.getIconWidth(),t1.getIconHeight());
		add(label0);
		JPanel pan=(JPanel) getContentPane();
		getLayeredPane().add(label0,new Integer(Integer.MIN_VALUE));//����ǩ�������Ϊ��ײ����
		pan.setOpaque(false);

		JLabel hy=new JLabel("��ӭʹ��ATM����ϵͳ");
		Font font=new Font("����",Font.BOLD,40);
		hy.setFont(font);
		JButton button1=new JButton("ȡ    ��");
		JButton button2=new JButton("�޸�����");
		JButton button3=new JButton("��    ��");
		JButton button4=new JButton("��ʾ���");
		JButton button5=new JButton("ת    ��");
		JButton button6=new JButton("��ѯ�޸�");
		JButton button7=new JButton("��  ��");
		JButton button8=new JButton("ע  ��");
		//����ť͸��
		Shujuk.touming a = new Shujuk.touming();//���������Shujuk��
		a.touming(button1);
		a.touming(button2);
		a.touming(button3);
		a.touming(button4);
		a.touming(button5);
		a.touming(button6);
		a.touming(button7);
		a.touming(button8);

		zy h=new zy();
		button1.addActionListener(h);
		button2.addActionListener(h);
		button3.addActionListener(h);
		button4.addActionListener(h);
		button5.addActionListener(h);
		button6.addActionListener(h);
		button7.addActionListener(h);
		button8.addActionListener(h);

		hy.setBounds(200,0,500,60);
		add(hy);
		button1.setBounds(150,70,150,40);
		add(button1);
		button2.setBounds(500,70,150,40);
		add(button2);
		button3.setBounds(150,170,150,40);
		add(button3);
		button4.setBounds(500,170,150,40);
		add(button4);
		button5.setBounds(150,270,150,40);
		add(button5);
		button6.setBounds(500,270,150,40);
		add(button6);
		button7.setBounds(220,370,130,40);
		add(button7);
		button8.setBounds(450,370,130,40);
		add(button8);
		setVisible(true);
	}

	public class zy implements ActionListener {
		public void actionPerformed (ActionEvent e) {
			if(e.getActionCommand()=="ȡ    ��")
				new Qukuan(z,"ȡ��ҵ��");
			else if(e.getActionCommand()=="�޸�����")
				new Gaimi(z,"�޸�����");
			else if(e.getActionCommand()=="��    ��")
				new Cunkuan(z,"���ҵ��");
			else if(e.getActionCommand()=="��ʾ���")
				new Xianshi(z,"��ʾ���");
			else if(e.getActionCommand()=="ת    ��")
				new Zhuanzhang(z,"ת��ҵ��");
			else if(e.getActionCommand()=="��ѯ�޸�")
				new Chagai(z,"��ѯ�޸�");
			else if(e.getActionCommand()=="��  ��") {
				dispose();//�����z������ҳ����
			}
			else if(e.getActionCommand()=="ע  ��") {

				String  str = JOptionPane.showInputDialog(null,"��������ȷ�����룺","@��������",0);
				Icon tb = new ImageIcon("bank/tb.jpg");//�滻�Ի���ͼ��
				int n = JOptionPane.showConfirmDialog(null,"�Ƿ�ȷ��ע��","ע��������",JOptionPane.YES_NO_OPTION,0,tb);
				if(n==JOptionPane.YES_OPTION){
					double a=(Shujuk.xianshi());
					if(a<0) {
						int b=(Shujuk.shanchu(str,Denlu.Kahao.getText()));
						if(b==1){
							JOptionPane.showMessageDialog(Zhuye.this,"ע���ɹ���");
							dispose();
							new Denlu();
						}
						else if(b==0)
							JOptionPane.showMessageDialog(Zhuye.this,"�������");
						else if(b==-1)
							JOptionPane.showMessageDialog(Zhuye.this,"ϵͳ����");
					}
					else
						JOptionPane.showMessageDialog(Zhuye.this,"�������˻���������ȡ��ʣ���Ǯ��ע��");
				}
				else if(n==JOptionPane.NO_OPTION) {}
			}

		}
	}
}
