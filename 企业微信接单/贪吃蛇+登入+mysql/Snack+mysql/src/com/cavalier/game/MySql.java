package com.cavalier.game;
import java.sql.*;
/*
 * ���ݿ����
 */
public class MySql {
	String datasourceName = "";
	String SQL="";
	String message = "";
	public MySql(){
		try {
			Class.forName("com.mysql.cj.jdbc.Driver");
		} catch (Exception e) {
			System.out.println("�������ݿ�ʧ��");
			e.printStackTrace();
		}
	}
	
	public void setSQL(String SQL){
		this.SQL = SQL;
	}
	
	public void setDatasourceName(String s){
		datasourceName = s.trim();
	}

	public String record() {
		try{
			Connection con;
			Statement state;
			String url ="jdbc:mysql://localhost:3306/"+datasourceName;
			con = DriverManager.getConnection(url,"root","123456");
			state = con.createStatement();
			state.execute(SQL);
			message = "sql�����ɹ�";
			con.close();
		}
		catch (SQLException e) {
			message = e.toString();
		}
		return message;
	}
}
