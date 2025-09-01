package banksystem;

import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
public class Zhuanzhang extends JDialog {
	TextField kahao = new TextField(15);
	TextField jine = new TextField(15);

	public Zhuanzhang(JFrame m, String s) {
		super(m, s);
		setDefaultCloseOperation(WindowConstants.HIDE_ON_CLOSE);
		setBounds(400, 250, 400, 300);
		setResizable(false);
		setLayout(null);

		// Set the window icon
		Toolkit tk = Toolkit.getDefaultToolkit();
		Image img = tk.getImage("bank/tb.jpg");
		setIconImage(img);

		Container con = getContentPane();
		con.setBackground(Color.pink);

		// Initialize the labels and button
		JLabel label1 = new JLabel("请输入转账信息");
		label1.setFont(new Font("宋体", Font.BOLD, 20));
		JLabel label2 = new JLabel("收款人卡号：");
		label2.setFont(new Font("宋体", Font.BOLD, 13));
		JLabel label3 = new JLabel("转账金额  ：");
		label3.setFont(new Font("宋体", Font.BOLD, 13));
		JButton button1 = new JButton("确认");

		// Action listener for the button
		button1.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent event) {
				if (!(jine.getText().equals("")) && !(kahao.getText().equals(""))) {
					int i = Shujuk.zhuanzhang(Integer.parseInt(kahao.getText()), Integer.parseInt(jine.getText()));
					if (i == 1) {
						JOptionPane.showMessageDialog(Zhuye.z, "成功转账" + jine.getText() + "元！");
						dispose();
					} else if (i == 2) {
						JOptionPane.showMessageDialog(Zhuye.z, "余额不足！");
					} else if (i == 0) {
						JOptionPane.showMessageDialog(Zhuye.z, "您输入的银行卡号不存在！");
					} else {
						JOptionPane.showMessageDialog(Zhuye.z, "系统故障！");
						dispose();
					}
				} else if ((jine.getText().equals("")) || (kahao.getText().equals(""))) {
					JOptionPane.showMessageDialog(Zhuye.z, "请补全信息！");
				}
			}
		});

		// Initialize panels for better organization
		JPanel p1 = new JPanel();
		JPanel p2 = new JPanel();
		JPanel p3 = new JPanel();
		JPanel p4 = new JPanel();

		// Making button transparent
		Shujuk.touming a = new Shujuk.touming();
		a.touming(button1);

		// Modify panel and font style
		Shujuk.touming px = new Shujuk.touming();
		px.touming(p1);
		px.touming(p2);
		px.touming(p3);
		px.touming(p4);

		// Setting bounds for each panel and adding components
		p1.setBounds(0, 0, 400, 50);
		p1.add(label1);
		p2.setBounds(0, 60, 400, 50);
		p2.add(label2);
		p2.add(kahao);
		p3.setBounds(0, 110, 400, 50);
		p3.add(label3);
		p3.add(jine);
		p4.setBounds(0, 170, 400, 50);
		p4.add(button1);

		// Add panels to the content pane
		add(p1);
		add(p2);
		add(p3);
		add(p4);

		// Finally set visibility of the dialog
		setVisible(true);
	}
}
