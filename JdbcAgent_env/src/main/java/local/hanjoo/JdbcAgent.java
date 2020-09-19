package local.hanjoo;

import java.sql.*;
import java.util.Scanner;
import java.io.Console;

public class JdbcAgent {

    // Connection info -------------------------------------------------------------------------------------------------
    final String ip = "192.1.5.108";
    final int port = 8629;
    final String db = "tibero";

    final String url = "jdbc:tibero:thin:@" + ip + ":" + port + ":" + db;
    final String driver = "com.tmax.tibero.jdbc.TbDriver";

    // Get ID & PW -----------------------------------------------------------------------------------------------------
    public String[] userInfo(String[] args) {

        String id;
        String pw;

        if (args.length == 2) {
            id = args[0];
            pw = args[1];
        } else {
            if (args.length != 0) {
                System.out.println("Enter the ID and Password correctly!\n");
            }
            Scanner scan = new Scanner(System.in);
            Console cons = System.console();

            char[] pw_char;

            System.out.println("Enter the ID: ");
            id = scan.nextLine();

            pw_char = cons.readPassword("Enter the password: ");
            pw = new String(pw_char);
        }

        return new String[] {id, pw};
    }

    // Connect to DBMS by JDBC -----------------------------------------------------------------------------------------
    public Connection connect(String id, String pw) {

        Connection con = null;

        try {
            Class.forName(driver);
            try {
                con = DriverManager.getConnection(url, id, pw);

                System.out.println("\nLog-in!\n");
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

        String[] loginInfo = tbAgent.userInfo(args);

        Connection con = tbAgent.connect(loginInfo[0], loginInfo[1]);

        Dbms tibero = new Dbms(con);

        tibero.select("AB1_2");
        tibero.showTable();

        con.close();
    }
}