package com.cavalier.game;


import java.sql.*;

public class Search {
	String datasourceName = "signups";
	String []name = new String[10];
	int []scores = new int[10];
	public Search(){
		try {
			Class.forName("com.mysql.cj.jdbc.Driver");
		} catch (Exception e) {
			System.out.println("加载数据库失败");
			e.printStackTrace();
		}
	}
	
	public boolean searchName(String user) {
		boolean flag = false;
		Connection con;
		Statement sql;
		String username;
		ResultSet rs1;
		try{
			String url ="jdbc:mysql://localhost:3306/"+datasourceName;
			con = DriverManager.getConnection(url,"root","123456");
			sql = con.createStatement();
			rs1 = sql.executeQuery("SELECT username FROM information");
			while(rs1.next()){
				username = rs1.getString("username");
				if(username.equals(user)){
					flag = true;
					break;
				}
			}
			con.close();
			sql.close();
		}
		catch (SQLException e) {
			System.out.println("请输入正确的表名"+e);
			}
		return flag;
		}
	
	
	
	public boolean searchKey(String user,String key){
		boolean flag2 = false;
		try{	 
			Connection con;
			Statement sql;
			ResultSet rs2;
			String passwords;
			String url ="jdbc:mysql://localhost:3306/"+datasourceName;
			con = DriverManager.getConnection(url,"root","123456");
			sql = con.createStatement();
			rs2 = sql.executeQuery("SELECT password FROM information WHERE username='"+user+"'");
			while(rs2.next()){
				passwords = rs2.getString("password");
				if(key.equals(passwords)){
					flag2 = true;
				}
			}
			con.close();
			sql.close();
		}
		catch (SQLException e) {
			System.out.println("请输入正确的表名"+e);
			}
		return flag2;
		}
	
	public boolean searchScore(String user,int score){
		boolean flag3 = false;
		try{	 
			Connection con;
			Statement sql;
			ResultSet rs3;
			int scores;
			String url ="jdbc:mysql://localhost:3306/"+datasourceName;
			con = DriverManager.getConnection(url,"root","123456");
			sql = con.createStatement();
			rs3 = sql.executeQuery("SELECT modescore FROM information WHERE username='"+user+"'");
			while(rs3.next()){
				scores = rs3.getInt("modescore");
				if(score > scores){
					flag3 = true;
					break;
				}
			}
			con.close();
			sql.close();
		}
		catch (SQLException e) { System.out.println("查询modescore成绩出错"); }
		return flag3;
		}


	public void readScore(){
		try{	 
			Connection con;
			Statement sql;
			ResultSet rs4;
			int i = 0;
			String url ="jdbc:mysql://localhost:3306/"+datasourceName;
			con = DriverManager.getConnection(url,"root","123456");
			sql = con.createStatement();
			rs4 = sql.executeQuery("SELECT username,modescore FROM information order by modescore desc");
			while(rs4.next()&&i<=4){
				name[i] = rs4.getString("username");
				scores[i] = rs4.getInt("modescore");
				i++;
			}
			con.close();
			sql.close();
		}
		catch (SQLException e) {
			System.out.println("请输入正确的表名"+e);
			}
		}
	}