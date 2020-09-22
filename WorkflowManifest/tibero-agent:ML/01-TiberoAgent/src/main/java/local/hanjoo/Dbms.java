package local.hanjoo;

import java.io.BufferedWriter;
import java.io.IOException;
import java.io.FileWriter;
import java.io.File;
import java.sql.*;

public class Dbms {

    private final Connection con;
    private String sql;
    private String table;
    private String col;

    public Dbms(Connection con) {
        this.con = con;
    }

    // Set -------------------------------------------------------------------------------------------------------------
    public void setTable(String table) {
        this.table = table;
        sql = "SELECT * FROM " + table;
    }

    public void setCol(String col) {
        this.col = col;
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

    public void showCol() {
        try {
            Statement st = con.createStatement();
            ResultSet rs = st.executeQuery(sql);
            try {
                while (rs.next()) {
                    if (rs.getString(col) == null) {
                        System.out.print("null");
                    } else {
                        System.out.print(rs.getString(col));
                    }
                    System.out.print(" ");
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

    // Output  ----------------------------------------------------------------------------------------------------------
    public void outCol() {
        try {
            String path = ".//Output";

            File Folder = new File(path);
            if (!Folder.exists()) {
                Folder.mkdir();
            }

            String fileContent = "";

            try {
                Statement st = con.createStatement();
                ResultSet rs = st.executeQuery(sql);
                try {
                    while (rs.next()) {
                        if (rs.getString(col) == null) {
                            fileContent += " ";
                        } else {
                            fileContent += rs.getString(col);
                        }
                        fileContent += " ";
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

            BufferedWriter writer = new BufferedWriter(new FileWriter(path + "//" + col + ".txt"));

            writer.write(fileContent);
            writer.close();

        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}