package com.cavalier.game;

/*shep
 * 链接数据库修改密码
 */
public class Change {
	public void Change(String user,String newkeys){
		MySql mySql = new MySql();
		mySql.setDatasourceName("signups");
		mySql.setSQL("UPDATE information SET password = '"+newkeys+"' WHERE username = '"+user+"'");
	}
}
