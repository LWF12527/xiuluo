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
        setLayout(null);//不用任何布局?
        Container con = getContentPane();
        con.setBackground(Color.pink);
        
        //修改图标
        Toolkit tk=Toolkit.getDefaultToolkit();
    	Image img=tk.getImage("bank/tb.jpg");//登入成功关闭登录窗口，找图标和背景图片
    	setIconImage(img);

        JLabel label1=new JLabel("修改密码");
        label1.setFont(new Font("宋体",Font.BOLD,20));
        JLabel label2=new JLabel("原密码：");
        label2.setFont(new Font("宋体",Font.BOLD,13));
        JLabel label3=new JLabel("新密码：");
        label3.setFont(new Font("宋体",Font.BOLD,13));
        JButton button1=new JButton("确认");
        JButton button2=new JButton("取消");
  
        button1.addActionListener(new ActionListener() {
    		public void actionPerformed (ActionEvent event){
    			if(event.getActionCommand()=="确认"&&!(ymima.getText().equals(""))&&!(xmima.getText().equals("")))
                 {//密码不能为空
    				int i=Shujuk.gaimi(ymima.getText(),xmima.getText());
    				if(i==1)
    				{
    					JOptionPane.showMessageDialog(Zhuye.z,"修改密码成功，请重新登录！");
    				    Zhuye.z.dispose();
    				    new Denlu();
    				}
    				else if(i==0)
    					JOptionPane.showMessageDialog(Zhuye.z,"原密码错误！");
    				else
    				{
    					JOptionPane.showMessageDialog(Zhuye.z,"系统故障！");
    					dispose();
    			    }
    			}
    			else {
    				if(event.getActionCommand()=="确认"&&((ymima.getText().equals(""))||(xmima.getText().equals(""))))
    					JOptionPane.showMessageDialog(Zhuye.z,"请补全信息！");
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
