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

		// �޸�ͼ��
		Toolkit tk = Toolkit.getDefaultToolkit();
		Image img = tk.getImage("bank/tb.jpg"); // ����ɹ��رյ�¼���ڣ���ͼ��ͱ���ͼƬ
		setIconImage(img);

		Container con = getContentPane();
		con.setBackground(Color.pink);

		JLabel label1 = new JLabel("��������Ľ��");
		label1.setFont(new Font("����", Font.BOLD, 20));
		JLabel label2 = new JLabel("��");
		label2.setFont(new Font("����", Font.BOLD, 13));
		JButton button1 = new JButton("ȷ��");

		// ����ť͸��
		Shujuk.touming a = new Shujuk.touming(); // ���������Shujuk��
		a.touming(button1);

		// �޸������ɫ������
		Shujuk.touming px = new Shujuk.touming(); // ������Shujuk��
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

		// ���ȷ�ϰ�ť���¼�������
		button1.addActionListener(new ActionListener() {
			@Override
			public void actionPerformed(ActionEvent event) {
				String input = jine.getText().trim();

				// ��������Ƿ�Ϊ�ջ������
				if (input.isEmpty()) {
					JOptionPane.showMessageDialog(Zhuye.z, "���������");
					return;
				}

				try {
					int amount = Integer.parseInt(input);
					if (amount <= 0) {
						JOptionPane.showMessageDialog(Zhuye.z, "�����Ӧ����0��");
						return;
					}

					// ���ô���
					int result = Shujuk.cunkuan(Integer.parseInt(Denlu.Kahao.getText()), amount);
					if (result == 1) {
						JOptionPane.showMessageDialog(Zhuye.z, "�ɹ���� " + amount + " Ԫ��");
						dispose();
					} else if (result == -1) {
						JOptionPane.showMessageDialog(Zhuye.z, "ϵͳ���ϣ����Ժ����ԣ�");
					}
				} catch (NumberFormatException e) {
					JOptionPane.showMessageDialog(Zhuye.z, "��������Ч�����֣�");
				}
			}
		});

		// ȷ���Ի����ڴ���ʱ�ɼ�
		setVisible(true);
	}
}