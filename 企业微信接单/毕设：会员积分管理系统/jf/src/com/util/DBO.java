package com.util;

import com.mysql.cj.jdbc.exceptions.SQLExceptionsMapping;
import org.apache.commons.lang.ObjectUtils;

import java.sql.*;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;

import java.sql.*;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import javax.naming.Context;
import javax.naming.InitialContext;

public class DBO {


	private Statement stmt;
	private Connection conn;
	public DBO()
	{
	}

	/**
		???????
	*/
	public void open() 
	{
		try 
		{	Class.forName("com.mysql.cj.jdbc.Driver");
			System.out.println("mysql数据库驱动加载成功！");
			conn=DriverManager.getConnection("jdbc:mysql://localhost:3306/jf","root","123456");
			System.out.println(conn==null);

			//Class.forName("com.microsoft.jdbc.sqlserver.SQLServerDriver");           
			//conn = DriverManager.getConnection("jdbc:microsoft:sqlserver://localhost:1433;databasename=xswz","sa","123");
			stmt=conn.createStatement();

			System.out.println("success");

		} 
		catch (Exception ex) 
		{
		System.err.println("????????????: " + ex.getMessage());
		}
	}

	/**
		????????????????????????
	*/
	public void close() 
	{
		try 
		{
		
				
		//	connMgr.freeConnection("java", conn);
			conn.close();
			System.out.println ("???????");
		} 
		catch (SQLException ex) 
		{
			System.err.println("????????????: " + ex.getMessage());
		}
	}

	/**
		??в??
	*/
	public ResultSet executeQuery(String sql) throws SQLException
	{
		ResultSet rs = null;
		rs = stmt.executeQuery(sql);
		System.out.println ("??в??");
		return rs;
	}

	/**
		????????
	*/
	public int executeUpdate(String sql) throws SQLException
	{
		int ret = 0;
		
		try {


			ret = stmt.executeUpdate(sql);
		}catch (SQLException throwables) {
			throwables.printStackTrace();
		}
		System.out.println ("????????");
		return ret;
	}

	/**
		??SQL????????????
	*/
	public void addBatch(String sql) throws SQLException 
	{
		stmt.addBatch(sql);
	}

	/**
		?????????
	*/
	public int [] executeBatch() throws SQLException 
	{
		boolean isAuto=conn.getAutoCommit();
		
		conn.setAutoCommit(false);
		int [] updateCounts = stmt.executeBatch();
		
//		conn.commit();
		
//		conn.setAutoCommit(isAuto);
		//conn.setAutoCommit(true);
		return updateCounts;
	}
	public boolean getAutoCommit() throws SQLException
	{
		return conn.getAutoCommit();
	}
	public void setAutoCommit(boolean auto)  throws SQLException 
	{
		conn.setAutoCommit(auto);
	}
	
	public void commit() throws SQLException 
	{
		conn.commit();
//		this.close();
	}
	public void rollBack() throws SQLException 
	{
		conn.rollback();
//		this.close();
	}
	
}
