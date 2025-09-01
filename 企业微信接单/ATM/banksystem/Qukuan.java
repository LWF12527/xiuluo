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
		
		//修改图标
        Toolkit tk=Toolkit.getDefaultToolkit();
    	Image img=tk.getImage("bank/tb.jpg");//登入成功关闭登录窗口，找图标和背景图片
    	setIconImage(img);
        
    	Container con = getContentPane();
        con.setBackground(Color.pink);
    	
		JLabel label1=new JLabel("请输入取款的金额");
		label1.setFont(new Font("宋体",Font.BOLD,20));
		label1.setForeground(Color.red);
		JLabel label2=new JLabel("金额：");
		label2.setFont(new Font("Serif",Font.BOLD,13));
		JButton button1=new JButton("确认");
		button1.setForeground(Color.black);
		
		//使按钮背景透明
		button1.setBackground(Color.white);
		button1.setOpaque(false);
		
		button1.addActionListener(new ActionListener() {
			public void actionPerformed (ActionEvent event) {
				int j = Integer.parseInt(jine.getText()); //j为取款金额
				if(!(jine.getText().equals(""))&&(j>0)){
					int i=0;
					i=Shujuk.qukuan(Integer.parseInt(Denlu.Kahao.getText()),Integer.parseInt(jine.getText()));
					if(i==1) {
						JOptionPane.showMessageDialog(Zhuye.z,"成功取款"+jine.getText()+"元！");
						dispose();
						}
					else if(i==0)
						JOptionPane.showMessageDialog(Zhuye.z,"您的余额不足！");
					else {
						JOptionPane.showMessageDialog(Zhuye.z,"系统故障，请稍后在试！");
						dispose();
						}
					}
				else
					JOptionPane.showMessageDialog(Zhuye.z,"取款金额应大于0!");
				}
			});
		JPanel p1=new JPanel();
		JPanel p2=new JPanel();
		//将按钮透明
		Shujuk.touming a = new Shujuk.touming();//将类放在了Shujuk里
		a.touming(button1);
		//修改面板颜色及字体
		Shujuk.touming px = new Shujuk.touming();//类在了Shujuk里
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