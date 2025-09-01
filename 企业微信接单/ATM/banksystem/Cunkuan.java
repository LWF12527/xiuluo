package banksystem;

import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class Cunkuan extends JDialog {
	private TextField jine = new TextField(10);

	public Cunkuan(JFrame m, String s) {
		super(m, s);
		setDefaultCloseOperation(WindowConstants.HIDE_ON_CLOSE);
		setBounds(400, 250, 400, 200);
		setVisible(true);
		setResizable(false);
		setLayout(null);

		// 修改图标
		Toolkit tk = Toolkit.getDefaultToolkit();
		Image img = tk.getImage("bank/tb.jpg"); // 登入成功关闭登录窗口，找图标和背景图片
		setIconImage(img);

		Container con = getContentPane();
		con.setBackground(Color.pink);

		JLabel label1 = new JLabel("请输入存款的金额");
		label1.setFont(new Font("宋体", Font.BOLD, 20));
		JLabel label2 = new JLabel("金额：");
		label2.setFont(new Font("宋体", Font.BOLD, 13));
		JButton button1 = new JButton("确认");

		// 将按钮透明
		Shujuk.touming a = new Shujuk.touming(); // 将类放在了Shujuk里
		a.touming(button1);

		// 修改面板颜色及字体
		Shujuk.touming px = new Shujuk.touming(); // 类在了Shujuk里
		JPanel p1 = new JPanel();
		JPanel p2 = new JPanel();
		px.touming(p1);
		px.touming(p2);

		p1.setBounds(0, 0, 400, 70);
		p1.add(label1);

		p2.setBounds(0, 70, 400, 50);
		p2.add(label2);
		p2.add(jine);
		p2.add(button1);

		add(p1);
		add(p2);

		// 添加确认按钮的事件监听器
		button1.addActionListener(new ActionListener() {
			@Override
			public void actionPerformed(ActionEvent event) {
				String input = jine.getText().trim();

				// 检查输入是否为空或非数字
				if (input.isEmpty()) {
					JOptionPane.showMessageDialog(Zhuye.z, "请输入存款金额！");
					return;
				}

				try {
					int amount = Integer.parseInt(input);
					if (amount <= 0) {
						JOptionPane.showMessageDialog(Zhuye.z, "存款金额应大于0！");
						return;
					}

					// 调用存款方法
					int result = Shujuk.cunkuan(Integer.parseInt(Denlu.Kahao.getText()), amount);
					if (result == 1) {
						JOptionPane.showMessageDialog(Zhuye.z, "成功存款 " + amount + " 元！");
						dispose();
					} else if (result == -1) {
						JOptionPane.showMessageDialog(Zhuye.z, "系统故障，请稍后重试！");
					}
				} catch (NumberFormatException e) {
					JOptionPane.showMessageDialog(Zhuye.z, "请输入有效的数字！");
				}
			}
		});

		// 确保对话框在创建时可见
		setVisible(true);
	}
}