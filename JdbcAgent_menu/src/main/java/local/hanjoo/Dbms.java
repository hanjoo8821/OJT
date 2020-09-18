package local.hanjoo;

import java.sql.*;
import java.util.Scanner;

public class Dbms {

    private final Connection con;
    private String sql;

    public Dbms(Connection con) {
        this.con = con;
    }

    // SELECT ----------------------------------------------------------------------------------------------------------
    public void tableList() {
        try {
            Statement st = con.createStatement();
            ResultSet rs = st.executeQuery("SELECT * FROM TAB");

            try {
                while (rs.next()) {
                    System.out.println(rs.getString(1));
                }
            } catch (Exception e) {
                e.printStackTrace();
            } finally {
                rs.close();
                st.close();
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    // SELECT ----------------------------------------------------------------------------------------------------------
    public String select() {
        Scanner scan = new Scanner(System.in);

        String table;
        System.out.print("Select a TABLE: ");
        table = scan.nextLine();

        return select(table);
    }

    public String select(String table) {
        sql = "SELECT * FROM " + table;

        System.out.printf("[ %s ] is selected!\n", table);

        return table;
    }

    // Query  ----------------------------------------------------------------------------------------------------------
    public void showTable() {
        try {
            Statement st = con.createStatement();
            ResultSet rs = st.executeQuery(sql);

            try {
                ResultSetMetaData rsMd = rs.getMetaData();
                int numCols = rsMd.getColumnCount();

                while (rs.next()) {
                    for (int i = 1; i <= numCols; i++) {
                        if (rs.getString(i) == null) {
                            System.out.print(" ");
                        } else {
                            System.out.print(rs.getString(i) + " ");
                        }
                    }
                    System.out.println();
                }
            } catch (Exception e) {
                e.printStackTrace();
            } finally {
                rs.close();
                st.close();
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }
}