import com.util.DBO;

import java.sql.ResultSet;
import java.sql.ResultSetMetaData;
import java.sql.SQLException;

public class SQLTest {
    public static void main(String[] args) throws Exception{
        DBO dbo=new DBO();
        ResultSet resultSet = null;
        dbo.open();
        try {
            resultSet = dbo.executeQuery("select * from admin");
        } catch (SQLException throwables) {
            throwables.printStackTrace();
        }
        //ResultSet resultSet = statement.executeQuery("SELECT * from foo");
        ResultSetMetaData rsmd = resultSet.getMetaData();
        int columnsNumber = rsmd.getColumnCount();
        while (resultSet.next()) {
            for (int i = 1; i <= columnsNumber; i++) {
                if (i > 1) System.out.print(",  ");
                String columnValue = resultSet.getString(i);
                System.out.print(columnValue + " " + rsmd.getColumnName(i));
            }
            System.out.println("");
        }
        System.out.println(resultSet.toString());
    }
}
