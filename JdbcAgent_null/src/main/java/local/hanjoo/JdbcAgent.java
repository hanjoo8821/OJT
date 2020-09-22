package local.hanjoo;

import java.sql.*;

public class JdbcAgent {

    // Connection info -------------------------------------------------------------------------------------------------
    final String ip = "192.1.5.108";
    final int port = 8629;
    final String db = "tibero";

    final String url = "jdbc:tibero:thin:@" + ip + ":" + port + ":" + db;
    final String driver = "com.tmax.tibero.jdbc.TbDriver";

    // Connect to DBMS by JDBC -----------------------------------------------------------------------------------------
    public Connection connect(String id, String pw) {

        Connection con = null;

        try {
            Class.forName(driver);
            try {
                con = DriverManager.getConnection(url, id, pw);
            } catch (SQLException e) {
                e.printStackTrace();
                System.exit(0);
            }
        } catch (ClassNotFoundException e) {
            e.printStackTrace();
            System.exit(0);
        }

        return con;
    }

    // ================================================== MAIN =========================================================
    public static void main(String[] args) throws SQLException {

        JdbcAgent tbAgent = new JdbcAgent();

        Connection con = tbAgent.connect(args[0], args[1]);

        Dbms tibero = new Dbms(con);

        tibero.select("AB1_2");
        tibero.showTable();

        con.close();
    }
}