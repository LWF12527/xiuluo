package game;
import java.awt.Graphics;

import javax.swing.*;
public class snakeMain extends JFrame {
	public snakeMain() {
		snakeWin win = new snakeWin();
		add(win);
		setTitle("̰贪吃蛇小游戏");
		setSize(435,390);
		setLocation(200, 200);
		setVisible(true);
	}
	public static void main(String[] args) {
		new snakeMain();
	}
}
