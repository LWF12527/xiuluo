package com.cavalier.view;

import java.awt.Color;
import java.awt.Font;
import java.awt.Graphics;

import javax.swing.JPanel;
import javax.swing.border.EtchedBorder;
import com.cavalier.entities.Food;
import com.cavalier.entities.Ground;
import com.cavalier.entities.Snake;
import com.cavalier.game.MySql;
import com.cavalier.game.Login;
import com.cavalier.game.Search;
import com.cavalier.util.Global;

public class GamePanel extends JPanel{

	private static final long serialVersionUID = 1L;

	private Snake snake;
	private Food food;
	private Ground ground;
	public Color backgroundColor;

	public GamePanel() {
		setLocation(200,60);
		/* ���ô�С�Ͳ��� */
		this.setSize(Global.WIDTH * Global.CELL_SIZE, Global.HEIGHT* Global.CELL_SIZE);
		this.setBorder(new EtchedBorder(EtchedBorder.LOWERED));
		this.setFocusable(true);

	}


	public void display(Snake snake,Food food,Ground ground) {
		this.snake = snake;
		this.food = food;
		this.ground = ground;

		repaint();
	}


	//�����Ϸ��壨����Ч����
	public void clearDraw(Graphics g) {
		if(backgroundColor==null) {
			g.setColor(new Color(0x4169E1));
		}
		else {
			g.setColor(backgroundColor);

		}
		g.fillRect(0, 0, Global.WIDTH*Global.CELL_SIZE, Global.HEIGHT*Global.CELL_SIZE);
	}


	@Override
	public void paint(Graphics g) {
		clearDraw(g);
		//������ʾ
		if(ground != null && snake != null && food != null) {
			ground.drawMe(g);
			food.drawMe(g);
			snake.drawMe(g);
		}
		if(snake!=null && !snake.isLife())  {
			recover(g);
		}

	}


	//�ָ�����
	public void recover(Graphics g) {
		clearDraw(g);

		//����Ϸ����������ơ�game over��
		g.setColor(Color.white);
		g.setFont(new Font("Serif",Font.BOLD,50));
		g.drawString("Game Over", 130, 210);
		int score = BottonPanel.score;
		MySql mySql = new MySql();
		Search se = new Search();
		boolean updateflag = se.searchScore(Login.user, score);
		if(updateflag) {
			mySql.setDatasourceName("signups");//�������ݿ�
			mySql.setSQL("UPDATE information SET modescore = "+score+" WHERE username = '"+Login.user+"'");
			mySql.record();
			System.out.println("�ɼ�д��ɹ���" + score);
		}
	}
}
