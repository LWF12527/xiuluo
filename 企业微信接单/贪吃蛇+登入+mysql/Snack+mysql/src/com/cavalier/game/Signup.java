package com.cavalier.game;

/*Shepherd*/

public class Signup {
	public String Signup(String newUser,String newKey){
		MySql data = new MySql();
		data.setDatasourceName("signups");
		String sql = "INSERT INTO information(username,password) VALUES ('"+newUser+"', '"+newKey+"')";
		data.setSQL(sql);
		return data.record();
	}
}
